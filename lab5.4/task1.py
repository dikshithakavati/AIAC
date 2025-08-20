
import json
import os
import sys
import hashlib
import hmac
from typing import List, Dict, Any


def hash_email(email: str, pepper: str | None = None) -> str:
    normalized_email = email.strip().lower()
    if pepper:
        return hmac.new(pepper.encode("utf-8"), normalized_email.encode("utf-8"), hashlib.sha256).hexdigest()
    return hashlib.sha256(normalized_email.encode("utf-8")).hexdigest()


def read_users(filepath: str) -> List[Dict[str, Any]]:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def write_users(filepath: str, users: List[Dict[str, Any]]) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)


def prompt_nonempty(prompt_text: str) -> str:
    while True:
        value = input(prompt_text).strip()
        if value:
            return value
        print("Please enter a non-empty value.")


def prompt_age(prompt_text: str) -> int:
    while True:
        raw = input(prompt_text).strip()
        try:
            age = int(raw)
            if age < 0:
                print("Age cannot be negative.")
                continue
            return age
        except ValueError:
            print("Please enter a valid whole number for age.")


def main() -> None:
    data_file = "users.json"
    name = prompt_nonempty("Enter your name: ")
    age = prompt_age("Enter your age: ")
    email = prompt_nonempty("Enter your email: ")
    pepper = os.getenv("EMAIL_PEPPER", "")
    email_digest = hash_email(email, pepper=pepper if pepper else None)
    users = read_users(data_file)
    users.append({
        "name": name,
        "age": age,
        "email_sha256": email_digest,
    })
    write_users(data_file, users)
    print("Thank you! Your data has been saved.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation canceled.")
        sys.exit(1)