import requests
import pprint as p

API_KEY = 'da0e6e21135e4b11b4eec62705093df8'
url = "https://newsapi.org/v2/everything?q=apple&" \
      "from=2023-09-09&to=2023-09-09&sortBy=popularity&" \
      "apiKey=da0e6e21135e4b11b4eec62705093df8"

request = requests.get(url=url)
content = request.text
p.pprint(content)