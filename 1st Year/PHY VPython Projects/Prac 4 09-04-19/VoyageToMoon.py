# Models a voyage from an orbit around Earth to the Moon
# Miles Kidson
# 8 April 2019

from vpython import *

# objects

earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.blue)
moon = sphere(pos=vector(4e8,0,0), radius=1.75e6, color=color.white)
craft = sphere(pos=vector(0,6.4e6+50000,0), radius=1e6, color=color.red)

# constants

earth.M = 6e24
moon.M = 7e22
craft.M = 175
G = 6.67e-11

scene.autoscale=1
t = 0
dt = 10

craft.trail = curve(pos=craft.pos, color=color.cyan)

craft.v = vector(7876,0,0)
craft.p = craft.M*craft.v

work = 0.0
#7876


while t < 4*3600*24:
    
    rate(500)
    
    #earth stuff
    R = craft.pos-earth.pos
    magR = mag(R)
    forceEarth = -(G*earth.M*craft.M*R)/magR**3
    
    # moon stuff
    Rmoon = craft.pos-moon.pos
    magRmoon = mag(Rmoon)
    forceMoon = -(G*moon.M*craft.M*Rmoon)/magRmoon**3
        
    #updates position, momentum, and trail
    craft.p += (forceEarth+forceMoon)*dt
    craft.pos += (craft.p/craft.M)*dt
    craft.trail.append(pos=craft.pos)
    
    #calculates work
    deltar = (craft.p/craft.M)*dt
    w = dot(forceEarth+forceMoon, deltar)
    work += w
    

    if t == 4650:
        craft.v = (craft.p/mag(craft.p))*1.3e4
        craft.p = craft.M*craft.v
        
    if magRmoon <= moon.radius:
        print("Oopsie Poopsie you crashed into the moon!!!\nTry again you big dummy.")
        print("The work done is:", work)
        break
        
    
    #update t
    t += dt