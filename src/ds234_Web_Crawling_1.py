
import requests
import lxml.html
from lxml.cssselect import CSSSelector

rResponse = requests.get("http://python.org/")
_html = lxml.html.fromstring(rResponse.text)
sel = CSSSelector("a[href]")
nodes = sel(_html)

for cnt, node in enumerate(nodes):
    print cnt, node.get('href'), node.text