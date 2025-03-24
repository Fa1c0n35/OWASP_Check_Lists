import requests
import re
import ssl
import socket

# List of weak cryptographic algorithms and ciphers
WEAK_ALGORITHMS = ["md5", "sha1", "des", "rc4", "rsa-1024"]
WEAK_CIPHERS = ["RC4", "DES", "3DES"]
SECURE_HEADERS = ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options"]
SECURE_TLS_VERSIONS = ['TLSv1.2', 'TLSv1.3']

def check_weak_encryption(target_url):
    try:
        print(f"[*] Checking for cryptographic issues at: {target_url}")
        response = requests.get(target_url)

        if response.status_code == 200:
            for algo in WEAK_ALGORITHMS:
                if re.search(algo, response.text, re.IGNORECASE):
                    print(f"[!] Possible vulnerability: Weak encryption detected ({algo}) in {target_url}")

            # Check for weak ciphers in response body
            for cipher in WEAK_CIPHERS:
                if re.search(cipher, response.text, re.IGNORECASE):
                    print(f"[!] Weak cipher detected: {cipher} in {target_url}")

            # Check for missing security headers
            missing_headers = [h for h in SECURE_HEADERS if h not in response.headers]
            if missing_headers:
                print(f"[!] Missing security headers: {', '.join(missing_headers)}")

        else:
            print(f"[-] Unable to access {target_url}. Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"[-] Error accessing {target_url}: {e}")

def check_ssl_certificate(target_host):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((target_host, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=target_host) as secure_sock:
                cert = secure_sock.getpeercert()
                for entry in cert.get("subject", ()):
                    for key, value in entry:
                        if key == "commonName":
                            print(f"[*] SSL Certificate Common Name: {value}")
                
                # Check if certificate uses weak RSA key (e.g., 1024-bit)
                pubkey = cert.get("subjectPublicKeyInfo")
                if pubkey and "1024" in str(pubkey):
                    print("[!] Weak SSL Certificate Key: RSA-1024 detected!")

                # Check for weak key lengths (e.g., 512, 768-bit keys)
                if pubkey and "512" in str(pubkey):
                    print("[!] Weak SSL Certificate Key: 512-bit detected!")
                elif pubkey and "768" in str(pubkey):
                    print("[!] Weak SSL Certificate Key: 768-bit detected!")

                # Check supported SSL/TLS versions
                ssl_version = secure_sock.version()
                if ssl_version not in SECURE_TLS_VERSIONS:
                    print(f"[!] Insecure SSL/TLS version detected: {ssl_version}. Use TLSv1.2 or higher.")

    except Exception as e:
        print(f"[-] SSL Certificate check failed: {e}")

# Get URL input from the user
target_url = input("Enter the target URL (e.g., https://example.com): ")
target_host = target_url.replace("https://", "").replace("http://", "").split("/")[0]

# Run checks
check_weak_encryption(target_url)
check_ssl_certificate(target_host)
