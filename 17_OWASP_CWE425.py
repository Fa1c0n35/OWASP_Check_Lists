import requests

# List of common restricted paths
restricted_paths = [
    "/admin", "/config", "/debug", "/backup.zip", "/error.log",
    "/user/1/profile", "/private", "/api/v1/secret-data"
]

def check_forced_browsing(target_url):
    print(f"[*] Checking forced browsing vulnerabilities on: {target_url}")

    for path in restricted_paths:
        full_url = target_url.rstrip("/") + path
        response = requests.get(full_url)

        if response.status_code == 200:
            print(f"[!] Possible Forced Browsing vulnerability: {full_url} (Check access manually)")
        elif response.status_code == 403:
            print(f"[+] Access denied to {full_url} (Good)")
        else:
            print(f"[-] {full_url} returned {response.status_code}")

# Get user input
target_url = input("Enter the target URL (e.g., https://example.com): ")
check_forced_browsing(target_url)
