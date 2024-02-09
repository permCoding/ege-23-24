from PIL import Image


img = Image.new('RGB', (300, 300), (255,255,255))

r,g,b = 0,0,0
for x in range(img.width):
    for y in range(img.height):
        g = x; b = y
        img.putpixel((x,y), (r,g,b))

img.show()

