from PIL import Image


img = Image.open('./images/белка.jpg')

print(img.size)

rect = (120, 120, 240, 240)

img = img.crop(rect)

img.show()
img.save('./images/crop.jpg')
img.save('./images/crop.bmp', bitmap_format='bmp')
