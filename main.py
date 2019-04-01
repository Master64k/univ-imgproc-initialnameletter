from PIL import Image, ImageDraw, ImageFont

image = Image.new("L", (250,250), "black")

font = ImageFont.truetype("Arial.ttf", 250)

draw = ImageDraw.Draw(image)

draw.text((40, 0), "N", font=font, fill="white")

image.save("img.png")
