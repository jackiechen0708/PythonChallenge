#make replace using rules given by the picture
#using string's translate function
#first make translate table using string.maketrans(from,to)

import string
s="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
table=string.maketrans("koe","mqg")
print s.translate(table)
print "map".translate(table)
table=string.maketrans("abcdefghijklmnopqrstuvwxyz",'cdefghijklmnopqrstuvwxyzab')