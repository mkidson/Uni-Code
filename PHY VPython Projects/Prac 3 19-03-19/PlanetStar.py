# A star with a planet orbiting it 
# Miles Kidson
# 19 March 2019

from vpython import *

sun = sphere(pos=vector(0,0,0), radius=1.5e10, color=color.yellow)
earth = sphere(pos=vector(1.5e11,0,0), radius=6.4e9, color=color.blue)
sun.M = 2e30
earth.M = 6e24
G = 6.67e-11

scene.autoscale=1
t = 0
dt = 24*3600

earth.p = earth.M*vector(sin(15)*sqrt(G*sun.M/mag(sun.pos-earth.pos)),sqrt(G*sun.M/mag(sun.pos-earth.pos)),0)
sun.p = sun.M*vector(0,0,0)

earth.trail = curve(pos=earth.pos, color=color.cyan)
sun.trail = curve(pos=sun.pos, color=color.red)

while t < 1000*dt:
    rate(50)
    R = earth.pos-sun.pos
    magR = mag(R)
    forceEarth = -(G*sun.M*earth.M*R)/magR**3
    earth.p += forceEarth*dt
    earth.pos += (earth.p/earth.M)*dt
    earth.trail.append(pos=earth.pos)
    
    Rsun = sun.pos-earth.pos
    magRsun = mag(Rsun)
    forceSun = -forceEarth
    sun.p += forceSun*dt
    sun.pos += (sun.p/sun.M)*dt
    sun.trail.append(pos=sun.pos)    
    t += dt