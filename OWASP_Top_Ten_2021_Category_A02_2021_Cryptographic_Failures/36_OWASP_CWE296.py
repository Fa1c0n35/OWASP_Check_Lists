import requests

def check_certificate_validation(target_url):
    try:
        print(f"[*] Checking SSL certificate validation for: {target_url}")
        response = requests.get(target_url, verify=True)  # Ensure SSL verification is enabled
        print(f"[+] SSL certificate validation is properly enforced. Status Code: {response.status_code}")
    except requests.exceptions.SSLError:
        print(f"[!] Possible vulnerability: Improper SSL certificate validation at {target_url}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error accessing {target_url}: {e}")

# Get URL input from the user
target_url = input("Enter the target URL (e.g., https://example.com): ")
check_certificate_validation(target_url)
