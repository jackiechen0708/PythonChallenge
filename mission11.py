from PIL import Image

# img=Image.open('cave.jpg')
# w,h=img.size
# print w,h
# image1=Image.new(img.mode, (w,h/2))
# image2=Image.new(img.mode, (w,h/2))
# for i in range(h):
#     for j in range(w):
#         if(i%2==0):
#             image1.putpixel((j,i/2),img.getpixel((j,i)))
#         else:
#             image2.putpixel((j,i/2),img.getpixel((j,i)))
#
#
#
#
#
# image1.show()
# image2.show()
#finally chessboard net pic
im=Image.open("cave.jpg")

width=im.size[0]
height=im.size[1]

even=Image.new(im.mode, (width/2,height/2))
odd=Image.new(im.mode, tuple([x/2 for x in im.size]))

for x in range(width):
    for y in range(height):
        pixel=im.getpixel((x,y))
        if x%2^y%2:
            print x,y
            odd.putpixel(((x-1)/2, y/2) if x%2 else (x/2, (y-1)/2) , pixel)
        else:
            even.putpixel((x/2, y/2), pixel)
even.save('cave_even.jpg')
odd.save('cave_odd.jpg')