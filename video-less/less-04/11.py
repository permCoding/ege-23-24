from PIL import Image


# img = Image.open('./images/белка.jpg')
# img.show()

# with open('./11.py') as file:
#     print(file.read())

with Image.open('./images/белка.jpg') as img:
    img.show()
