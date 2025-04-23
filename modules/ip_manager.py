import os
import subprocess

def change_ip():
    os.system("protonvpn-cli d")
    os.system("protonvpn-cli c --fastest")

def print_current_ip():
    try:
        ip = subprocess.getoutput("curl -s https://ipinfo.io/ip")
        print(f"[+] IP الحالي: {ip}")
    except:
        print("[-] فشل في جلب عنوان IP")
