
from urllib import FancyURLopener
import os
import webbrowser

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'

myopener = MyOpener()
page = myopener.open('http://www.google.com/search?q=python')
html=page.read()

f=open(os.path.join('src','mygoogle2.html'),'w')
f.write(html)
f.close()

mygoogle2='file://'+ os.path.join(os.getcwd(), 'src','mygoogle2.html')
print mygoogle2

webbrowser.open(mygoogle2)