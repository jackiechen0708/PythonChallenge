import pickle
p=pickle.load(file('mission5data'))
for item in p:
    # print item
    print "".join(map(lambda p: p[0]*p[1], item))




