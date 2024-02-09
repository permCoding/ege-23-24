from PIL import Image


img = Image.open('./images/ждун.jpeg')

print(img.size)

img = img.rotate(-45, expand=True, fillcolor='white')

img.show()
