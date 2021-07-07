import requests

def send_mail(rec, txt):
    return requests.post(
        "https://api.mailgun.net/v3/mail.jjjziso.net/messages",
        auth=("api", "4f48cac49ffe61bcad7ba98edefa7748-074fa10c-dae505fa"),
        data={"from": "PS5_Monitor <mailgun@mail.jjjziso.net>",
              "to": rec,
              "subject": "PS5 to Buy",
              "text": txt})


