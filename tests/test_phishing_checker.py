import unittest
from phishing_checker import inspect_url, has_warnings


class TestPhishingChecker(unittest.TestCase):
    def test_benign_url(self):
        url = "https://www.example.com/login"
        findings = inspect_url(url)
        self.assertIn("No listed warning signs found. This does NOT prove safety.", findings)
        self.assertFalse(has_warnings(findings))

    def test_ip_address_and_http(self):
        url = "http://192.0.2.10/account"
        findings = inspect_url(url)
        self.assertIn("Uses an IP address instead of a familiar domain.", findings)
        self.assertIn("Uses HTTP. HTTPS alone does not prove trust.", findings)
        self.assertTrue(has_warnings(findings))

    def test_at_symbol_and_http(self):
        url = "http://example.com@sample.invalid/login"
        findings = inspect_url(url)
        self.assertIn("Contains an @ symbol; inspect carefully.", findings)
        self.assertIn("Uses HTTP. HTTPS alone does not prove trust.", findings)
        self.assertTrue(has_warnings(findings))

    def test_many_hostname_segments(self):
        url = "https://a.b.c.d.e.example.invalid/path"
        findings = inspect_url(url)
        self.assertIn("Contains many hostname segments/subdomains.", findings)
        self.assertTrue(has_warnings(findings))

    def test_punycode_hostname(self):
        url = "https://xn--example.invalid/"
        findings = inspect_url(url)
        self.assertIn("Contains a punycode-style hostname.", findings)
        self.assertTrue(has_warnings(findings))

    def test_unusually_long_url(self):
        url = "https://example.com/" + "a" * 90
        self.assertGreater(len(url), 100)
        findings = inspect_url(url)
        self.assertIn("Unusually long URL (over 100 characters).", findings)
        self.assertTrue(has_warnings(findings))

    def test_empty_input(self):
        findings = inspect_url("")
        self.assertEqual(findings, ["No URL entered."])
        self.assertFalse(has_warnings(findings))

        findings_spaces = inspect_url("   ")
        self.assertEqual(findings_spaces, ["No URL entered."])
        self.assertFalse(has_warnings(findings_spaces))

    def test_malformed_url(self):
        findings = inspect_url("http://[bad")
        self.assertEqual(findings, ["This text is not a valid URL format."])
        self.assertFalse(has_warnings(findings))

    def test_missing_scheme_defaults_to_http(self):
        findings = inspect_url("www.example.com")
        self.assertIn("Uses HTTP. HTTPS alone does not prove trust.", findings)
        self.assertTrue(has_warnings(findings))


if __name__ == "__main__":
    unittest.main()

