
# coding: utf-8
import lxml.html
import requests
from lxml.cssselect import CSSSelector

keyword='비오는'
response = requests.get("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")
_html = lxml.html.fromstring(response.text)

sel = CSSSelector("#content > div:nth-child(4) > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack > table > tbody > tr")

nodes = sel(_html)

_selName = CSSSelector('.name > a.title')
_selArtist = CSSSelector('._artist.artist')
_selAlbum= CSSSelector('.album > a')
for node in nodes:
    _name=_selName(node)
    _artist=_selArtist(node)
    _album=_selAlbum(node)
    if _name:
        print _artist[0].text_content().strip(),
        print "---",
        print _name[0].text_content(),
        print "---",
        print _album[0].text_content()