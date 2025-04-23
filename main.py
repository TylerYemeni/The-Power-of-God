import os
import time
import random
import threading
from modules.whatsapp_report import report_number
from modules.ip_manager import change_ip, print_ip
from modules.fake_data import generate_identity
from modules.logger import log_report
from modules.email_report import send_email_report
from modules.self_detector import is_banned
from modules.google_voice import assign_google_voice_number
from modules.twilio_sms import send_twilio_sms

BANNER = """
██████╗  ██████╗ ██╗    ██╗███████╗ ██████╗ ██████╗  ██████╗  ██████╗ 
██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔═══██╗██╔══██╗██╔═══██╗██╔════╝ 
██████╔╝██║   ██║██║ █╗ ██║█████╗  ██║   ██║██████╔╝██║   ██║██║  ███╗
██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██║   ██║██╔═══╝ ██║   ██║██║   ██║
██║     ╚██████╔╝╚███╔███╔╝███████╗╚██████╔╝██║     ╚██████╔╝╚██████╔╝
╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝ ╚═════╝ ╚═╝      ╚═════╝  ╚═════╝ 
          WhatsApp Number Destroyer - by Abu Salem
"""

TARGET_NUMBERS = [
    "+966500000000",
    "+967770000000",
]

EMAIL_TARGET = "support@whatsapp.com"

def run_attack(target):
    identity = generate_identity()
    change_ip()
    print_ip()

    if is_banned():
        print(f"[!] رقمك محظور مؤقتًا من واتساب. التوقف عن البلاغات.")
        return

    # إرسال بلاغ مباشر إلى واتساب
    success = report_number(target, identity)
    log_report(target, identity, success)

    # إرسال بلاغ عبر الإيميل
    send_email_report(EMAIL_TARGET, identity["name"])

    # إرسال SMS وهمي
    voice_number = assign_google_voice_number()
    fake_msg = f"الرقم {target} يرسل تهديدات، الرجاء التحقيق."
    send_twilio_sms(target, fake_msg)

    time.sleep(random.uniform(1.5, 4.0))  # Random delay لتفادي الاكتشاف

if __name__ == "__main__":
    os.system("clear")
    print(BANNER)

    while True:
        for number in TARGET_NUMBERS:
            t = threading.Thread(target=run_attack, args=(number,))
            t.start()
            time.sleep(random.uniform(0.5, 1.5))  # تأخير بين إنشاء الجلسات

        time.sleep(10)  # وقت بين كل دورة هجوم
