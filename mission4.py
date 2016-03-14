import urllib
url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
count=273
# initNum=str(12345)
initNum=str(66831)
while 1:
     count+=1
     content=urllib.urlopen(url+initNum).read()
     print count
     print content
     initNum = content.split(' ')[5]


