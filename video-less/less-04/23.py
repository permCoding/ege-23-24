from PIL import Image, ImageFilter


Image.open('./images/белка.jpg').filter(ImageFilter.BoxBlur(5)).show()
