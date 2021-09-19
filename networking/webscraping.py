# Webscraping via BeautifulSoup https://pypi.python.org/pypi/beautifulsoup4
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter url: ') # be sure to include http://
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags from given url
tags = soup('a')
for tag in tags:
    print(tag.get('href', None)) # Give me the values of the href



