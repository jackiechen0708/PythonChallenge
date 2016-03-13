my=file('mytest.txt').readlines()
others=file('otherstest.txt').readlines()
for i in range(10000):
    if( not my[i]==others[i]):
        print i

