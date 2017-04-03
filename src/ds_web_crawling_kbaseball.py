
import requests
import lxml.etree

def getkb():
    rResponse = requests.get('http://www.kbreport.com/main')
    _html = lxml.etree.HTML(rResponse.text)

    nodes = _html.xpath("//*/div[@class = 'team-rank-box']//table[@class='team-rank']//tr")
    print "number of table cols: ", len(nodes)

    for cnt, teams in enumerate(nodes):
        for cols in teams:
            if cols.xpath(".//a/text()"):
                print cols.xpath('.//a/text()')[0],  #comma for make table form
            else:
                print cols.text.strip(),
        print #add another line
    
def main():
    getkb()
    
if __name__ == "__main__":
    main()