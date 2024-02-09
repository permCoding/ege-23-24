from PIL import Image, ImageDraw


img = Image.new("RGB", (400, 200), (0, 55, 127))
drw = ImageDraw.Draw(img)

crd = (0,0,img.width-1,img.height-1)

drw.ellipse(crd, fill=(200,200,150), outline='red', width=3)

# drw.point((100,100), fill=(0,0,0))
# points = [(10,10), (11,11), (12,12)]
points = [10,10, 11,11, 12,12, 13,13]
drw.point(points)

img.show()
