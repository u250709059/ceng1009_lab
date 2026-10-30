# def sumTo(n):
#     total = n+ (n+1)/2
#     return total
# print(sumTo(10))
# n=int(input("please enter a number:"))
# print( "print sum is", sumTo(n))
#
# import turtle
# def drawstar(t , n ,size):
#     angle =180 - 180 /n
#     for i in range(n):
#         t.forward(size)
#         t.right(angle)
#
#
# wn =turtle.Screen()
# t = turtle.Turtle()
# t.pensize(3)
#
# drawstar(t ,11,100)
# wn.exitonclick()
import numbers


# def sumTo(n):
#     total = 0
#
#     for i in range (1 , n+1):
#         total += i
#     return total
# print(sumTo(10))
# n = int (input("Enter a number: "))
# print(" sum is ", sumTo(n))

# import math
#
# def mySqrt(x):
#     guess = x / 2
#     for i in range (20):
#         guess = (1/2) * (guess + x / guess)
#     return guess
# n = int(input("Enter a positive integer: "))
# print(" the result is " , mySqrt(n))
# print(" the result is " , math.sqrt(n))
#
# import turtle
#
#
# def drawSprite(someturtle , legs ,lenght):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(lenght)
#         someturtle.backward(lenght)
#         someturtle.left(angle)
# def fancySquare(t , side):
#     for corner in range (4):
#         drawSprite(t  ,8 ,20)
#         t.forward(side)
#         t.left(90)
#
# wn = turtle.Screen()
# t=turtle.Turtle()
# t.color("pink")
# t.speed(1)
# t.pensize(2)
# fancySquare(t,100)
# wn.exitonclick()
#
# import turtle
# def drawTip(t, side):
#     t.begin_fill()
#     t.left(90)
#     t.forward(side/2)
#     t.right(120)
#     t.forward(side)
#     t.right(120)
#     t.forward(side)
#     t.right(120)
#     t.forward (side / 2)
#     t.right(90)
#     t.end_fill()
# def drawSpirateWithTips(someturtle ,legs,lenght):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(lenght)
#         drawTip(someturtle, 10)
#         someturtle.backward(lenght)
#         someturtle.left(angle)
#
# def fancySquare (t, size):
#     for corner in range (4):
#         drawSpirateWithTips(t ,8, 20)
#         t.forward(size)
#         t.left(90)
# wn=turtle.Screen()
# wn.bgcolor("lightgreen")
# t=turtle.Turtle()
# t.pensize(2)
# fancySquare(t, 100)
# wn.exitonclick()

# def chechSign(x):
#     if x >0 :
#         return "the number is positive"
#     elif x < 0 :
#         return "the number is negative"
#     else:
#         return "the number is zero"
#
#
# numbers = [-7  , 5 , 0]
# for number in numbers:
#     print(number , "is" , chechSign(number))
# n = int(input("Enter a number: "))
# print(chechSign(n))

# import turtle
# def drawBar(t,height ,gap):
#     t.penup()
#     t.left(90)
#     t.forward(height + gap)
#     t.write(""+ str(height))
#     t.backward(height + gap)
#     t.right(90)
#     t.pendown()
#
#
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()




def barChart(data):
    maxheight = max(data)
    num_bars = len(data)
    border = 10

    gap =(maxheight - border)/ 25

    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    right  = 40 * num_bars + border
    top =maxheight + 4 * gap
    wn.setworldcoordinates(-border, -border,right,top)
    t=turtle.Turtle()
    t.color("blue")
    t.fillcolor("red")
    t.pensize(3)
    for height in data:
        drawBar(t, height, gap)
    wn.exitonclick()
data = [48,117,200,240,160,260,220]

barChart(data)






