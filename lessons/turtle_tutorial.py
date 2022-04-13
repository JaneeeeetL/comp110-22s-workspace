from turtle import Turtle, colormode, done  # importing a function from library(?)
colormode(255)  # to enable RGB mode
leo: Turtle = Turtle()  # selecting an object(?)
# leo.forward(50)
# leo.left(30)
# leo.right(40)
# done()
i: int = 0  # to draw a square (ln 8-12)
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1

leo.penup()  # lifting the pen out of the page
leo.goto(45, 60)  # moving the tip of the pen to a certain location
leo.pendown()  # putting the pen down
leo.color("blue")  # changing the color of the pen
leo.color(99, 204, 250)
leo.begin_fill()
i: int = 0

# code for shape to be filled 
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1


leo.end_fill()
done()