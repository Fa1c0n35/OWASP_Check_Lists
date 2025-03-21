import requests
import re

def check_sensitive_info(target_url):
    print(f"[*] Scanning for exposed system information at: {target_url}")

    try:
        response = requests.get(target_url, timeout=5)

        # Check for sensitive headers
        sensitive_headers = ["Server", "X-Powered-By"]
        for header in sensitive_headers:
            if header in response.headers:
                print(f"[!] Potential Issue: {header} header found - {response.headers[header]}")

        # Check for leaked system information in response body
        patterns = [
            (r"([A-Z]:\\[^\n]+)", "Windows file path"),  # Windows file paths
            (r"(/[^/ ]+)+/", "Unix file path"),  # Unix file paths
            (r"\b(v?\d+\.\d+\.\d+)\b", "Version numbers"),  # Generic version numbers
            (r"(Exception|Traceback)", "Error stack traces")  # Common error messages
        ]

        for pattern, desc in patterns:
            if re.search(pattern, response.text):
                print(f"[!] Possible Issue: {desc} found in response.")

    except requests.exceptions.RequestException as e:
        print(f"[-] Error connecting to {target_url}: {e}")

# Get user input
target_url = input("Enter the target URL (e.g., https://example.com): ")
check_sensitive_info(target_url)
