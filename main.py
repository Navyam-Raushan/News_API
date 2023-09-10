import requests
import random
from pprint import pprint
from send_mail import send_gmail

topic = "amazon"
API_KEY = 'da0e6e21135e4b11b4eec62705093df8'
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-09-09&to=2023-09-09&" \
      "sortBy=popularity&" \
      "apiKey=da0e6e21135e4b11b4eec62705093df8&" \
      "language=en"

request = requests.get(url=url)
# Json returns dictionary but text file return plain string which is not helpful.
content = request.json()

# ACCESSING DIFFERENT PART OF ARTICLE.
body = ""
for article in content["articles"][:10]:
    if article["title"] is not None:
        body = "Subject: Today's News" \
               + "\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
# That's not error but a warning from google as same subject is reapeating with same ip address.
send_gmail(message=body)
