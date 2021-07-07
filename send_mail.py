import requests

def send_mail(rec, txt):
    return requests.post(
        "API_URL",
        auth=("api", "YOUR_API_KEYS"),
        data={"from": "PS5_Monitor <"FROM_MAIL_GUN">",
              "to": rec,
              "subject": "PS5 to Buy",
              "text": txt})


