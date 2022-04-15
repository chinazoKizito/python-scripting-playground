# web scrapping/html parsing using BeautifulSoup to return only the links
import ssl
import urllib.request

from bs4 import BeautifulSoup

# Ignore SSl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all the anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
