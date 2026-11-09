# Test Results

Tester: Mathias William (@mathiaswilliam761-ui) | Python version used: 3.13.14 | Operating system: Windows 11 | Date: 2026-11-06

| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | `https://www.example.com/login` | No listed warning signs | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | `http://192.0.2.10/account` | IP address + HTTP | Uses an IP address instead of a familiar domain. <br> Uses HTTP. HTTPS alone does not prove trust. <br> (REVIEW CAREFULLY: 2 warning sign(s) found.) | PASS |
| 3 | `http://example.com@sample.invalid/login` | @ symbol + HTTP | Contains an @ symbol; inspect carefully. <br> Uses HTTP. HTTPS alone does not prove trust. <br> (REVIEW CAREFULLY: 2 warning sign(s) found.) | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments | Contains many hostname segments/subdomains. <br> (REVIEW CAREFULLY: 1 warning sign(s) found.) | PASS |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname | Contains a punycode-style hostname. <br> (REVIEW CAREFULLY: 1 warning sign(s) found.) | PASS |

---

### Bonus Edge Case Checks

| # | Input | Expected Behavior | Actual Observation | Pass/Fail |
|---|-------|-------------------|--------------------|-----------|
| 6 | *(Empty string / Enter)* | Handles empty input gracefully | `No URL entered.` | PASS |
| 7 | `www.example.com` | Defaults to HTTP; flags plain HTTP | `Uses HTTP. HTTPS alone does not prove trust.` | PASS |
| 8 | `https://secure-login.example.invalid` | Deceptive name with no syntax clues slips through | `No listed warning signs found. This does NOT prove safety.` | PASS |
| 9 | `http://[bad` | Caught by try/except; prevents ValueError crash | `This text is not a valid URL format.` | PASS |

---

## Notes
- What I learned: A URL's text structure can reveal suspicious patterns before a browser ever connects. Attackers frequently leverage techniques like userinfo `@` obscuration, bare IP addresses, and deep subdomain stacking to deceive victims.
- What surprised me: An absence of warnings never proves a website is legitimate (`https://secure-login.example.invalid` triggers 0 warnings despite being potentially malicious). Conversely, legitimate services sometimes trigger warnings (such as corporate internal IP addresses or CDN subdomains). URL inspection is an awareness aid, not an absolute guarantee of safety.

