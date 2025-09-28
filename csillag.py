import turtle
# import math

SIDE_LENGHT = 250
TURN_ANGLE = 144
BG_COLOR = 'blue'
LINE_COLOR = 'red'
#FILL_COLOR = 'YELLOW'


def csillag():
    turtle.pensize(5)
    turtle.pencolor(LINE_COLOR)
    turtle.speed(3)

    turtle.penup()
    y_start = SIDE_LENGHT / 6
    turtle.goto(-SIDE_LENGHT / 2, y_start)
    turtle.pendown()

    turtle.fillcolor(BG_COLOR)
    turtle.begin_fill()

    for _ in range(5):
        turtle.forward(SIDE_LENGHT)
        turtle.right(TURN_ANGLE)

    turtle.end_fill()
    turtle.hideturtle()

def start_drawing():
    turtle.clear()
    turtle.bgcolor(BG_COLOR)
    csillag()

ablak =turtle.Screen()
ablak.setup(width=700, height=700)
ablak.title('Csillag Rajzoló ')

turtle.listen()

turtle.onkey(start_drawing, 'h')

turtle.onkey(turtle.bye, 'q')

turtle.mainloop()





