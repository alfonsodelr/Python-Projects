from PIL import Image, ImageFilter

def merge(image1,image2):
    image1 = image1.resize((426,240))
    image2 = image2.resize((426,240))
    image1_size = image1.size
    image2_size = image2.size
    merged = Image.new("RGB", (2*image1_size[0], image1_size[1]), (250,250,250))
    merged.paste(image1, (0,0))
    merged.paste(image2, (image1_size[0],0))
    merged.show()


def main():
    image = Image.open("elephant.jpg")
    image = image.rotate(90, Image.NEAREST, expand = 1)
    image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
    r,g,b = image.split()
    image = Image.merge("RGB", (b,g,r))
    image.show()
    image2 = Image.open("elephant.jpg")
    image2 = image2.filter(ImageFilter.BoxBlur(5))
    merge(image, image2)
    #image.save("filename.jpg")

main()