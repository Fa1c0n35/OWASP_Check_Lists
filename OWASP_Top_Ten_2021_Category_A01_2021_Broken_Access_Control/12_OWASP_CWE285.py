import requests

# Target URL and endpoints to check
target_url = input("Enter the target URL (e.g., https://example.com): ")
endpoints = [
    "/admin", "/user/settings", "/api/admin/users", 
    "/api/transactions", "/api/user/1/profile"
]

# Headers for different user roles
headers_admin = {"Authorization": "Bearer VALID_ADMIN_TOKEN"}
headers_user = {"Authorization": "Bearer VALID_USER_TOKEN"}

def check_improper_authorization():
    print("Checking for Improper Authorization...")

    for endpoint in endpoints:
        url = target_url + endpoint

        # Test with normal user token
        response_user = requests.get(url, headers=headers_user)

        if response_user.status_code == 200:
            print(f"[!] Possible Authorization Issue: {url} is accessible by a normal user!")
        else:
            print(f"[-] Access Restricted (OK): {url}")

check_improper_authorization()
