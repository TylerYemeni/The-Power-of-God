import random
import time

def report_number(number, identity):
    print(f"[+] الإبلاغ عن: {number} بواسطة {identity['email']}")
    time.sleep(random.uniform(2.5, 5.0))  # Delay عشوائي
    return random.choice([True, False, True])  # محاكاة نجاح وهمي
