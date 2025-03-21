import requests
import re

def check_sensitive_data_exposure(url):
    print(f"Checking for Exposure of Sensitive Information on: {url}")

    # Common sensitive keywords to look for in responses
    sensitive_keywords = ["password", "token", "session", "api_key", "credit_card", "secret"]

    # Make a request to the URL
    response = requests.get(url)

    # Check for sensitive data in URL parameters
    if any(param in url for param in sensitive_keywords):
        print(f"[!] Possible sensitive data exposure in URL: {url}")

    # Check for sensitive data in response body
    for keyword in sensitive_keywords:
        if re.search(rf"{keyword}\s*=\s*[\"']?[\w-]+[\"']?", response.text, re.IGNORECASE):
            print(f"[!] Possible sensitive data exposure found in response: {keyword}")

    # Check for sensitive data in headers
    for header, value in response.headers.items():
        if any(keyword in value.lower() for keyword in sensitive_keywords):
            print(f"[!] Sensitive information found in header: {header}: {value}")

    # Check for sensitive cookies
    if "Set-Cookie" in response.headers:
        cookies = response.headers["Set-Cookie"]
        if any(keyword in cookies.lower() for keyword in sensitive_keywords):
            print(f"[!] Sensitive information found in cookie: {cookies}")

# Get the target URL from the user
target_url = input("Please enter the target URL (e.g., https://example.com): ")
check_sensitive_data_exposure(target_url)
