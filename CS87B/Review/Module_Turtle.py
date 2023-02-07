import turtle


def main():
    screen = turtle.Turtle()
    turtle.speed(1)
    turtle.title("Review")
    turtle.bgcolor("blue")
    screen.color("black", "red")
    screen.begin_fill()
    screen.pensize(20)
    screen.goto(100,100)
    screen.right(90)
    screen.forward(100)
    screen.home()
    screen.goto(-100,100)
    screen.right(90)
    screen.forward(100)
    screen.home()
    screen.circle(100)
    screen.end_fill()
    screen.clear()
    var = input()

    #screen.penup() screen.pendown()

    
main()

