import turtle
import math

def my_name():
	# Background color
	background = turtle.Screen()
	background.bgcolor("white")
	# How the turtle look like
	gabriel = turtle.Turtle()
	gabriel.shape("classic")
	gabriel.speed(1)
	# Just calling the function
	draw_my_name(gabriel)
	# Close
	background.exitonclick()

def draw_my_name(name):
	name.goto(50.0,0.0)
	name.right(90)
	name.speed(11)
	name.circle(-100/2,270)


my_name()