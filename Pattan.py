import turtle
ter=turtle.Turtle()
ter.speed(0)

def drow(size,angle):
    for j in range(4):
        ter.fd(size)
        ter.right(angle)
    

print('lets start')
for i in range(36):
    drow(100,90)
    ter.right(11)
    ter.color("Blue")

for i in range(36):
    drow(100,90)
    ter.right(11)
    ter.color("Green")

for i in range(36):
    drow(100,90)
    ter.right(11)
    ter.color("Red")
