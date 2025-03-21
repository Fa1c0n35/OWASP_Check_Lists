import requests

# Example URL and endpoints to check
target_url = input("Enter the target URL (e.g., https://example.com): ")
endpoints = [
    "/admin", "/dashboard", "/settings", 
    "/api/user/1", "/api/admin/config"
]

# Example headers (modify token for unauthorized access attempts)
headers_admin = {"Authorization": "Bearer VALID_ADMIN_TOKEN"}
headers_user = {"Authorization": "Bearer VALID_USER_TOKEN"}

def check_access_control():
    print("Checking for Improper Access Control...")

    for endpoint in endpoints:
        url = target_url + endpoint

        # Send request as a normal user
        response_user = requests.get(url, headers=headers_user)

        if response_user.status_code == 200:
            print(f"[!] Possible Access Control Issue: {url} is accessible by a normal user!")
        else:
            print(f"[-] Restricted Access (OK): {url}")

check_access_control()
