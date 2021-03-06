import turtle
import random
turtle.setup(700, 700)
wn = turtle.Screen()
wn.bgcolor('light green')
screen = turtle.Turtle()
screen.pensize(3)
screen.speed(0)

actualAnswer = 0
playerSpeed = 0

contestant1 = turtle.Turtle()
contestant2 = turtle.Turtle()
contestant3 = turtle.Turtle()
player = turtle.Turtle()

contestants = [contestant1, player, contestant2, contestant3]

questionWriter = turtle.Turtle()

def setInitialPositions():
    x = -150
    y = -240
    for i in contestants:
        i.speed(0)
        i.penup()
        i.goto(x,y)
        i.color('green')
        i.shape('turtle')
        i.lt(90)
        x += 100
    player.color('red')

def setPlayfield():
    screen.penup()
    screen.goto(-250,-250)
    screen.pendown()
    screen.fd(500)
    screen.lt(90)
    screen.fd(500)
    screen.lt(90)
    screen.fd(500)
    screen.lt(90)
    screen.fd(500)
    screen.penup()
    screen.goto(0,-180)
    screen.lt(180)
    screen.pendown()
    for i in range (5):
        screen.fd(35)
        screen.penup()
        screen.fd(35)
        screen.pendown()
    screen.fd(20)
    screen.pensize(4)
    screen.penup()
    screen.goto(-250,200)
    screen.rt(90)
    screen.pendown()
    screen.color("red")
    screen.fd(500)
    screen.penup()
    screen.goto(-70,210)
    screen.write("F   I   N   I   S   H",move=False, align='left', font=('Arial',15,'bold'))
    screen.goto(-56,-230)
    screen.color("orange")
    screen.write("S  T  A  R  T",move=False, align='left', font=('Arial',15,'bold'))
    screen.goto(-250,-200)
    screen.pendown()
    screen.fd(500)
    screen.ht()
    questionWriter.penup()
    questionWriter.goto(-200,230)
    questionWriter.ht()

setInitialPositions()
setPlayfield()


def answer(received):
    return 0.2 if received == actualAnswer else -0.2

def onePressed():
    global playerSpeed
    playerSpeed += answer(1)
    if(playerSpeed < 0.5):
        playerSpeed = 0.5
    generateQuestion()
def twoPressed():
    global playerSpeed
    playerSpeed += answer(2)
    if(playerSpeed < 0.5):
        playerSpeed = 0.5
    generateQuestion()
def threePressed():
    global playerSpeed
    playerSpeed += answer(3)
    if(playerSpeed < 0.5):
        playerSpeed = 0.5
    generateQuestion()
def fourPressed():
    global playerSpeed
    playerSpeed += answer(4)
    if(playerSpeed < 0.5):
        playerSpeed = 0.5
    generateQuestion()
def fivePressed():
    global playerSpeed
    playerSpeed += answer(5)
    if(playerSpeed < 0.5):
        playerSpeed = 0.5
    generateQuestion()
def sixPressed():
    global playerSpeed
    playerSpeed += answer(6)
    if(playerSpeed < 0.5):
        playerSpeed = 0.5
    generateQuestion()
def sevenPressed():
    global playerSpeed
    playerSpeed += answer(7)
    if(playerSpeed < 0.5):
        playerSpeed = 0.5
    generateQuestion()
def eightPressed():
    global playerSpeed
    playerSpeed += answer(8)
    if(playerSpeed < 0.5):
        playerSpeed = 0.5
    generateQuestion()
def ninePressed():
    global playerSpeed
    playerSpeed += answer(9)
    if(playerSpeed < 0.5):
        playerSpeed = 0.5
    generateQuestion()



turtle.onkey(onePressed,"1")
turtle.onkey(twoPressed,"2")
turtle.onkey(threePressed,"3")
turtle.onkey(fourPressed,"4")
turtle.onkey(fivePressed,"5")
turtle.onkey(sixPressed,"6")
turtle.onkey(sevenPressed,"7")
turtle.onkey(eightPressed,"8")
turtle.onkey(ninePressed,"9")
turtle.listen()


plusPairs = [[0,1], [0,2], [0,3], [0,4],
              [0,5], [0,6], [0,7], [0,8],
              [0,9], [1,1], [1,2], [1,3],
              [1,4], [1,5], [1,6], [1,7],
              [1,8], [2,2], [2,3], [2,4],
              [2,5], [2,6], [2,7], [3,3],
              [3,4], [3,5], [3,6], [4,4],
              [4,5]]

minusPairs = [[1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [1,9], [1,10],
              [2,3], [2,4], [2,5], [2,6], [2,7], [2,8], [2,9], [2,10] [2,11],
              [3,4], [3,5], [3,6], [3,7], [3,8], [3,9], [3,10], [3,11], [3,12],
              [4,4], [4,5], [4,6], [4,7], [4,8], [4,9], [4,10], [4,11], [4,12], [4,13],
              [5,6], [5,7], [5,8], [5,9], [5,10], [5,11], [5,12], [5,13], [5,14],
              [6,7], [6,8], [6,9], [6,10], [6,11], [6,12], [6,13], [6,14], [6,15],
              [7,8], [7,9], [7,10], [7,11], [7,12], [7,13], [7,14], [7,15], [7,16],
              [8,9], [8,10], [8,11], [8,12], [8,13], [8,14], [8,15], [8,16], [8,17],
              [9,10], [9,11], [9,12], [9,13], [9,14], [9,15], [9,16], [9,17], [9,18]]

def printQuestion(questionString):
    questionWriter.write(questionString,move=False, align='left', font=('Arial',17,'bold'))

def generateQuestion():
    plusOrMinus = random.randint(0,1)
    if(plusOrMinus == 0):
        randomInd = random.randint(0, len(plusPairs) - 1)
        pair = plusPairs[randomInd]
        questionString = pair[0] + " + " + pair[1] + " = ?"
        actual = pair[0] + pair[1]
        printQuestion(questionString)

generateQuestion()

while(player.ycor() <=201):
    player.fd(playerSpeed)
    
