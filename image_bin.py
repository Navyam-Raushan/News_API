import requests

url = "https://wallpaperaccess.com/full/5153571.jpg"
response = requests.get(url)

# It will return binary code of the image let's make the image.
content = response.content

with open("image.jpg", "wb") as img:
    img.write(response.content)
