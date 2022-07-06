import urllib.request
#import urllib.erro
import urllib.parse
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
lst = list()
tags = soup('span')
for tag in tags:
    Contents = tag.contents[0]
    c = int(Contents)
    lst.append(c)
print(sum(lst))