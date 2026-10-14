#!/usr/bin/env python3
import socket
import sys
import os
import requests

# Colors
GREEN = "\033[1;32m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

VALID_KEY = "CYPHEER-2026-PRO"

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{CYAN}")
    print("  ____                  _                      ____  _     _ ")
    print(" / ___| _   _ _ __  | |__   ___  ___ _ __ / ___|| |__ (_) ___| | __| |")
    print("| |  _ | | | | '_ \ | '_ \ / _ \/ _ \ '__|\___ \| '_ \| |/ _ \ |/ _` |")
    print("| |_| || |_| | |_) || | | |  __/  __/ |    ___) | | | | |  __/ | (_| |")
    print(" \____| \__, | .__/ |_| |_|\___|\___|_|   |____/|_| |_|_|\___|_|\__,_|")
    print(f"        |___/|_|      {YELLOW}[ Created by Cypheeeeer7 ]{CYAN}")
    print(f"{RESET}")

def authenticate():
    banner()
    print(f"{YELLOW}[!] Access Restricted! License Key Required.{RESET}")
    user_key = input(f"{CYAN}[*] Enter License Key: {RESET}").strip()
    
    if user_key == VALID_KEY:
        print(f"{GREEN}[+] Key Validated Successfully! Welcome Cypheeeeer7.{RESET}\n")
        input("Press Enter to open dashboard...")
    else:
        print(f"{RED}[-] Invalid Key! Access Denied.{RESET}")
        sys.exit(1)

def header_check(target):
    print(f"\n{YELLOW}[*] Checking Security Headers for: {target}{RESET}")
    if not target.startswith("http://") and not target.startswith("https://"):
        target = "https://" + target
    try:
        response = requests.get(target, timeout=5)
        headers = response.headers
        security_headers = ["X-Frame-Options", "X-Content-Type-Options", "Strict-Transport-Security", "Content-Security-Policy"]
        for header in security_headers:
            if header in headers:
                print(f"{GREEN}[+] {header}: Present ({headers[header]}){RESET}")
            else:
                print(f"{RED}[-] {header}: MISSING! (Vulnerable){RESET}")
    except Exception as e:
        print(f"{RED}[-] Error connecting to target: {e}{RESET}")

def port_scan(target):
    print(f"\n{YELLOW}[*] Scanning Common Ports on: {target}{RESET}")
    target_ip = target.replace("https://", "").replace("http://", "").split("/")[0]
    ports = [21, 22, 80, 443, 3306, 8080]
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        res = s.connect_ex((target_ip, port))
        if res == 0:
            print(f"{GREEN}[+] Port {port}: OPEN{RESET}")
        else:
            print(f"{RED}[-] Port {port}: CLOSED{RESET}")
        s.close()

def main():
    authenticate()
    while True:
        banner()
        print(f"{CYAN}1. Security Headers Audit")
        print("2. Quick Port Scan")
        print(f"3. Exit{RESET}")
        choice = input(f"\n{YELLOW}Select Option [1-3]: {RESET}").strip()
        
        if choice == '1':
            t = input("[*] Enter Target Domain (e.g. example.com): ")
            header_check(t)
            input("\nPress Enter to return...")
        elif choice == '2':
            t = input("[*] Enter Target IP/Domain: ")
            port_scan(t)
            input("\nPress Enter to return...")
        elif choice == '3':
            print(f"{GREEN}Thanks for using CypheerShield!{RESET}")
            sys.exit(0)

if __name__ == "__main__":
    main()
