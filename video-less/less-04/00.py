from PIL import Image

# img = Image.new("RGB", (400, 200), 'yellow')
img = Image.new("RGB", (400, 200), (200, 200, 0))

print(img)

img.show()
