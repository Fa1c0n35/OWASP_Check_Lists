import requests

# Common sensitive file locations
SENSITIVE_FILES = [
    "/.env", "/config.json", "/config.yml", "/config.php", "/web.config",
    "/debug.log", "/error.log", "/database.sql", "/backup.sql", "/dump.sql"
]

def check_sensitive_files(target_url):
    print(f"[*] Scanning {target_url} for exposed sensitive files...")

    for file_path in SENSITIVE_FILES:
        full_url = target_url.rstrip("/") + file_path
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200 and len(response.text) > 10:
                print(f"[!] Possible Vulnerability: {full_url} (Check manually)")
        except requests.exceptions.RequestException as e:
            print(f"[-] Error accessing {full_url}: {e}")

# Get user input
target_url = input("Enter the target URL (e.g., https://example.com): ")
check_sensitive_files(target_url)
