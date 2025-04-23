import smtplib
from email.message import EmailMessage

def send_email_report(target_email, fake_name, fake_image="samples/fake_profile.jpg", fake_audio="samples/fake_voice.mp3"):
    msg = EmailMessage()
    msg['Subject'] = "بلاغ عاجل - محتوى مسيء على واتساب"
    msg['From'] = "your_email@gmail.com"  # غيّر هذا لاحقًا
    msg['To'] = target_email
    msg.set_content(f"نبلغ عن الرقم المزعج المرتبط بشخصية {fake_name}. التفاصيل في الملفات المرفقة.")

    with open(fake_image, 'rb') as img:
        msg.add_attachment(img.read(), maintype='image', subtype='jpeg', filename='profile.jpg')
    
    with open(fake_audio, 'rb') as aud:
        msg.add_attachment(aud.read(), maintype='audio', subtype='mpeg', filename='voice.mp3')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("your_email@gmail.com", "your_password")  # غيّرها حسب بياناتك
        smtp.send_message(msg)
