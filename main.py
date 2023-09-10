import requests
import random
from pprint import pprint
from send_mail import send_gmail

API_KEY = 'da0e6e21135e4b11b4eec62705093df8'
url = "https://newsapi.org/v2/everything?q=apple&" \
      "from=2023-09-09&to=2023-09-09&sortBy=popularity&" \
      "apiKey=da0e6e21135e4b11b4eec62705093df8"

request = requests.get(url=url)
# Json returns dictionary but text file return plain string which is not helpful.
content = request.json()

# ACCESSING DIFFERENT PART OF ARTICLE.
title = []
author = []
description = []

for article in content["articles"]:
    if article["title"] is not None:
        title.append(article["title"])
    if article["author"] is not None:
        author.append(article["author"])
    description.append(article["description"])

chosen_title = random.choice(title)

index = title.index(chosen_title)
chosen_author = author[index]
chosen_des = description[index]

# the encoding is causing problem only.
chosen_des = chosen_des.encode("utf-8")

message = f"""\
Subject: {chosen_title}

From: {chosen_author}
 
{chosen_des}
"""

send_gmail(message)
print(message)
