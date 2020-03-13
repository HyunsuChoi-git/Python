import turtle as t

def spiral(length):
    if length <= 5:
        return
    t.forward(length)
    t.right(90)
    spiral(length-5)


t.speed(100)
t.goto(-100, 100)
t.hideturtle()
spiral(300)
t.done()
# t.exitonclick()
