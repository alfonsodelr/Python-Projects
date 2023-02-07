import turtle

def drawFlower(numOfSquares):
    turt = turtle.Turtle()

    turt.speed(15)

    turt.color("black", "purple")


    turt.begin_fill()
    for i in range(numOfSquares):
        for k in range(4):
            turt.forward(50)
            turt.left(90)

        turt.forward(50)
        turt.right(360 / numOfSquares)
    turt.end_fill()


def main():
    numOfSquares = int(input("How many Petals would you like? \n"))
    drawFlower(numOfSquares)
    pause = int(input(""))


main()