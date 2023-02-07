import turtle


window = turtle.Screen()
window.setup(height=400, width=500)
window.bgcolor("white")
window.tracer(0)
window.title("Snake")

snake = turtle.Turtle()
snake.color("black")
snake.shape("square")
snake.penup()
snake.goto(0,0)
snake.speed()

def snake_up():
    y = snake.ycor()
    y+=20
    snake.sety(y)

def snake_left():
    x = snake.xcor()
    x-=20
    snake.setx(x)

def snake_down():
    y = snake.ycor()
    y-=20
    snake.sety(y)

def snake_right():
    x = snake.xcor()
    x+=20
    snake.setx(x)


window.listen()
window.onkeypress(snake_down, "s")
window.onkeypress(snake_up, "w")
window.onkeypress(snake_left, "a")
window.onkeypress(snake_right, "d")


while True:
    window.update()

    
    