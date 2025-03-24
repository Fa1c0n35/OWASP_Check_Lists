import requests

# Define test cases for incorrect authorization
test_endpoints = {
    "Admin Panel": "/admin",
    "Modify Other User": "/api/user/2/edit",
    "Financial Transactions": "/api/transactions",
    "System Settings": "/api/settings"
}

# Low-privileged user token (replace with actual test token)
low_privilege_headers = {
    "Authorization": "Bearer LOW_PRIVILEGE_USER_TOKEN",
    "User-Agent": "Mozilla/5.0"
}

def check_incorrect_authorization(target_url):
    print(f"[*] Checking for CWE-863 at: {target_url}")

    for name, endpoint in test_endpoints.items():
        test_url = f"{target_url}{endpoint}"
        try:
            response = requests.get(test_url, headers=low_privilege_headers, timeout=5)

            if response.status_code == 200:
                print(f"[!] Possible Vulnerability: Incorrect Authorization -> {test_url} ({name})")
            elif response.status_code in [401, 403]:
                print(f"[-] Proper authorization enforced for: {test_url} ({name})")

        except requests.exceptions.RequestException as e:
            print(f"[-] Error accessing {test_url}: {e}")

# Get user input
target_url = input("Enter the target URL (e.g., https://example.com): ")
check_incorrect_authorization(target_url)
