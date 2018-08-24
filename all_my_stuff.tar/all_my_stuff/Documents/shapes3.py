from turtle import *
def regular_polygon(sides, length, color):
	for i in range(sides):
		pencolor(color)
		pendown()
		forward(length)
		right(360/sides)
penup()
goto(20,0)
regular_polygon(4,50,"red")
penup()
goto(80,0)
regular_polygon(4,50,"blue")
penup()
goto(140,0)
regular_polygon(4,50,"green")


