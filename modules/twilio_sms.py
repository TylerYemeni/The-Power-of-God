from twilio.rest import Client

def send_twilio_sms(target_number, fake_msg):
    account_sid = 'YOUR_SID'
    auth_token = 'YOUR_AUTH_TOKEN'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=fake_msg,
        from_='+1XXXXXXXXXX',  # رقم Twilio الخاص بك
        to=target_number
    )
    return message.sid
