import requests
import base64
import codecs
import re
import json

def detect_weak_encoding(value, key_path):
    """Check if a given value is weakly encoded and return its path in the response."""
    
    # Check for Base64 encoding
    try:
        decoded_base64 = base64.b64decode(value).decode('utf-8')
        if re.match(r'^[a-zA-Z0-9@#$%^&+=]{6,}$', decoded_base64):  
            return f"[!] Weak Encoding Found (Base64) at {key_path}: {decoded_base64}"
    except Exception:
        pass  

    # Check for ROT13 encoding
    decoded_rot13 = codecs.encode(value, 'rot_13')
    if re.match(r'^[a-zA-Z0-9@#$%^&+=]{6,}$', decoded_rot13):
        return f"[!] Weak Encoding Found (ROT13) at {key_path}: {decoded_rot13}"

    return None  

def extract_values(data, path="response"):
    """Recursively extract values from JSON and return paths."""
    if isinstance(data, dict):
        for key, value in data.items():
            yield from extract_values(value, f"{path} -> {key}")
    elif isinstance(data, list):
        for index, item in enumerate(data):
            yield from extract_values(item, f"{path}[{index}]")
    else:
        yield path, str(data)

def check_weak_password_encoding(url):
    """Scan a website for weakly encoded passwords and show paths."""
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"[*] Checking for weak password encoding at {url}...\n")
            
            # Try parsing JSON responses
            try:
                json_data = response.json()
                data_pairs = list(extract_values(json_data))  # Extract JSON key-value pairs
            except ValueError:
                data_pairs = re.findall(r'(["\']?)(\w+)\1\s*:\s*["\']([^"\']+)["\']', response.text)
            
            found_issues = False
            
            for path, value in data_pairs:
                result = detect_weak_encoding(value, path)
                if result:
                    print(result)
                    found_issues = True
            
            if not found_issues:
                print("[+] No weakly encoded passwords detected.")

        else:
            print(f"[!] Failed to fetch {url}. HTTP Status: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"[!] Error accessing {url}: {e}")

# Get target URL from the user
target_url = input("Enter the target URL (e.g., https://example.com/api/userinfo): ")
check_weak_password_encoding(target_url)
