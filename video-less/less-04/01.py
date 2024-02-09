from PIL import Image

clr = (0, 200, 0)
img = Image.new("RGB", (400, 200), clr)

point = (0,0)
color = img.getpixel(point)

print(color)

# img.putpixel()

img.show()
