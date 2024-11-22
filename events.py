import turtle,random
pen = turtle.Turtle()
screen = turtle.Screen()

colors = ["red", "blue", "green", "orange", "pink", "pink", "purple", "yellow", "magenta", "black"]

def click(x,y):
 color = random.choice(colors)
 screen.bgcolor(color)

turtle.onscreenclick(click)

turtle.done()