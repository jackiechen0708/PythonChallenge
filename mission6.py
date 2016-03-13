import sys
#zip
import zipfile
import re
# what's comment? thus this method is not ok
# import os
# path1=os.path.abspath('.')+"\mission6\\"
# init=str(90052);
# while 1:
#     file1=file(path1+init+".txt").read()
#     print file1
#     init=file1.split(' ')[3]
value=90052
findNothing = re.compile(r'(?<=Next nothing is )\d+').search
comments=[]
z =zipfile.ZipFile("channel.zip")
while True:
    content=z.read('%s.txt'%value)
    print z.getinfo('%s.txt'%value).comment
    comments.append(z.getinfo('%s.txt'%value).comment)
    match=findNothing(content)
#    match=apply(findNothing,(content,))
    if match:
        value=match.group(0)
    else:
        break
    print content

print z.read('%s.txt'%value)

print ''.join(comments)
