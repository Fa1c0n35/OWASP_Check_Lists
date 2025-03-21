import requests
import re

def check_asp_net_debug_misconfiguration(url):
    try:
        # Check for the presence of debug symbols (e.g., .pdb files)
        pdb_urls = [url + "/bin/somefile.pdb", url + "/bin/anotherfile.pdb"]
        for pdb_url in pdb_urls:
            response = requests.get(pdb_url)
            if response.status_code == 200:
                print(f"Debug binary found: {pdb_url}")
            else:
                print(f"No debug binary found at: {pdb_url}")
        
        # Check for possible debug-related error messages or settings in the page content
        response = requests.get(url)
        if 'debug="true"' in response.text:
            print("Warning: Debugging is enabled in the web.config file (debug='true').")
        
        # Check for any potential debug-related query parameters or URLs
        if re.search(r'\?debug=true', url):
            print("Warning: Debugging query parameter found in the URL (e.g., ?debug=true).")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

# Get URL input from the user
target_url = input("Please enter the target URL (e.g., https://example.com): ")
check_asp_net_debug_misconfiguration(target_url)
