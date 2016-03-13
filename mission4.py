import urllib
url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
# initNum=str(12345)
initNum=str(6050)
# while 1:
#     try:
#         content=urllib.urlopen(url+initNum).read()
#         print content.split(' ')[5]
#         initNum = content.split(' ')[5]
#     finally:
#         print "over"
while 1:
     content=urllib.urlopen(url+initNum).read()
     print content
     print content.split(' ')[5]
     initNum = content.split(' ')[5]
