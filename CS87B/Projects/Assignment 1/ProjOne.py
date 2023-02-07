#Name: Alfonso Del Rosario
#Project 1
#Submission Date: 09/26/2021

import turtle

def draw_petals(pencil, numOfSquares, length, angle_between_squares):
    
    pencil.color('black', 'yellow')
    pencil.begin_fill()
    pencil.left(90)

    for i in range(numOfSquares):
        pencil.forward(length)
        pencil.right(90)
        pencil.forward(length)
        pencil.right(90)
        pencil.forward(length)
        pencil.left(angle_between_squares) # 108 is 180 - (360/n) 

    pencil.right(90)
    pencil.end_fill()

def draw_center(pencil, numOfSquares, length, angle):
    pencil.color('orange', 'blue')
    pencil.begin_fill()

    for i in range(numOfSquares):
        pencil.forward(length)
        pencil.right(angle)

    pencil.end_fill()

def drawFlower(numOfSquares):
    pencil = turtle.Turtle()
    pencil.speed(2)
    angle = 360/numOfSquares
    length = 50
    angle_between_squares = 180 - (angle)
    
    draw_petals(pencil, numOfSquares, 50, angle_between_squares)
    draw_center(pencil, numOfSquares, length, angle)


def main():
    numOfSquares = int(input("How Many Squares Would You Like?\n"))
    drawFlower(numOfSquares)
    pause = int(input(""))

main()