import requests
from bs4 import BeautifulSoup

req = requests.get("https://pypi.org")

soup = BeautifulSoup(req.content,"html.perser")

req = soup.title

print(soup.get_text())

