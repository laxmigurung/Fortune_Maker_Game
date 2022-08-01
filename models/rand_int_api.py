from urllib import response
import requests

url = "https://www.random.org/integers/"
response = requests.get(url)
print(response.status_code)