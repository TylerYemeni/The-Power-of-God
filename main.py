import os
import time
import random
import threading
from modules.whatsapp_report import report_number
from modules.ip_manager import change_ip, print_current_ip
from modules.fake_data import generate_identity
from modules.logger import log_report
from ui.cli_ui import show_banner, loading_animation

TARGET_NUMBERS = [
    "+966500000000",  # رقم سعودي وهمي
    "+967770000000",  # رقم يمني وهمي
]

def run_attack(target):
    identity = generate_identity()
    change_ip()
    print_current_ip()
    loading_animation(f"إرسال بلاغ إلى {target} من {identity['name']}")
    success = report_number(target, identity)
    log_report(target, identity, success)

if __name__ == "__main__":
    os.system("clear")
    show_banner()
    while True:
        for number in TARGET_NUMBERS:
            t = threading.Thread(target=run_attack, args=(number,))
            t.start()
        time.sleep(10)
