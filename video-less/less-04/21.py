from PIL import Image


img1 = Image.open('./images/color.jpg')
img2 = Image.open('./images/белка.jpg')

print(img1.size, img2.size)

full_w = img1.width + img2.width
full_h = max(img1.height, img2.height)

img = Image.new('RGB', (full_w, full_h), (255,255,255))

img.paste(img1)
img.paste(img2, (img1.width ,0))

img.show()
