from PIL import Image


img1 = Image.open('./mini/белка.png')
img2 = Image.open('./mini/color.png')

img = Image.blend(img1, img2, .20)

img.show()
