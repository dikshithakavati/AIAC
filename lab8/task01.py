def is_valid_email(email):
	"""
	Validates an email address based on the following rules:
	- Must contain both '@' and '.' characters.
	- Must not start or end with special characters ('@' or '.').
	- Should not allow multiple '@' symbols.
	"""
	if not isinstance(email, str):
		return False
	if '@' not in email or '.' not in email:
		return False
	if email.startswith('@') or email.startswith('.') or email.endswith('@') or email.endswith('.'):
		return False
	if email.count('@') != 1:
		return False
	return True

if __name__ == "__main__":
	test_cases = [
		# Valid emails
		("user@example.com", True),
		("john.doe@mail.co.uk", True),
		("a.b@c.d", True),
		("a@b.c", True),
		("user_123@domain.co", True),
		# Invalid: missing '@'
		("userexample.com", False),
		# Invalid: missing '.'
		("user@examplecom", False),
		# Invalid: starts with '@'
		("@user.com", False),
		# Invalid: ends with '@'
		("user.com@", False),
		# Invalid: starts with '.'
		(".user@example.com", False),
		# Invalid: ends with '.'
		("user@example.com.", False),
		# Invalid: multiple '@'
		("user@@example.com", False),
		("user@ex@ample.com", False),
		# Invalid: only '@' and '.'
		("@.", False),
		# Invalid: empty string
		("", False),
		# Invalid: only special characters
		("@.", False),
		# Invalid: '@' and '.' at the ends
		("@user.com.", False),
	]

	for email, expected in test_cases:
		result = is_valid_email(email)
		print(f"is_valid_email({email!r}) == {result} (expected: {expected}) {'✅' if result == expected else '❌'}")
