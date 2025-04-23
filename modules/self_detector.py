import requests

def is_banned():
    try:
        r = requests.get("https://web.whatsapp.com/")
        if "temporarily unavailable" in r.text.lower():
            return True
    except:
        return False
    return False
