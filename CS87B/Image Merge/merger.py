from PIL import Image

def main():

    i1 = 'N_2_B.jpg'
    i2 = 'N_4_B.jpg'
    left = Image.open(i1)
    right = Image.open(i2)
    size = (1920,1080)
    new_image = Image.new('RGB',(2*size[0], size[1]), (250,250,250))
    new_image.paste(left,(0,0))
    new_image.paste(right,(size[0],0))
    new_image.save('test_2.jpg')
    new_image.show()

main()