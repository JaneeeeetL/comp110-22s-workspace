"""A TURTLE drawing program."""

__author__: str = "730401522"

from random import uniform
from turtle import Turtle, colormode, done  # importing a function from library(?)
colormode(255)  # to enable RGB mode
leo: Turtle = Turtle()  # selecting an object(?)


def draw_triangle(leo: Turtle, x: float, y: float) -> None:
    """A function to draw a triangle."""
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    i: int = 0
    while (i < 3):
        leo.forward(300)
        leo.left(120)
        i = i + 1
    

def draw_square(leo: Turtle, x: float, y: float) -> None:
    """A function to draw a square."""
    leo.penup()
    leo.goto(uniform(x, y), uniform(x, y))
    leo.pendown()
    i: int = 0 
    while (i < 4):
        leo.forward(300)
        leo.left(90)
        i = i + 1
    

def draw_hexagon(leo: Turtle, x: float, y: float) -> None:
    """A function to draw a hexagon."""
    leo.penup()
    leo.goto(uniform(x, y), uniform(x, y))
    leo.pendown()
    i: int = 0
    while (i < 6):
        leo.forward(100)
        leo.left(60)
        i += 1
    

def draw_octagon(leo: Turtle, x: float, y: float) -> None:
    """A function to draw a octagon."""
    leo.penup()
    leo.goto(uniform(x, y), uniform(x, y))
    leo.pendown()
    i: int = 0
    while (i < 8):
        leo.forward(200)
        leo.left(45)
        i += 1


def main() -> None:
    """A function to draw specific patterns."""
    i: int = 0
    while (i < 3):
        x: float = uniform(-300, 300)
        y: float = uniform(-300, 300)
        draw_triangle(leo, x, y)
        leo.color("green", "yellow")
        leo.begin_fill()
        draw_square(leo, x, y)
        leo.end_fill()
        draw_hexagon(leo, x, y)
        draw_octagon(leo, x, y)
        leo.stamp()
        i += 1
    done()


if __name__ == "__main__":
    main()