from PIL import Image


img = Image.open('./images/dog.jpg')
img.show()

for x in range(img.width):
    for y in range(img.height):
        clr = img.getpixel((x,y))
        img.putpixel((x,y), 255-clr)

img.show()

