import subprocess
import random
import time

def change_ip():
    print("[~] تغيير الـ VPN ...")
    try:
        subprocess.call(["protonvpn-cli", "disconnect"])
        time.sleep(2)
        server = random.choice(["US", "NL", "DE", "FR", "CH"])
        subprocess.call(["protonvpn-cli", "connect", "--cc", server])
        print(f"[+] تم الاتصال بـ VPN في {server}")
    except Exception as e:
        print(f"[!] خطأ في تغيير الـ VPN: {e}")

def print_ip():
    ip = subprocess.getoutput("curl -s ifconfig.me")
    print(f"[IP] عنوانك الحالي: {ip}")
