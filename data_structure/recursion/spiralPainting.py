#coding:utf-8

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()
def drawSpiral(myTurtle, length):
    """用海龟通过递 归的方法来画一个螺旋线"""

    if length > 0:
        myTurtle.forward(length)
        myTurtle.right(90)
        drawSpiral(myTurtle, length - 5)

drawSpiral(myTurtle,100)
myWin.exitonclick()
