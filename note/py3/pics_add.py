from PIL import Image,ImageFont,ImageDraw

im = Image.open('tu1.jpg')
width = im.size[0]
height = im.size[1]
print(width,height)
read = input('Enter to continue')

draw = ImageDraw.Draw(im)

newfont = ImageFont.truetype('ttf/simkai.ttf',40)
draw.text((width*0.8,height*0.9),'Good',(255,255,0),font=newfont)
im.show()
im.save('tu2.jpg')
