import unittest
def deduplicate_emails(emails: list) -> list:
    seen = set()
    output = []
    for email in emails:
        lower_email = email.lower()
        if lower_email not in seen:
            seen.add(lower_email)
            output.append(email)
    return output
class TestEmailDeduplication(unittest.TestCase):
    def test_sample_input(self):
        input_list = ['A@x.com', 'a@x.com', 'B@y.com']
        expected_output = ['A@x.com', 'B@y.com']
        self.assertEqual(deduplicate_emails(input_list), expected_output)

    def test_no_duplicates(self):
        input_list = ['test@example.com', 'another@domain.net']
        expected_output = ['test@example.com', 'another@domain.net']
        self.assertEqual(deduplicate_emails(input_list), expected_output)

    def test_all_duplicates(self):
        input_list = ['user@mail.com', 'User@mail.com', 'USER@MAIL.COM']
        expected_output = ['user@mail.com']
        self.assertEqual(deduplicate_emails(input_list), expected_output)

    def test_mixed_case_duplicates(self):
        input_list = ['test@email.com', 'Test@email.com', 'unique@email.org', 'test@email.com', 'last@email.com']
        expected_output = ['test@email.com', 'unique@email.org', 'last@email.com']
        self.assertEqual(deduplicate_emails(input_list), expected_output)
if __name__ == '__main__':
    unittest.main(exit=False)
    print("\nExpected output without duplicates:")
    print(deduplicate_emails(['A@x.com', 'a@x.com', 'B@y.com']))
