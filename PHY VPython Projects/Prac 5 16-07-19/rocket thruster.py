# emulates a rocket thruster
# Miles Kidson
# 16-07-19

from vpython import *

c = 0.7
M = 3.2
R = 0.87
Fmag = 3.4
I = c*M*(R**2)

theta = (3*pi)/2
omega = 0

rcm = vector(0,0,0)
pcm = vector(0,0,0)
Fvector = vector(-Fmag*sin(theta), Fmag*cos(theta), 0)

t = 0
dt = 0.1

trail = curve(pos=rcm, color=color.yellow, radius = 0.05)

while t < 10000:
    rate(100)
    t += dt
    
    Fvector = vector(-Fmag*sin(theta), Fmag*cos(theta), 0)
    omega += (Fmag*R/I)*dt
    theta += omega*dt + ((Fmag*R)/(2*I))*dt**2
    pcm += Fvector*dt
    rcm += (pcm/M)*dt + (Fvector/(2*M))*dt**2
    
    trail.append(pos=rcm)
    