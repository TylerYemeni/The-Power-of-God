import random
import string
import requests

def generate_identity():
    names = ["أبو سالم", "خالد", "ناصر", "محمد", "جهاد"]
    name = random.choice(names)
    email = name.lower() + ''.join(random.choices(string.digits, k=4)) + "@gmail.com"
    avatar_url = f"https://i.pravatar.cc/150?img={random.randint(1, 70)}"
    voice_sample = "samples/fake_voice.mp3"  # مسار صوت وهمي

    return {
        "name": name,
        "email": email,
        "avatar": avatar_url,
        "voice": voice_sample
    }
