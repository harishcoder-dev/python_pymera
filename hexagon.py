import turtle
t = turtle.Pen()
turtle.bgcolor("black")
sides = 6
colors = ["red","green","blue","yellow","orange","maroon"]
for x in range(360):
	t.pencolor(colors[x%sides])
	t.forward(x * 3/sides + x)
	t.left(360/sides + 1)
	t.width(x*sides/200)