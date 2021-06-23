import turtle
t=turtle.Turtle()

t.color('red')
t.pensize(6)
turtle.bgcolor('black')

t.speed(0)
for i in range(220):
	t.forward(1)
	t.left(1)

t.penup()
t.goto(0,0)
t.pendown()

t.left(140)

for i in range(220):
	t.forward(1)
	t.right(1)
	
for i in range(100):
	t.forward(1)
	t.left(1)

t.penup()
t.goto(0,0)
t.pendown()

t.left(125)
t.forward(25)

for i in range(80):
	t.forward(1)
	t.right(1)
for i in range(165):
	t.forward(1)
	t.left(1)

t.forward(80)

for i in range(160):
	t.forward(1)
	t.left(1)
	
for i in range(30):
	t.forward(1)
	t.right(1)
	
t.penup()

t.goto(0,200)
t.left(40)
t.pendown()

for i in range(200):
	t.forward(1)
	t.left(1)

t.penup()	
t.goto(60,180)
t.pendown()

t.circle(5)

turtle.mainloop()
