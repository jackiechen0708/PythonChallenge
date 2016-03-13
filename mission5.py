import pickle
p=pickle.load(file('mission5data'))
#print p[i][j][0]*p[i][j][1]
for item in p:
    print item
    print map(lambda p: p[0]*p[1], item)




