import re

result='1'
#this regular using well & this lambda using very well!!!
#6666666666
pattern=re.compile(r'((?P<w>\d)(?P=w)*)')

for i in range(30):
    a=map(lambda x:'%s%s'%(len(x[0]),x[1]),pattern.findall(result))

    result=''.join(a)
    print result

print len(result)