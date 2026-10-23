import turtle

#--setup--
wn=turtle.Screen()
wn.bgcolor("lightgreen")

tess=turtle.Turtle()

#--functions--
def drawPoly(someturtle,somesides,somesize):
    angle= 360/somesides
    for i in range (somesides):
        someturtle.forward(somesize)
        someturtle.left(angle)
def drawSpiral(someturtle , angle,):
    size=1
    for i in range(100):
        someturtle.forward(size)
        someturtle.right(angle)
        size=size+2
def drawEquitriangle(someturtle ,somesize):
    drawPoly(someturtle,3,somesize)
def drawStar(someturtle,size,):
    for i in range (5):
        someturtle.forward(size)
        someturtle.right(144)
def drawSprite(someturtle ,legs,lenght):
    angle= 360/legs
    for i in range (legs):
        someturtle.forward(lenght)
        someturtle.backward(lenght)
        someturtle.left(angle)


#--exercises--
#Exercise1
# tess.pensize(3)
# tess.pencolor("hotpink")
# drawPoly(tess,8,50)

#Exercise2
# tess.pencolor("blue")
# for i in range(20):
#     drawPoly(tess,4,100)
#     tess.left(18)
#Exercise3
# tess.pencolor("blue")
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# drawSpiral(tess, 90)
#
# tess.penup()
# tess.goto(150,0)
# tess.pendown()
# drawSpiral(tess ,89)
#Exercise4
# drawEquitriangle(tess,100)
# #Exercise5
# tess.pencolor("hotpink")
# for i in range(5):
#     drawStar(tess,50)
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()
#Exercise6
# drawSprite(tess,15 ,120)






#--finish--
wn.exitonclick()