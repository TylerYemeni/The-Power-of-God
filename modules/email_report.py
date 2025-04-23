import smtplib
from email.mime.text import MIMEText

EMAIL_SENDER = "youremail@gmail.com"
EMAIL_PASSWORD = "your_app_password"

def send_email_report(to_email, fake_name):
    subject = "إبلاغ عن حساب مزعج في واتساب"
    body = f"""
    مرحبًا، أود الإبلاغ عن رقم يرسل رسائل مزعجة.

    الاسم: {fake_name}
    الرقم المشبوه: مزعج جداً

    الرجاء التحقيق، وشكرًا.
    """

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("[+] تم إرسال بلاغ إلى البريد.")
    except Exception as e:
        print(f"[!] فشل في إرسال البلاغ عبر البريد: {e}")
