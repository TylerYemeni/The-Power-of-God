from twilio.rest import Client

# ضع بياناتك من https://twilio.com
ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
AUTH_TOKEN = "your_auth_token"
FROM_NUMBER = "+1234567890"

def send_twilio_sms(to_number, message):
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=FROM_NUMBER,
            to=to_number
        )
        print("[+] تم إرسال رسالة Twilio وهمية.")
    except Exception as e:
        print(f"[!] فشل إرسال SMS: {e}")
