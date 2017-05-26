import turtle
ted = turtle.Turtle()

def draw_center():
	ted.pensize(2)
	ted.color("yellow")
	for angle in range(0,360,30):
		ted.seth(angle)
		ted.circle(20)


def drawing_flower():
	window = turtle.Screen()
	window.bgcolor("white")
	ted.speed(10)
	draw_center()

	window.exitonclick()

drawing_flower()


