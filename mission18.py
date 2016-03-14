# from PIL import Image
# image=Image.open('balloons.jpg')
# w,h=image.size
# print w,h
# image1=image.crop([0, 0 ,w/2,h ])
# image2=image.crop([w/2, 0 ,w,h ])
# image3=Image.new(image1.mode,image1.size)
# def tupleMinus(tuple1,tuple2):
#     return (tuple1[0]-tuple2[0],
#             tuple1[1]-tuple2[1],
#             tuple1[2]-tuple2[2])
#
#
# for i in range (image1.size[0]):
#     for j in range (image1.size[1]):
#         image3.putpixel((i,j),tupleMinus(image1.getpixel((i,j)),image2.getpixel((i,j))))
# image3.show()

import  difflib
file1=file('delta.txt')
d1, d2 = [], []
for line in file1.readlines():
    d1.append(line[:53]+'\n')
    d2.append(line[56:])

img1 = file('mission18_1.png','wb')
img2 = file('mission18_2.png','wb')
img3 = file('mission18_3.png','wb')
diff = difflib.ndiff(d1,d2)
for line in diff:
    print line
    bytes = [chr(int(i,16)) for i in line[2:].split()]
    if line.startswith('-'):
        img1.write(''.join(bytes))
    elif line.startswith('+'):
        img2.write(''.join(bytes))
    elif line.startswith(' '):
        img3.write(''.join(bytes))
img1.close()
img2.close()
img3.close()