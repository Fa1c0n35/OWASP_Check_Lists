import requests

# Define test cases for unauthorized access
test_endpoints = [
    "/admin",            # Common admin panel
    "/user/1",           # User profile access
    "/api/transactions", # Sensitive API endpoint
    "/settings",         # Application settings
]

# Headers without authentication
unauthorized_headers = {
    "User-Agent": "Mozilla/5.0",
}

def check_missing_authorization(target_url):
    print(f"[*] Checking for CWE-862 at: {target_url}")

    for endpoint in test_endpoints:
        test_url = f"{target_url}{endpoint}"
        try:
            response = requests.get(test_url, headers=unauthorized_headers, timeout=5)

            if response.status_code == 200 and "error" not in response.text.lower():
                print(f"[!] Possible Vulnerability: Unauthorized access allowed -> {test_url}")
            elif response.status_code in [401, 403]:
                print(f"[-] Proper authorization enforced for: {test_url}")

        except requests.exceptions.RequestException as e:
            print(f"[-] Error accessing {test_url}: {e}")

# Get user input
target_url = input("Enter the target URL (e.g., https://example.com): ")
check_missing_authorization(target_url)
