from PIL import Image


img = Image.open('./images/белка.jpg')
img.show()

down = .8
for x in range(img.width):
    for y in range(img.height):
        r, g, b = img.getpixel((x,y))
        clr = (int(r*down), int(g*down), int(b*down))
        img.putpixel((x,y), clr)

img.show()

