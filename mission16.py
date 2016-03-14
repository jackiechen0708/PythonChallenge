#?????????????????????????????????????????????????????????????????
from PIL import  Image
# im = Image.open("mozart.gif")
# im.save("0.gif",quality=100)
# while True:
#     try:
#         seq = im.tell()
#         im.seek(seq + 1)
#         im.save("%s.gif" %(seq),quality=100)
#     except EOFError:
#         print "error"
#         break

im = Image.open("mozart.gif")
magic = chr(195)
print im.size
for y in range(im.size[1]):
    box = 0, y, im.size[0], y+1 # box bounding row y
    row = im.crop(box)
    bytes = row.tostring()
    # Rotate 195 to the first column.
    i = bytes.index(magic)
    print i
    bytes = bytes[i:] + bytes[:i]
    row.fromstring(bytes)
    im.paste(row, box)  # overwrite the original row
im.show()