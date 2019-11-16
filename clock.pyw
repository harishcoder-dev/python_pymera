#!/usr/bin/python3.5
import turtle
import datetime
import time

def drawclock(radius,hours,minutes,length,color):
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(0,radius)
    turtle.bgcolor("yellow")
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.pencolor("darkgray")
    turtle.begin_fill()
    for degree in range(0,360,360//minutes):
        turtle.circle(-radius,360//minutes)
        turtle.right(90)
        turtle.forward(length/3)
        turtle.back(length/3)
        turtle.left(90)
    turtle.end_fill()
    turtle.pencolor("black")
    for degree in range(0,360,360//hours):
        turtle.circle(-radius,360//hours)
        turtle.right(90)
        turtle.forward(length)
        turtle.back(length)
        turtle.left(90)
    turtle.circle(-radius)

def drawhand(angle, radius, width, color, outline=False):
    if outline:
        turtle.pencolor("black")
    else:
        turtle.pencolor(color)
    turtle.pensize(2)
    turtle.penup()
    turtle.home()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.left(90)
    turtle.right(angle)
    turtle.forward(radius)
    turtle.pendown()
    turtle.left(150)
    turtle.forward(width)
    turtle.home()
    turtle.left(90)
    turtle.right(angle)
    turtle.penup()
    turtle.forward(radius)
    turtle.pendown()
    turtle.right(150)
    turtle.forward(width)
    turtle.home()
    turtle.end_fill()

radius=200
turtle.speed(0)
turtle.hideturtle()
turtle.title("Analog Clock")
drawclock(radius,12,60,radius*.1,"lightgray")
current_time=datetime.datetime.now().time()
turtle.title(current_time.strftime("%H:%M Analog Clock"))
drawhand(current_time.minute * 6, radius * .9, radius // 10, "gray")
drawhand(((current_time.hour + current_time.minute / 60) % 12) * 30, radius * .6, radius // 10, "black")

while True:
    new_time=datetime.datetime.now().time()
    if current_time.minute is not new_time.minute:
        turtle.title(new_time.strftime("%H:%M Analog Clock"))
        drawhand(current_time.minute * 6, radius * .9, radius // 10, "lightgray")
        drawhand(((current_time.hour + current_time.minute / 60) % 12) * 30, radius * .6, radius // 10, "lightgray")
        drawhand(new_time.minute * 6, radius * .9, radius // 10, "gray")
        drawhand(((new_time.hour + new_time.minute / 60) % 12) * 30, radius * .6, radius // 10, "black")
    current_time=new_time
    time.sleep(60)