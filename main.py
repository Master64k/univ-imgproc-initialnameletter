from PIL import Image, ImageDraw, ImageFont
import numpy as np

image = Image.new("L", (250,250), "black")

font = ImageFont.truetype("Arial.ttf", 250)

draw = ImageDraw.Draw(image)

draw.text((40, 0), "N", font=font, fill="white")

image.save("img.png")

image = np.zeros((5, 5), dtype=np.uint8)
image[0][0] = 1
image[1][0] = 1
image[2][0] = 1
image[3][0] = 1
image[4][0] = 1

image[1][1] = 1
image[2][2] = 1
image[3][3] = 1

image[0][4] = 1
image[1][4] = 1
image[2][4] = 1
image[3][4] = 1
image[4][4] = 1

print(image)

img = Image.fromarray(image*255)
img.save('my.png')
#img.show()