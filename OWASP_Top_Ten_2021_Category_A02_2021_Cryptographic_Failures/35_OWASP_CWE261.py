import requests
import base64
import codecs
import re

def detect_weak_encoding(text):
    """Check if a given text is weakly encoded."""
    
    # Check for Base64 encoding
    try:
        decoded_base64 = base64.b64decode(text).decode('utf-8')
        if re.match(r'^[a-zA-Z0-9@#$%^&+=]{6,}$', decoded_base64):  
            return f"[!] Weak Encoding Found: Base64 -> {decoded_base64}"
    except Exception:
        pass  

    # Check for ROT13 encoding
    decoded_rot13 = codecs.encode(text, 'rot_13')
    if re.match(r'^[a-zA-Z0-9@#$%^&+=]{6,}$', decoded_rot13):
        return f"[!] Weak Encoding Found: ROT13 -> {decoded_rot13}"

    return None  

def check_weak_password_encoding(url):
    """Scan a website for weakly encoded passwords."""
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"[*] Checking for weak password encoding at {url}...")
            
            # Extract potential password fields from response
            potential_passwords = re.findall(r'["\'](.*?)["\']', response.text)
            
            for password in potential_passwords:
                result = detect_weak_encoding(password)
                if result:
                    print(result)
            
            print("[+] Scan complete.")

        else:
            print(f"[!] Failed to fetch {url}. HTTP Status: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"[!] Error accessing {url}: {e}")

# Get target URL from the user
target_url = input("Enter the target URL (e.g., https://example.com/api/userinfo): ")
check_weak_password_encoding(target_url)
