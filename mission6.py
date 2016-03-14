import sys
#zip
import zipfile
import re
# what's comment? thus this method is not ok
# import os
# path1=os.path.abspath('.')+"\channel\\"
# init=str(90052);
# while 1:
#     file1=file(path1+init+".txt").read()
#     print file1
#     init=file1.split(' ')[-1]
value=90052
comments=[]
z =zipfile.ZipFile("channel.zip")
while True:
    try:
        content=z.read('%s.txt'%value)
        print z.getinfo('%s.txt'%value).comment
        comments.append(z.getinfo('%s.txt'%value).comment)
        value=content.split(' ')[-1]
        print content
    except Exception,e:
        print e
        break
print ''.join(comments)
