import requests
def generate_fake_image(path="samples/fake_profile.jpg"):
    url = "https://thispersondoesnotexist.com/image"
    with open(path, "wb") as f:
        f.write(requests.get(url).content)
