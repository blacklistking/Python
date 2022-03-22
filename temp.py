from bs4 import BeautifulSoup 
import requests
import pandas as pd
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_greenhouse_gas_emissions'
import urllib.request as urlrq
import certifi
import ssl
import urllib
from lxml import html

payload = {
	"username": "30018344", 
	"password": "Berlin@feb21", 
	"__VIEWSTATE": ""
}
session_requests = requests.session()
login_url = "https://solarspc.adani.com/"
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
result = session_requests.post(
	login_url, 
	data = payload, 
	headers = dict(referer=login_url)
)

print(tree.text_content())

url = 'https://solarspc.adani.com/MyTaskSearch/SearchDiffusionInput.aspx'
result = session_requests.get(
	url, 
	headers = dict(referer = url)
)

tree = html.fromstring(result.content)
