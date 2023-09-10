import requests
import pprint as p

API_KEY = 'da0e6e21135e4b11b4eec62705093df8'
url = "https://newsapi.org/v2/everything?q=apple&" \
      "from=2023-09-09&to=2023-09-09&sortBy=popularity&" \
      "apiKey=da0e6e21135e4b11b4eec62705093df8"

request = requests.get(url=url)
# Json returns dictionary but text file return plain string which is not helpful.
content = request.json()

# ACCESSING DIFFERENT PART OF ARTICLE.
print(len(content["articles"]))
for article in content["articles"]:
      p.pprint(article["author"])
      p.pprint(article["title"])
      p.pprint(article["description"])

