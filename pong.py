import turtle
import time

#screen
s = turtle.Screen()
s.setup(800,600)
s.title("pong")
s.bgcolor("black")
s.tracer(0)

#ball
b = turtle.Turtle()
b.penup()
b.shape("square")
b.color("white")
b.speed(0)
b.x = 0.1
b.y = 0.1

#paddle A
pa = turtle.Turtle()
pa.penup()
pa.goto(-350,0)
pa.shape("square")
pa.color("white")
pa.speed(0)
pa.shapesize(stretch_len=1,stretch_wid=5)

#paddle B
pb = turtle.Turtle()
pb.penup()
pb.goto(350,0)
pb.shape("square")
pb.color("white")
pb.speed(0)
pb.shapesize(stretch_len=1,stretch_wid=5)



#pen

pen = turtle.Turtle()
pen.penup()
pen.goto(0,270)
pen.color("white")
pen.hideturtle()
pen.write("Player A : 0   Player B : 0",font=('courier',18 , "normal"),align="center")

#score
sa = 0
sb = 0

def a_up():
    y = pa.ycor()
    y += 20
    if y>250:
        y=250
    pa.sety(y)

def a_down():
    y = pa.ycor()
    y -= 20
    if y<-250:
        y=-250
    pa.sety(y)

def b_up():
    y = pb.ycor()
    y += 20
    if y>250:
        y=250
    pb.sety(y)

def b_down():
    y = pb.ycor()
    y -= 20
    if y<-250:
        y=-250
    pb.sety(y)

s.listen()
s.onkeypress(a_up, 'w')
s.onkeypress(a_down, 's')
s.onkeypress(b_up, 'Up')
s.onkeypress(b_down, 'Down')


while True:
    s.update()

    b.setx(b.xcor()+ b.x)
    b.sety(b.ycor()+ b.y)

    #border checks
    if b.ycor()>290:
        b.sety(290)
        b.y *= -1

    if b.ycor()<-290:
        b.sety(-290)
        b.y *= -1

    if b.xcor()>390:
        b.goto(0,0)
        b.x *= -1
        sa += 1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(sa,sb),font=('courier',18 , "normal"),align="center")

    if b.xcor()<-390:
        b.goto(0,0)
        b.x *= -1
        sb += 1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(sa, sb),font=('courier',18 , "normal"),align="center")


    #collision
    if b.xcor()>340 and b.xcor()<350 and b.ycor()<(pb.ycor()+50) and b.ycor()>(pb.ycor()-50):
        b.setx(340)
        b.x *= -1

    if b.xcor()<-340 and b.xcor()>-350 and b.ycor()<(pa.ycor()+50) and b.ycor()>(pa.ycor()-50):
        b.setx(-340)
        b.x *= -1

    #result
    if sa==5:
        s.clear();
        pen = turtle.Turtle()
        pen.penup()
        pen.goto(-190,-10)
        pen.color("black")
        pen.hideturtle()
        pen.write("Congratulations!!! Player A won",font=("Calibri", 20, "bold"))
        time.sleep(5)
        break

    if sb == 5:
        s.clear();
        pen = turtle.Turtle()
        pen.penup()
        pen.goto(-190, -10)
        pen.color("black")
        pen.hideturtle()
        pen.write("Congratulations!!! Player B won", font=("Calibri", 20, "bold"))
        time.sleep(5)
        break

