from turtle import *

def draw_half(radius, color1, color2):
    shapesize(3,3,5)
    width(4)
    color(color1)
    begin_fill()
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    end_fill()
    left(90)
    up()
    forward(radius*0.375)
    speed(-50)
    right(90)
    down()
    color(color2)
    begin_fill()
    circle(radius*0.125)
    end_fill()
    left(90)
    up()
    backward(radius*0.375)
    down()
    left(90)

def main():
    reset()
    bgcolor('firebrick1')
    draw_half(300, 'black', 'white')
    draw_half(300, 'white', 'black')
    ht()
    return "DONE! :-)"

if __name__ == '__main__':
    main()
    mainloop()
