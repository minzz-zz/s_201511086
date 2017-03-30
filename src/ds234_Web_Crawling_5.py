
import lxml.html
from lxml.cssselect import CSSSelector
import requests

rResponse = requests.get("http://www.ieee.org/conferences_events/conferences/search/index.html")
_html = lxml.html.fromstring(rResponse.text)

sel = CSSSelector("#inner-container > div.content-gray > div.box-lr-top > div.content-r-full > div > table > tbody > tr > td > p > a[href]")
nodes = sel(_html)
print len(nodes)

for cnt, node in enumerate(nodes):
    print cnt, node.text #node.text mean get text between <a> </a> tag