# step 1
import turtle
import random
import math
# setup the screen
screenobj=turtle.Screen()
screenobj.bgcolor('black')
screenobj.title('Space X')
screenobj.bgpic('background.gif')

#drow the Border
pen_1=turtle.Turtle()
pen_1.speed(0)
pen_1.color('white')
pen_1.up()
pen_1.goto(-260,-260)
pen_1.down()
pen_1.pensize(4)
for i in range(4):
    pen_1.fd(520)
    pen_1.lt(90)
pen_1.hideturtle()

#set score 0
score=0
# drow score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.up()
score_pen.color('white')
score_pen.setposition(-240,260)
score_pen.hideturtle()
scorest='score: %s' %score
score_pen.write(scorest,False,align='left',font=('Arial',14,'normal'))


# Desining the player
player=turtle.Turtle()
player.speed(0)
player.color("blue")
player.shape("turtle")
player.up()
player.goto(0,-240)
player.lt(90)
playerspeed=15
player.shapesize(1.5,1.5)
# movement of player

def move_left():
    x=player.xcor()
    x-=playerspeed
    if x< -250:
        x=-250
    player.setx(x)

def move_right():
    x=player.xcor()
    x+=playerspeed
    if x> 250:
        x=250
    player.setx(x)
def fire_bullet():
    #delear bullet state as global
    global bulletstate
    if bulletstate=="ready":
        bulletstate='fire'
        # place the bullet just above the player
        x=player.xcor()
        y=player.ycor() +10
        bullet.goto(x,y)
        bullet.showturtle()

def isCollision(bul,ene):
    distance=math.sqrt(math.pow(bul.xcor()-ene.xcor(),2)+math.pow(bul.ycor()-ene.ycor(),2))
    if distance < 15:
        return True
    else:
        return False



#creat keybord bindibg
alu=turtle.Screen()
alu.listen()
alu.onkey(move_left,'Left')
alu.onkey(move_right,'Right')
alu.onkey(fire_bullet,'space')


#chose number of enemy
num_of_enemys=5
#creat a empty list
enemys=[]
# add enemys to the list
for i in range(num_of_enemys):
 # create enemy
    enemys.append(turtle.Turtle())
for enemy in enemys:

    enemy.speed(0)
    enemy.color("red")
    enemy.shape("circle")
    enemy.shapesize(1.5,1.5)
    enemy.up()
    m=random.randint(-240,200)
    n=random.randint(50,240)
    enemy.goto(m,n)
enemyspeed= 2


# players bullet
bullet=turtle.Turtle()
bullet.speed(0)
bullet.color("yellow")
bullet.shapesize(0.5,0.5)
bulletspeed=20
bullet.shape("triangle")
bullet.up()
bullet.setheading(90)
bullet.hideturtle()
#define bullet state
#ready- ready to fire
#fire - the bulllet is firing
bulletstate='ready'




# main game loop
while True:

    #enemy movement
    for enemy in enemys:
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)
    # move enemy back
        if enemy.xcor()> 240:
            for e in enemys:
                y=e.ycor()
                y-=40
                e.sety(y)
            enemyspeed*=-1
        if enemy.xcor()< -240:
            for e in enemys:
                y=e.ycor()
                y-=40
                e.sety(y)
            enemyspeed*=-1
        #collision between bullt and enemy
        if isCollision(bullet,enemy):
            #reset the bullet
            bullet.hideturtle()
            bulletstate='ready'
            # update score
            score=score+10
            scorest='score: %s' %score
            score_pen.clear()
            score_pen.write(scorest,False,align='left',font=('Arial',14,'normal'))

            #reset the enemy
            m=random.randint(-240,200)
            n=random.randint(50,240)
            enemy.goto(m,n)
    # check the collision between enemy and player
        if isCollision(enemy,player):
            enemy.hideturtle()
            player.hideturtle()
            print("Game Over")
            over_pen=turtle.Turtle()
            over_pen.speed(0)
            over_pen.up()
            over_pen.color('white')
            over_pen.setposition(-150,0)
            over_pen.hideturtle()
            overst='Game Over'
            over_pen.write(overst,False,align='left',font=('Arial',34,'normal'))

            break



# bullet movement
   # if bulletstate=="fire":
    y=bullet.ycor()
    y+=bulletspeed
    bullet.sety(y)

    # check the bullet if it cross the border
    if bullet.ycor() > 260:
        bulletstate='ready'




screenobj.mainloop()
