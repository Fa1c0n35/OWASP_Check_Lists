import os
import tempfile

def insecure_temp_file():
    temp_file_path = "/tmp/insecure_temp.txt"  # Insecure method: hardcoded temp file

    # Writing data to the insecure temp file
    with open(temp_file_path, "w") as f:
        f.write("Sensitive Data\n")

    print(f"[!] Insecure temporary file created: {temp_file_path}")
    print("[!] This file can be accessed or modified by other users!")

def secure_temp_file():
    # Using tempfile.NamedTemporaryFile for a secure method
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Secure Data\n")
        print(f"[+] Secure temporary file created: {temp_file.name}")

if __name__ == "__main__":
    print("Checking for insecure temporary file usage...\n")
    
    # Example of insecure temp file usage
    insecure_temp_file()

    # Example of secure temp file usage
    secure_temp_file()
