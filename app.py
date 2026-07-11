import platform
import os
import sys

def run_hardware_scan():
    print("=" * 40)
    print("      OSINT HARDWARE AUDIT TOOL        ")
    print("=" * 40)
    
    # 1. System OS Info
    print(f"[+] Operating System: {platform.system()}")
    print(f"[+] OS Release Version: {platform.release()}")
    print(f"[+] OS Machine Architecture: {platform.machine()}")
    
    # 2. CPU Details
    print(f"[+] Processor Type: {platform.processor()}")
    
    # 3. Python Environment Details
    print(f"[+] Python Version: {sys.version.split()[0]}")
    print(f"[+] Executable Path: {sys.executable}")
    
    # 4. Check for Apple Silicon specifics safely
    if platform.system() == "Darwin":
        print("[*] macOS Detected! Scanning for Apple Silicon elements...")
        # Check if running under Rosetta emulation or native ARM
        is_arm = "ARM64" in platform.version().upper() or platform.machine().lower() == "arm64"
        print(f"[+] Native Apple Silicon (ARM64): {is_arm}")
    else:
        print("[!] Non-Mac system detected. Apple hardware extensions skipped.")
        
    print("=" * 40)
    print("Scan complete. Ready for cross-platform validation.")

if __name__ == "__main__":
    run_hardware_scan()
