from PIL import Image


img = Image.new('RGB', (300, 300), (255,255,255))

clr = (0,0,0)
for x in range(img.width):
    for y in range(img.height):
        img.putpixel((x,y), clr)

img.show()

