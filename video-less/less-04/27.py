from PIL import Image


img = Image.open('./images/белка.jpg')
img.show()

for x in range(img.width):
    for y in range(img.height):
        r, g, b = img.getpixel((x,y))
        img.putpixel((x,y), (255-r, g, 255-b))

img.show()

