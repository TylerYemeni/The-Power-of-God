from datetime import datetime

def log_report(number, identity, success):
    with open("reports.log", "a") as log:
        log.write(f"{datetime.now()} - {number} | {identity['email']} | {'نجح' if success else 'فشل'}\n")
    print(f"[=] {'تم الحظر' if success else 'لم يُحظر'} للرقم {number}")
