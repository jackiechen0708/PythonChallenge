class Student(object):

    def __init__(self,name):
        self.name=name

    def __init__(self, name, score):
        self.name = name
        self.score = score

def myNew(name,score=0):
    s=Student(name,score)
    return s

s1=myNew("zhangsan")
print s1
s2=myNew("lisi",98)
print s2
