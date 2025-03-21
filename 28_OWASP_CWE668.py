import requests

# List of common sensitive resources
sensitive_endpoints = [
    "/admin", "/config", "/api/internal", "/.git", "/.env", "/db_backup.sql",
    "/private", "/server-status", "/debug"
]

def check_exposed_resources(target_url):
    print(f"[*] Checking for exposed resources at: {target_url}")

    for endpoint in sensitive_endpoints:
        url = target_url.rstrip("/") + endpoint
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                print(f"[!] Possible Vulnerability: Exposed resource found -> {url}")
                if "password" in response.text.lower() or "apikey" in response.text.lower():
                    print(f"[!!] Warning: Sensitive information detected at {url}")

        except requests.exceptions.RequestException as e:
            print(f"[-] Error accessing {url}: {e}")

# Get user input
target_url = input("Enter the target URL (e.g., https://example.com): ")
check_exposed_resources(target_url)
