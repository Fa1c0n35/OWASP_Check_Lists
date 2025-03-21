import requests

# List of test redirect URLs
TEST_URLS = [
    "http://evil.com",
    "//evil.com",
    "/\\evil.com",
    "https://evil.com",
    "https://google.com@evil.com",
    "https://example.com@evil.com"
]

def check_open_redirect(target_url):
    print(f"[*] Checking for open redirect at {target_url}...")

    for test_redirect in TEST_URLS:
        test_url = target_url.replace("{{REDIRECT}}", test_redirect)  # Replace placeholder with test value
        try:
            response = requests.get(test_url, allow_redirects=False, timeout=5)
            if "Location" in response.headers and response.headers["Location"] in TEST_URLS:
                print(f"[!] Possible Vulnerability: Redirecting to {response.headers['Location']} -> {test_url}")
            else:
                print(f"[-] No open redirect for {test_redirect}")
        except requests.exceptions.RequestException as e:
            print(f"[-] Error accessing {test_url}: {e}")

# Get user input
target_url = input("Enter the target URL with {{REDIRECT}} placeholder (e.g., https://example.com/login?redirect={{REDIRECT}}): ")
check_open_redirect(target_url)
