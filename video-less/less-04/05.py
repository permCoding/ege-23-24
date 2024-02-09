from PIL import Image


def put_line(x=0):
    gr = 255
    for y in range(img.height):
        if x >= img.width: break
        img.putpixel((x,y), (gr, gr, gr))
        x += 1
        gr -= 1


img = Image.new("RGB", (400, 200), (0, 200, 0))

for x in range(0, img.width, 2):
    put_line(x)

img.save('./images/line.bmp', bitmap_format='bmp')
