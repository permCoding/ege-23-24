from PIL import Image


img = Image.new("RGB", (400, 200), (0, 200, 0))

for y in range(0, img.height):
    img.putpixel((25,y), (255, 255, 255))

img.save('./images/line.bmp', bitmap_format='bmp')
