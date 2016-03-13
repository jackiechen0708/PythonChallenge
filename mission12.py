# from PIL import Image
# img=Image.open('evil1.jpg')
# print img.size
# w,h=img.size
# image1=Image.new(img.mode,(w,h))
# image2=Image.new(img.mode,(w,h))
# image3=Image.new(img.mode,(w,h))
# for i in range(h):
#     for j in range(w):
#         pix=img.getpixel((j,i))
#         if(i%3==0):
#             image1.putpixel((j,i/3),pix)
#         elif(i%3==1):
#             image2.putpixel((j,i/3),pix)
#         else:
#             image3.putpixel((j,i/3),pix)
#
#
# image1.show()
# image2.show()
# image3.show()

#naive aha
#binary read
file1=file('evil2.gfx','rb')
content=file1.read()
[open("evil_%d.jpg" %i, "wb").write(content[i::5]) for i in range(5)]
# for i in range(5):
#         file = open('evil_%d.jpg' % i, 'wb')
#         file.write(content[i::5])
#         file.close()



