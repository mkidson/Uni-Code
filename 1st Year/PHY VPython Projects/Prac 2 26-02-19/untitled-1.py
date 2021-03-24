# VPython assignment for PHY1004W
# Miles Kidson
# 26-02-19

from vpython import *

# objects
ball = sphere(pos=vector(0,0,0), radius=0.5, color=color.cyan)

# creates a box missing two sides and with side length 20. centre is at the origin.
wallR = box(pos=vector(10,0,0), size=vector(0.2,20,20), color=color.green)              # Right wall
wallL = box(pos=vector(-10,0,0), size=vector(0.2,20,20), color=color.green)             # Left wall
wallU = box(pos=vector(0,10,0), size=vector(20,0.2,20), color=color.green)              # Up wall
wallD = box(pos=vector(0,-10,0), size=vector(20,0.2,20), color=color.green)             # Down wall
wallF = box(pos=vector(0,0,10), size =vector(20,20,0.2), color=color.green, opacity=0)  # Front wall (invisible)
wallB = box(pos=vector(0,0,-10), size=vector(20,20,0.2), color=color.green)             # Back wall


# creates a trail for the ball
ball.trail = curve(color=ball.color) 

# initial values
#ball.velocity = vector(25,5,15)

ball.velocity = vector(0,0,0)   # assigns the ball a velocity of (0,0,0)
ball.velocity.x = eval(input("What is the ball's velocity in the x direction: ")) # asks for a velocity in the x direction
ball.velocity.y = eval(input("What is the ball's velocity in the y direction: ")) 
ball.velocity.z = eval(input("What is the ball's velocity in the z direction: ")) 

deltat = 0.005
t = 0
vscale = 0.1
scene.autoscale = 0 

# defines an arrow representing the velocity vector of the ball
varr = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=color.yellow)

# calculations
while t < 3:
    if ball.pos.x >= wallR.pos.x:                
        ball.velocity.x = -ball.velocity.x      # if ball hits a wall it bounces off (reverses velocity in respective direction)
    if ball.pos.x <= wallL.pos.x:                
        ball.velocity.x = -ball.velocity.x      
    if ball.pos.y >= wallU.pos.y:
        ball.velocity.y = -ball.velocity.y      
    if ball.pos.y <= wallD.pos.y:
        ball.velocity.y = -ball.velocity.y
    if ball.pos.z >= wallF.pos.z:
        ball.velocity.z = -ball.velocity.z
    if ball.pos.z <= wallB.pos.z:
        ball.velocity.z = -ball.velocity.z
    
    ball.pos += ball.velocity*deltat            # updates ball's position with respect to it's velocity
    ball.trail.append(pos=ball.pos)             # appends a new piece of the trail to the ball's current position
    varr.pos = ball.pos                         # updates velocity vector arrow position to be the same as the ball's
    varr.axis = vscale*ball.velocity            # updates velocity vector arrow direction based on velocity of the ball
    t += deltat                                 # updates current time
    rate(100)