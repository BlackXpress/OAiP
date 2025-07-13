import turtle
t = turtle.Turtle()
t.color('green', 'red')
t.pensize(5)
t.speed(10)

povtor = 6
ugol = 6
def fig(n):
    for i in range(n):
        t.forward(200)
        t.right(360/n)
for i in range(povtor):
    fig(ugol)
    t.right(360/povtor)

turtle.done()