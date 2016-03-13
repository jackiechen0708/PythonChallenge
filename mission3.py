from itertools import permutations
import re
file1=file('mission3data')
content=file1.readlines()
#misunderstand questions! I thought 3 sides have big letters
# def upperCount(myString,i,j):
#     print str(i)+","+str(j)+"\n";
#     sum=0;
#     if((i-1)>=0):
#         if(myString[i-1][j].isupper()):
#             sum=sum+1
#     if((i+1)<len(myString)):
#         if(myString[i+1][j].isupper()):
#             sum=sum+1
#     if((j-1)>=0):
#         if(myString[i][j-1].isupper()):
#             sum=sum+1
#     if((j+1)<len(myString[i])-1):
#         if(myString[i][j+1].isupper()):
#             sum=sum+1
#     return sum
# list=[]
# for i in range(3,len(content)):
#     for j in range(3,len(content[i])):
#         if(upperCount(content,i,j)==3):
#             if(content[i][j].islower()):
#                 list.append(content[i][j])
# print list

#forget 4

# def isRequired(myString,i,j):
#     if(
#         myString[i-3][j].isupper()&
#         myString[i-2][j].isupper()&
#         myString[i-1][j].isupper()&
#         myString[i+1][j].isupper()&
#         myString[i+2][j].isupper()&
#         myString[i+3][j].isupper()
#        ):
#         return True
#     else:
#         return False
# list1=[]
# for i in range(3,1247):
#     for j in range(3,77):
#         if(isRequired(content,i,j)):
#             if(content[i][j].islower()):
#                 list1.append(content[i][j])
# print "".join(list1)
# for i in  list(permutations(list1)):
#     print "".join(i)
#finally regular expression
p=re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',re.S)
for i in range(len(content)):
    if(len(re.findall(p,content[i]))>0):
        print re.findall(p,content[i])











