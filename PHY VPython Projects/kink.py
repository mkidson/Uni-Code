# GlowScript 2.9 VPython

# Written by Bruce Sherwood, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0
from vpython import *

scene.width = scene.height = 600
max = 7.5
scene.range = max
scene.background = color.white
scene.caption = "Accelerated charge; click to run or pause."

start = sphere(pos=vector(0,0,0), radius=0.1, color=vector(1,.5,.5))
proton = sphere(pos=vector(0,0,0),radius=0.1, color=color.red)
rad = 0.5
lines = []
for theta in arange(0,2*pi,pi/8):
    a = curve(pos=[vector(0,0,0), vector(.5*max*cos(theta), .5*max*sin(theta),0),
                 vector(1*max*cos(theta),1*max*sin(theta),0), vector(2*max*cos(theta),2*max*sin(theta),0)],
                    color=vector(1,.5,0),radius=0.03)
    lines.append(a)
dt = 0.01
vmag = 0.01
v = vector(0,-vmag,0)
c = 10*vmag
a = rad/2 ## magnitude of acceleration (arbitrary, to get visible kinks)
ahat = vector(0,-1,0)

def getclick(evt):
    global run
    run = not run

scene.bind('click', getclick)

run = False
first = True
while True:
    rate(500)
    if first:
        t = 0
        proton.pos = vector(0,0,0)
        first = False
    if not run: continue
    proton.pos = proton.pos + v*dt
    for fl in lines:
        # Note that in GlowScript modifying a curve is quite different from classic VPython
        fl.modify(0, pos=proton.pos) ## beginning of line tracks proton
        r = fl.slice(3)[0].pos ## from origin to end of line
        rhat = norm(r)
        fl.modify(2, pos=rhat*c*t) ## end of the kink
        zvector = -cross(rhat, ahat) # +z if rhs, -z if lhs          
        rhatperp = norm(cross(rhat,zvector)) ## vector perp to r and zhat 
        magaperp = mag(cross(rhat,norm(proton.pos))) ## sin theta
        b = rhatperp*magaperp*a
        fl.point(1).pos = fl.point(2).pos+b
        fl.modify(1, pos=fl.slice(2)[0].pos + b)
    t = t+dt
    if c*t > max:
        run = False
        first = True