#Alfonso Del Rosario
#10/10/2021
#Assignment 3

#this program changes the colors of the top half of the image to shades of red similar
#to the shades of gray that it's replacing
#it does the same to the bottom half, but with the color blue instead.
#the original image is also changed from 612x612 to 300x300 in size

from PIL import Image

def main():
    img = Image.open("moon.jpg")
    img = img.convert("RGBA")

    pixdata = img.load()

    for x in range(img.width):
        for y in range(int(img.height/2)):
            r , g , b, d = img.getpixel((x,y))
            if (r > 230 and g > 230 and b > 230):
                pixdata[x, y] = (230, 0, 0, 230)
            elif (r > 200 and g > 200 and b > 200):
                pixdata[x, y] = (200, 0, 0, 200)
            elif (r > 170 and g > 170 and b > 170):
                pixdata[x, y] = (170, 0, 0, 170)
            elif (r > 140 and g > 140 and b > 140):
                pixdata[x, y] = (140, 0, 0, 140)
            elif (r > 80 and g > 80 and b > 80):
                pixdata[x, y] = (80, 0, 0, 80)
            elif (r > 30 and g > 30 and b > 30):
                pixdata[x, y] = (30, 0, 0, 180)
            else:
                pixdata[x, y] = (0, 0, 0, 180)

    for x in range(img.width):
        for y in range(img.height):
            r , g , b, a = img.getpixel((x,y))
            if (r > 230 and g > 230 and b > 230 and a > 230):
                pixdata[x, y] = (0, 0, 230, 230)
            elif (r > 200 and g > 200 and b > 200 and a > 200):
                pixdata[x, y] = (0, 0, 200, 200)
            elif (r > 170 and g > 170 and b > 170 and a > 170):
                pixdata[x, y] = (0, 0, 170, 170)
            elif (r > 140 and g > 140 and b > 140 and a > 140):
                pixdata[x, y] = (0, 0, 140, 140)
            elif (r > 80 and g > 80 and b > 80 and a > 80):
                pixdata[x, y] = (0, 0, 80, 80)
            elif (r > 30 and g > 30 and b > 30 and a > 30):
                pixdata[x, y] = (0, 0, 30, 180)
            
                
    size = (300,300)
    img = img.resize(size)
    img.show()

main()