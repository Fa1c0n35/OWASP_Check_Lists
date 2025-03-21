import requests

# List of commonly exposed sensitive files and directories
COMMON_FILES = [
    "/.git/", "/.svn/", "/.env", "/config.php", "/web.config", "/db_backup.sql",
    "/backup.zip", "/error.log", "/debug.log", "/private_uploads/"
]

def check_exposed_files(target_url):
    print(f"[*] Checking for exposed files or directories on {target_url}...")

    for file_path in COMMON_FILES:
        url = target_url.rstrip("/") + file_path  # Ensure proper URL format
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[!] Possible Vulnerability: Exposed file or directory at {url}")
            else:
                print(f"[-] No access to {url}")
        except requests.exceptions.RequestException as e:
            print(f"[-] Error accessing {url}: {e}")

# Get user input
target_url = input("Enter the target URL (e.g., https://example.com): ")
check_exposed_files(target_url)

