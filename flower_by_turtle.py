import turtle
ted = turtle.Turtle()

def draw_center():
	ted.pensize(2)
	ted.color("yellow")
	for angle in range(0,360,30):
		ted.seth(angle)
		ted.circle(20)

def draw_petal1():
	ted.color("red")
	ted.pensize(2)
	for angle in range(0,360,15):
		ted.seth(angle)
		ted.fd(100)
		ted.left(120)
		ted.fd(100)
		ted.left(120)
		ted.fd(100)


def drawing_flower():
	window = turtle.Screen()
	window.bgcolor("white")
	ted.speed(10)
	draw_center()
	draw_petal1()

	window.exitonclick()

drawing_flower()


