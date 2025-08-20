"""
Ethical, privacy-conscious logging utilities for Python web applications.

This module provides a safe logging configuration that:
- Redacts sensitive fields (e.g., passwords, tokens, emails, personal identifiers)
- Discourages logging request/response bodies by default
- Encourages an allowlist approach when logging metadata

Ethical logging principles implemented here:
- Log only what you need for operability (errors, timing, coarse-grained context).
- Never log secrets or personal data. Prefer allowlists over denylists.
- Treat logs as production data: protect, rotate, and minimize retention.
- Consider regulatory requirements (e.g., GDPR/CCPA/PCI) and your data classification policy.
"""

from __future__ import annotations

import json
import logging
import re
import sys
from logging import Logger
from typing import Any, Dict, Iterable, Mapping, MutableMapping, Optional


REDACTED = "[REDACTED]"


# Patterns for accidental sensitive data that can appear in free text. These are
# intentionally conservative, redacting common formats without attempting to
# perfectly identify every case (to avoid false negatives).
EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
SSN_PATTERN = re.compile(r"\b\d{3}-?\d{2}-?\d{4}\b")
# This pattern is broad to catch many card-like sequences; we avoid logging bodies anyway.
CARD_PATTERN = re.compile(r"\b(?:\d[ -]?){13,19}\b")
TOKENISH_PATTERN = re.compile(r"(?i)\b(?:bearer\s+)?[a-z0-9-_]{20,}\b")


# Common sensitive keys we should NEVER log in cleartext. Use lowercase for comparisons.
SENSITIVE_KEYS = {
    "password",
    "pass",
    "pwd",
    "secret",
    "token",
    "access_token",
    "refresh_token",
    "authorization",
    "api_key",
    "apikey",
    "session",
    "cookie",
    "set-cookie",
    "ssn",
    "email",
    "phone",
    "mobile",
    "dob",
    "date_of_birth",
    "address",
    "credit_card",
    "card",
    "card_number",
    "cvv",
    "pin",
    "otp",
    "user_id",
    "customer_id",
}


def _redact_string(value: str) -> str:
    """Redact likely sensitive substrings within a string.

    This is a safety net for freeform text. Primary protection should be to avoid
    logging sensitive content at all.
    """

    value = EMAIL_PATTERN.sub(REDACTED, value)
    value = SSN_PATTERN.sub(REDACTED, value)
    value = CARD_PATTERN.sub(REDACTED, value)
    value = TOKENISH_PATTERN.sub(REDACTED, value)
    return value


def _is_mapping(obj: Any) -> bool:
    return isinstance(obj, Mapping)


def _sanitize_mapping(data: Mapping[str, Any]) -> Dict[str, Any]:
    """Return a sanitized copy of a mapping, redacting sensitive keys and values.

    Ethical guidance:
    - Prefer to not include fields at all when not necessary.
    - When including data for operability, redact values for keys that can hold
      identifiers, secrets, or personal data.
    """

    sanitized: Dict[str, Any] = {}
    for key, value in data.items():
        key_lower = str(key).lower()
        if key_lower in SENSITIVE_KEYS:
            sanitized[key] = REDACTED
            continue

        sanitized[key] = sanitize_value(value)
    return sanitized


def sanitize_value(value: Any) -> Any:
    """Sanitize any value recursively.

    - Dicts/Maps: redact sensitive keys and sanitize nested values.
    - Lists/Tuples: sanitize each element.
    - Strings: mask email/SSN/card/token-like substrings.
    - Other primitives: returned as-is.
    """

    if _is_mapping(value):
        return _sanitize_mapping(value)  # type: ignore[arg-type]

    if isinstance(value, (list, tuple)):
        return [sanitize_value(v) for v in value]

    if isinstance(value, str):
        return _redact_string(value)

    return value


class SensitiveDataFilter(logging.Filter):
    """Logging filter that redacts sensitive data from records.

    This filter aims to be framework-agnostic. It safely handles:
    - record.msg and string formatting args
    - record.__dict__ extras (including 'extra'/'context' patterns)

    Note: The best protection is to avoid logging sensitive data entirely. This
    filter is a safety net in case something slips through.
    """

    def filter(self, record: logging.LogRecord) -> bool:  # noqa: D401
        # Sanitize formatted message text
        try:
            # getMessage() applies %-formatting with record.args
            message = record.getMessage()
            record.msg = _redact_string(message)
            record.args = ()
        except Exception:
            # If formatting fails, do not break logging
            pass

        # Sanitize common extra/context fields defensively
        for field_name in ("extra", "context", "payload", "details"):
            if hasattr(record, field_name):
                try:
                    original = getattr(record, field_name)
                    setattr(record, field_name, sanitize_value(original))
                except Exception:
                    setattr(record, field_name, REDACTED)

        # Avoid accidental header/body dumps if present
        for field_name in ("headers", "body", "request_body", "response_body"):
            if hasattr(record, field_name):
                setattr(record, field_name, "<omitted>")

        return True


class RedactingFormatter(logging.Formatter):
    """Formatter that emits structured JSON with redaction.

    JSON logs are easier to parse and safer to consume. We still avoid including
    potentially large or sensitive blobs.
    """

    def format(self, record: logging.LogRecord) -> str:  # noqa: D401
        base: Dict[str, Any] = {
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        # Include minimal contextual fields if present
        for key in ("context", "extra", "request_id", "route", "method", "path"):
            if hasattr(record, key):
                base[key] = getattr(record, key)

        safe = sanitize_value(base)
        try:
            return json.dumps(safe, ensure_ascii=False)
        except Exception:
            # Fall back to plain formatting if something is not serializable
            return f"{record.levelname} {record.name} {safe.get('message', '')}"


def configure_safe_logging(
    *,
    level: int | str = logging.INFO,
    json_output: bool = True,
    logger_name: Optional[str] = None,
) -> Logger:
    """Configure a safe default logger for a web application.

    Ethical defaults:
    - Console-only by default to respect unknown filesystem constraints.
    - Structured JSON logs for reliable parsing and downstream redaction.
    - SensitiveDataFilter applied globally as a safety net.

    Parameters:
    - level: minimum severity to log
    - json_output: if True, output JSON lines; otherwise, a concise text format
    - logger_name: name of the application logger; None selects the root logger
    """

    # Ensure root logger is configured once
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Clear existing handlers only if none are configured or if they output to default stderr
    if not root_logger.handlers:
        handler = logging.StreamHandler(stream=sys.stdout)
        handler.addFilter(SensitiveDataFilter())
        if json_output:
            handler.setFormatter(RedactingFormatter())
        else:
            text_format = "%(levelname)s %(name)s: %(message)s"
            handler.setFormatter(logging.Formatter(text_format))
        root_logger.addHandler(handler)
    else:
        # Add the filter to existing handlers for safety
        for h in root_logger.handlers:
            h.addFilter(SensitiveDataFilter())

    app_logger = logging.getLogger(logger_name) if logger_name else root_logger
    return app_logger


class SafeLoggerAdapter(logging.LoggerAdapter):
    """Logger adapter that sanitizes the 'extra' mapping and message.

    Prefer using this adapter when adding request or domain context.
    """

    def process(self, msg: Any, kwargs: MutableMapping[str, Any]):  # noqa: D401
        sanitized_msg = _redact_string(str(msg))
        if "extra" in kwargs and isinstance(kwargs["extra"], Mapping):
            kwargs["extra"] = sanitize_value(kwargs["extra"])  # type: ignore[index]
        return sanitized_msg, kwargs


def _allowlist_subset(
    data: Optional[Mapping[str, Any]],
    *,
    allowed_keys: Optional[Iterable[str]] = None,
) -> Dict[str, Any]:
    """Return only a safe subset of mapping based on an allowlist of keys."""

    if not data:
        return {}

    if not allowed_keys:
        return {}

    allowed = {k.lower() for k in allowed_keys}
    subset: Dict[str, Any] = {}
    for key, value in data.items():
        key_lower = str(key).lower()
        if key_lower in allowed and key_lower not in SENSITIVE_KEYS:
            subset[key] = sanitize_value(value)
    return subset


def build_http_request_context(
    *,
    method: str,
    path: str,
    ip: Optional[str] = None,
    user_agent: Optional[str] = None,
    route: Optional[str] = None,
    query_params: Optional[Mapping[str, Any]] = None,
    route_params: Optional[Mapping[str, Any]] = None,
    request_id: Optional[str] = None,
    allowed_query_keys: Optional[Iterable[str]] = None,
    allowed_route_param_keys: Optional[Iterable[str]] = None,
) -> Dict[str, Any]:
    """Build a minimal, privacy-conscious context dict for an HTTP request.

    Ethical defaults:
    - Do not include request/response bodies or full headers.
    - Only include allowlisted query and route parameters.
    - Avoid identifiers like user IDs unless strictly necessary.
    """

    context: Dict[str, Any] = {
        "method": method,
        "path": path,
    }
    if ip:
        context["ip"] = ip
    if user_agent:
        context["user_agent"] = _redact_string(user_agent)
    if route:
        context["route"] = route
    if request_id:
        context["request_id"] = request_id

    if query_params:
        context["query"] = _allowlist_subset(query_params, allowed_keys=allowed_query_keys)
    if route_params:
        context["route_params"] = _allowlist_subset(
            route_params, allowed_keys=allowed_route_param_keys
        )

    return sanitize_value(context)


def log_http_request(
    logger: Logger,
    *,
    method: str,
    path: str,
    ip: Optional[str] = None,
    user_agent: Optional[str] = None,
    route: Optional[str] = None,
    query_params: Optional[Mapping[str, Any]] = None,
    route_params: Optional[Mapping[str, Any]] = None,
    request_id: Optional[str] = None,
    allowed_query_keys: Optional[Iterable[str]] = None,
    allowed_route_param_keys: Optional[Iterable[str]] = None,
) -> None:
    """Log an inbound HTTP request with minimal, sanitized context.

    This function is framework-agnostic and can be called from middleware hooks
    in Flask, FastAPI, Django, etc.
    """

    context = build_http_request_context(
        method=method,
        path=path,
        ip=ip,
        user_agent=user_agent,
        route=route,
        query_params=query_params,
        route_params=route_params,
        request_id=request_id,
        allowed_query_keys=allowed_query_keys,
        allowed_route_param_keys=allowed_route_param_keys,
    )

    SafeLoggerAdapter(logger, {}).info("HTTP request", extra={"context": context})


def log_http_response(
    logger: Logger,
    *,
    status_code: int,
    duration_ms: Optional[float] = None,
    request_id: Optional[str] = None,
    route: Optional[str] = None,
) -> None:
    """Log an outbound HTTP response with minimal metadata.

    Ethical defaults:
    - Do not log response bodies or full headers.
    - Prefer coarse-grained timing only (e.g., total duration).
    """

    context: Dict[str, Any] = {"status": status_code}
    if duration_ms is not None:
        context["duration_ms"] = float(duration_ms)
    if request_id:
        context["request_id"] = request_id
    if route:
        context["route"] = route

    SafeLoggerAdapter(logger, {}).info("HTTP response", extra={"context": context})


# Example integration notes (do not execute in production as-is):
#
# Flask (app factory):
#     from flask import Flask, request, g
#
#     logger = configure_safe_logging(logger_name="myapp")
#
#     def before_request():
#         # Avoid logging request bodies. Use an allowlist for query params.
#         log_http_request(
#             logger,
#             method=request.method,
#             path=request.path,
#             ip=request.headers.get("X-Forwarded-For", request.remote_addr),
#             user_agent=request.headers.get("User-Agent"),
#             route=getattr(request.url_rule, "rule", None),
#             query_params=request.args,
#             route_params=request.view_args,
#             request_id=request.headers.get("X-Request-Id"),
#             allowed_query_keys=("page", "limit", "sort"),
#             allowed_route_param_keys=("resource",),
#         )
#
#     def after_request(response):
#         log_http_response(
#             logger,
#             status_code=response.status_code,
#             duration_ms=None,  # attach your timing measurement if available
#             request_id=request.headers.get("X-Request-Id"),
#             route=getattr(request.url_rule, "rule", None),
#         )
#         return response
#
#     app = Flask(__name__)
#     app.before_request(before_request)
#     app.after_request(after_request)
#     return app
#
# FastAPI (middleware sketch):
#     from fastapi import FastAPI, Request
#     import time
#
#     app = FastAPI()
#     logger = configure_safe_logging(logger_name="myapp")
#
#     @app.middleware("http")
#     async def logging_middleware(request: Request, call_next):
#         start = time.perf_counter()
#         log_http_request(
#             logger,
#             method=request.method,
#             path=request.url.path,
#             ip=request.headers.get("x-forwarded-for"),
#             user_agent=request.headers.get("user-agent"),
#             route=None,
#             query_params=dict(request.query_params),
#             route_params=request.path_params,
#             request_id=request.headers.get("x-request-id"),
#             allowed_query_keys=("page", "limit", "sort"),
#             allowed_route_param_keys=("resource",),
#         )
#
#         response = await call_next(request)
#         duration_ms = (time.perf_counter() - start) * 1000
#         log_http_response(
#             logger,
#             status_code=response.status_code,
#             duration_ms=duration_ms,
#             request_id=request.headers.get("x-request-id"),
#         )
#         return response


if __name__ == "__main__":
    # Minimal self-test demonstrating safe behavior. In production, import
    # configure_safe_logging() and call it during app startup.
    app_logger = configure_safe_logging(logger_name="example-app")
    safe_logger = SafeLoggerAdapter(app_logger, {})

    safe_logger.info(
        "User login attempt",
        extra={
            "context": {
                "username": "alice",  # usernames may still be identifiers; log only if necessary
                "password": "supersecret",  # will be redacted
                "email": "alice@example.com",  # will be redacted
                "ip": "203.0.113.5",
            }
        },
    )

    # Demonstrate string redaction safety net
    app_logger.warning(
        "Payment card provided 4111 1111 1111 1111, token abcdefghijklmnopqrstuvwxyz",
    )



