from PIL import Image

def main():

    topleft = Image.open("moon.jpg")
    
    width, height = topleft.size

    left = 0
    top = 0
    right = width/2
    bottom = height/2

    topleftcrop = topleft.crop((left, top,right,bottom))
    newsize = (300,300)
    topleftcrop = topleftcrop.resize(newsize)

    #########################################

    topright = Image.open("moon.jpg")
    
    width, height = topright.size

    left = width/2
    top = 0
    right = width
    bottom = height/2

    toprightcrop = topleft.crop((left, top,right,bottom))
    newsize = (300,300)
    toprightcrop = toprightcrop.resize(newsize)

    ##########################################

    bottomright = Image.open("moon.jpg")
    
    width, height = bottomright.size

    left = width/2
    top = height/2
    right = width
    bottom = height

    bottomrightcrop = bottomright.crop((left, top,right,bottom))
    newsize = (300,300)
    bottomrightcrop = bottomrightcrop.resize(newsize)


    #############################################

    bottomleft = Image.open("moon.jpg")
    
    width, height = bottomleft.size

    left = 0
    top = height/2
    right = width/2
    bottom = height

    bottomleftcrop = bottomleft.crop((left, top,right,bottom))
    newsize = (300,300)
    bottomleftcrop = bottomleftcrop.resize(newsize)

    ###############################################

    tophalf = Image.new("RGB", (600,300), "white")
    tophalf.paste(topleftcrop, (0,0))
    tophalf.paste(bottomleftcrop, (300,0))

    bottomhalf = Image.new("RGB", (600,300), "white")
    bottomhalf.paste(bottomrightcrop, (0,0))
    bottomhalf.paste(toprightcrop, (300,0))

    full = Image.new("RGB", (600,600), "white")
    full.paste(tophalf, (0,0))
    full.paste(bottomhalf, (0,300))

    full.show()


main()