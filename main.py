import turtle as t
import random
import time

# Setup screen
screen = t.Screen()
screen.colormode(255)
screen.bgcolor(0, 113, 193)
screen.setup(600, 600)
screen.title("Sailing Strait")
screen.register_shape('boat.gif')
screen.register_shape('rock.gif')

scoreNum = 0

# Score display
score = t.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 160)
score.write(f"Score: {scoreNum}", align="center", font=("Courier", 16, "normal"))

# Boat setup
boat = t.Turtle()
boat.penup()
boat.speed(10)
boat.shape("boat.gif")
boat.goto(0, -100)

# Obstacle setup
obstacleSpeed = 20
obstacle = t.Turtle()
obstacle.shape("rock.gif")
obstacle.penup()
obstacle.goto(0, 300)

def pressP():
    screen.bye()

# Boat movement functions
def moveBoatLeft():
    x = boat.xcor()
    boat.setx(x - 20)

def moveBoatRight():
    x = boat.xcor()
    boat.setx(x + 20)

# Obstacle generation
def generateObstacles():
    obstacle.setx(1000)
    obstacle.sety(700)
    time.sleep(0.5)
    obstacle.setx(random.randint(-190, 190))

# Obstacle movement
def moveObstacle():
    global scoreNum, obstacleSpeed
    y = obstacle.ycor()
    obstacle.sety(y - obstacleSpeed)
    if obstacle.distance(boat) < 100:  # Adjusted for a larger obstacle
        die()

    if y < -350:
        scoreNum += 1
        obstacleSpeed += 1
        score.clear()
        score.write(f"Score: {scoreNum}", align="center", font=("Courier", 16, "normal"))
        generateObstacles()

# Main menu
def menu():
    score.clear()
    boat.goto(0, 800)

    global title, subtitle, playButton
    title = t.Turtle()
    title.speed(0)
    title.color("white")
    title.penup()
    title.goto(0, 150)
    title.write("Sailing Strait!", align="center", font=("Courier", 20, "bold"))

    subtitle = t.Turtle()
    subtitle.speed(0)
    subtitle.color("white")
    subtitle.penup()
    subtitle.goto(0, 130)
    subtitle.write("By Ethan", align="center", font=("Courier", 16, "bold"))

    playButton = t.Turtle()
    playButton.speed(0)
    playButton.color("white")
    playButton.penup()
    playButton.goto(0, 50)
    playButton.write("Press Space To Play!", align="center", font=("Courier", 16, "bold"))

    title.hideturtle()
    subtitle.hideturtle()
    playButton.hideturtle()

# Start the game
def play():
    global scoreNum
    scoreNum = 0
    score.write(f"Score: {scoreNum}", align="center", font=("Courier", 16, "normal"))
    title.clear()
    subtitle.clear()
    playButton.clear()
    boat.goto(0, -100)

# Game over function
def die():
    obstacle.hideturtle()
    boat.hideturtle()
    score.goto(0, 0)
    score.write(f"Game Over!  Score: {scoreNum}", align="center", font=("Courier", 24, "normal"))
    screen.update()
    time.sleep(5)
    screen.bye()

# Game loop
def gameLoop():
    moveObstacle()
    screen.ontimer(gameLoop, 100)

# Initialization
def init():
    screen.listen()
    screen.onkey(moveBoatLeft, "a")
    screen.onkey(moveBoatRight, "d")
    screen.onkey(play, "space")
    screen.onkey(pressP, "p")
    generateObstacles()
    gameLoop()

# Start the game
menu()
init()
screen.mainloop()