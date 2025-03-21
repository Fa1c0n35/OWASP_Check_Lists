import requests

# List of commonly exposed sensitive files
sensitive_files = [
    "config.php", "web.config", ".env", "appsettings.json",
    "database.yml", "debug.log", "error.log", "backup.zip",
    "backup.sql", "dump.sql", "db_backup.tar.gz", ".git/config"
]

def check_exposed_files(url):
    print(f"Checking for exposed sensitive files on: {url}")

    for file in sensitive_files:
        target_url = f"{url}/{file}"
        response = requests.get(target_url)

        if response.status_code == 200:
            print(f"[!] Possible Vulnerability: {target_url} (Check content manually)")
        elif response.status_code == 403:
            print(f"[!] Restricted access but exists: {target_url} (May be protected but still exists)")
        else:
            print(f"[-] Not found: {target_url}")

# Get the target URL from the user
target_url = input("Please enter the target URL (e.g., https://example.com): ")
check_exposed_files(target_url)
