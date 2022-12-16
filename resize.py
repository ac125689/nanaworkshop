from PIL import Image

image1 = Image.open('image/puja_icons/engagement-rings.jpeg')

print(image1.size)

new_hight  = 219
new_width = int(new_hight / image1.height * image1.width)
print(new_width)

re_im = image1.resize(219,220)

re_im.show()