
import requests
import lxml.html
from lxml.cssselect import CSSSelector

def getkb():
    rResponse = requests.get('http://www.kbreport.com/main')
    _html = lxml.html.fromstring(rResponse.text)

    sel = CSSSelector("div.team-rank-box table.team-rank tr")
    nodes = sel(_html)
    print "number of table cols: ", len(nodes)

    for cnt, teams in enumerate(nodes):
        for cols in teams:
            if cols.cssselect("td > a"):
                print cols.text,  #comma for make table form
            else:
                print cols.text.strip(),
        print #add another line
    
def main():
    getkb()
    
if __name__ == "__main__":
    main()