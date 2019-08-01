import turtle
import math

def draw_square(name):
	for e in range(1,37):
		for i in range(1,5):
			name.forward(50)
			name.right(90)
		name.right(10)
	name.setheading(0)
	name.right(90)
	name.forward(150)

def draw_circle(name):
	name.circle(100)

def draw_triangle(name):
	name.forward(100)
	name.right(90)
	name.fd(100)
	name.right(135)
	name.fd(math.sqrt(20000))
	name.right(145)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("white")
	'''
	# Square
	brad = turtle.Turtle()
	brad.shape("arrow")
	brad.color("blue")
	brad.speed(11)
	draw_square(brad)
	# Circle
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("yellow")
	angie.speed(10)
	draw_circle(angie)
	'''
	# Triangle
	walter = turtle.Turtle()
	walter.shape("arrow")
	walter.color("red")
	walter.speed(11)
	for e in range(1,19):
		draw_triangle(walter)
		walter.right(10)
	# Close
	window.exitonclick()

draw_art()