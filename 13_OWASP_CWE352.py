import requests

# Target URL and CSRF-protected endpoint
target_url = input("Enter the target URL (e.g., https://example.com): ")
csrf_test_endpoint = "/account/settings"  # Modify based on the application

# Example user session cookie
cookies = {"session": "VALID_SESSION_COOKIE"}

def check_csrf():
    print("Checking for CSRF Vulnerability...")

    # Send a request without CSRF token
    response = requests.post(target_url + csrf_test_endpoint, cookies=cookies)

    if response.status_code == 200:
        print(f"[!] Possible CSRF Issue: {target_url + csrf_test_endpoint} accepted request without CSRF token!")
    else:
        print(f"[-] CSRF Protection Detected (OK): {target_url + csrf_test_endpoint}")

check_csrf()
