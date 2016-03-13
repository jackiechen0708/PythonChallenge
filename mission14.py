# <!-- remember: 100*100 = (100+99+99+98) + (...  -->
# above means clockwise
#????????????????????????????????????????????????????????????????????????
from PIL import Image
img=Image.open('wire.png')
def spiral(source):
    mImage=Image.new(source.mode,(100,100))
    w=0
    h=0
    upboder=0
    downboder=100
    leftboder=0
    rightboder=100
    count=0
    for i in xrange(10000):



        if(h==upboder and w< rightboder ):#up
            print w,h
            mImage.putpixel((w,h),source.getpixel((i,0)))
            count=count+1
            w=w+1
            if(w==rightboder):
                upboder=upboder+1
                h=h+1


        if(w==rightboder and h< downboder ):#right
            print w-1,h
            mImage.putpixel((w-1,h),source.getpixel((i,0)))
            count=count+1
            h=h+1
            if(h==downboder):
                rightboder=rightboder-1
                w=w-1

        if(h==downboder and w> leftboder ):#down
            print w-1,h-1
            mImage.putpixel((w-1,h-1),source.getpixel((i,0)))
            count=count+1
            w=w-1
            if(w==leftboder):
                downboder=downboder-1
                h=h+1

        if(w==leftboder and h> upboder+2 ):#left
            print w,h-3
            mImage.putpixel((w,h-3),source.getpixel((i,0)))
            count=count+1
            h=h-1
            if(h==upboder+2):
                leftboder=leftboder+1
                w=w+1
                h=h-2
    return mImage
spiral(img).show()


# def spiral(source):
#      target = Image.new(source.mode, (100, 100))
#      left, top, right, bottom = (0, 0, 99, 99)
#      x, y = 0, 0
#      dirx, diry = 1, 0
#      for i in xrange(10000):
#          print x,y
#          target.putpixel((x, y), source.getpixel((i, 0)))
#          if dirx == 1 and x == right:
#              dirx, diry = 0, 1
#              top += 1
#          elif dirx == -1 and x == left:
#              dirx, diry = 0, -1
#              bottom -= 1
#          elif diry == 1 and y == bottom:
#              dirx, diry = -1, 0
#              right -= 1
#          elif diry == -1 and y == top:
#              dirx, diry = 1, 0
#              left += 1
#          x += dirx
#          y += diry
#      return target
#
# spiral(img).show()






