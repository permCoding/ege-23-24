from PIL import Image

clr = (0, 200, 0)
img = Image.new("RGB", (400, 200), clr)

print(img.size, img.width, img.height, img.mode)

for y in range(0, img.height):
    img.putpixel((25,y), (255, 255, 255))

img.show()
