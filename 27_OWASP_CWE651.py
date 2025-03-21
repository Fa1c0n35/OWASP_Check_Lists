import requests

def check_wsdl_exposure(target_url):
    wsdl_url = target_url.rstrip("/") + "?wsdl"
    print(f"[*] Checking for exposed WSDL file at: {wsdl_url}")

    try:
        response = requests.get(wsdl_url, timeout=5)

        if response.status_code == 200 and "definitions" in response.text:
            print(f"[!] Possible Vulnerability: Exposed WSDL file found -> {wsdl_url}")
            # Check for sensitive data patterns in WSDL
            if any(keyword in response.text.lower() for keyword in ["password", "apikey", "authentication", "internal"]):
                print(f"[!!] Warning: Sensitive information detected in WSDL file!")
        else:
            print("[-] No WSDL file found or not accessible.")

    except requests.exceptions.RequestException as e:
        print(f"[-] Error accessing {wsdl_url}: {e}")

# Get user input
target_url = input("Enter the target URL (e.g., https://example.com/service): ")
check_wsdl_exposure(target_url)
