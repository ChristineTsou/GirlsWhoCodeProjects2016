from turtle import *
def draw_square(length):
	pendown()
	for i in range(4):
		forward(length)
		right(90)
		
def draw_triangle(length):
	pendown()
	for i in range(3):
		forward(length)
		right(120)

draw_square(50)
penup()
goto(50,50)
pendown()
draw_triangle(50)