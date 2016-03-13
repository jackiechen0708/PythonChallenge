#urllib
import urllib
#try to parse using bs4 but failed
from bs4 import BeautifulSoup
#determine to use file
url="http://www.pythonchallenge.com/pc/def/ocr.html"
#function redirect
# urltest=urllib.urlopen(url).read
# print urltest()
file1=file('mission2data')
content=file1.read()
def findRare(string):
    mMap={}
    for i in range(len(string)):
        if string[i] in mMap:
            mMap[string[i]]=mMap[string[i]]+1
        else:
            mMap[string[i]]=1
    return sorted(mMap.iteritems(),key=lambda asd:asd[1])
print findRare(content)
#equality!




