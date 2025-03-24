import requests

# Common directories that may expose sensitive files
COMMON_DIRS = [
    "/uploads/", "/backup/", "/logs/", "/files/", "/.git/", "/config/", "/database/"
]

def check_directory_listing(target_url):
    print(f"[*] Checking for directory listing vulnerabilities on {target_url}...")

    for directory in COMMON_DIRS:
        url = target_url.rstrip("/") + directory  # Ensure proper URL format
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200 and "Index of" in response.text:
                print(f"[!] Possible Vulnerability: Directory listing enabled at {url}")
            else:
                print(f"[-] No directory listing detected at {url}")
        except requests.exceptions.RequestException as e:
            print(f"[-] Error accessing {url}: {e}")

# Get user input
target_url = input("Enter the target URL (e.g., https://example.com): ")
check_directory_listing(target_url)
