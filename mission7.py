from PIL import Image
image1=Image.open('oxygen.png','r')
print image1.size
w,h=image1.size
print image1.getpixel((0,h//2))



print ''.join([chr(image1.getpixel((i,h//2))[0]) for i in range(0,w,7)])

print ''.join(map(chr,[105, 110, 116, 101, 103, 114, 105, 116, 121]))