import turtle 





t = turtle.Turtle()
t.speed(10)
t.hideturtle()
t.pensize(4)
turtle.setup(840,500)

myWin = turtle.Screen()

# 头
t.penup()
t.goto(100,150)
t.pendown()
t.setheading(90)
len = 1   # 设置初始走的速度为1
for k in range(2):
    for j in range(60):
        if j < 30:              # 当j<30，也就是画前一半的弧线
            len += 0.2          # 让速度越走越快
        else:                   # 画后一半弧线
            len -= 0.2          # 让速度越走越慢
        t.forward(len)
        t.left(3)

#眼睛
t.penup()
t.goto(-25,150)

t.begin_fill()
t.circle(8)
t.end_fill()

t.goto(50,150)

t.begin_fill()
t.circle(8)
t.end_fill()

t.goto(45,150)
t.pendown()
t.seth(180)
t.forward(73)

# 腮
t.color("pink")
t.pu()
t.goto(-50,125)

t.pd()
t.begin_fill()
t.circle(7)
t.end_fill()


t.pu()
t.goto(64,125)

t.pd()
t.begin_fill()
t.circle(7)
t.end_fill()

# 身体
t.color("black")
t.pu()
t.goto(-50,100)

t.pd()
t.seth(-140)
t.circle(130,80)

t.pu()
t.goto(64,100)

t.pd()
t.seth(-40)
t.circle(-130,80)


t.seth(-140)
t.circle(-130,80)

# 手
t.pu()
t.goto(-50,102)
t.pd()
t.seth(-160)
t.circle(130,80)
t.seth(-80)
t.circle(20,180)

t.pu()
t.goto(65,102)
t.pd()
t.seth(-20)
t.circle(-130,80)
t.seth(-100)
t.circle(-20,180)

# 脚
t.pu()
t.goto(-60,-82)
t.pd()
t.seth(-95)
t.circle(150,20)
t.seth(-75)
t.circle(20,120)
t.seth(50)
t.circle(80,38)

t.pu()
t.goto(63,-82)
t.pd()
t.seth(-85)
t.circle(-150,20)
t.seth(-105)
t.circle(-20,120)
t.seth(130)
t.circle(-80,38)

# 心

def curvemove():
    for i in range(200):
        right(1)
        forward(1)
t.pu()
t.color("pink")
t.goto(50,60)
t.pd()
t.begin_fill()
t.seth(105)
t.circle(5,180)
t.seth(-60)
t.fd(19)
t.end_fill()


t.pu()
t.goto(50,60)
t.pd()
t.begin_fill()
t.seth(75)
t.circle(-5,180)
t.seth(-120)
t.fd(19)
t.end_fill()


myWin.exitonclick()



