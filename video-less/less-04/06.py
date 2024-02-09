from PIL import Image, ImageDraw


img = Image.new("RGB", (400, 200), (0, 200, 0))
drw = ImageDraw.Draw(img)

crd_line = (0,0,img.width-1,img.height-1)

drw.line(crd_line, (255,255,0), width=5)

img.show()
