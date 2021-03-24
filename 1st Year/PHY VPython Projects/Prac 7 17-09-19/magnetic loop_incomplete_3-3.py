from vpython import *

## Motion of a charged particle in the (dipole) magnetic field of a circular coil of current
## Based on the original code from Roger Fearick, September 2008
## Updated to work with Python 3 and VPython 7

## Define the circular current-carring loop
def makeloop(rloop,loopradius):
    dtheta=pi/100       # loop is made of segments of this size
    loop = curve(color = vector(1.,.7,.2), radius = 0.01) # visualize loop
    for theta in arange(0.0, 2.0 * pi, dtheta):
        loop.append(rloop + vector(loopradius*sin(theta), 0.0, loopradius*cos(theta)))
    loop.append(loop.point(0)['pos']) # close loop
    return loop

loop = makeloop(vector(0.0,0.0,0.0), 0.3)

## Calculate the magnetic field at r due to the loop
## Note: (mu0/4pi)I arbitrarily set to 10.0
def Field(r, loop):
    B = vector(0,0,0);
    loop_positions = loop.slice(0,-1)
    # print(loop_positions)
    for i in range(len(loop_positions)-1):
        dR = (loop_positions[i]['pos']+loop_positions[i+1]['pos'])/2 - r     # distance r to loop segment
        dI = loop_positions[i]['pos'] - loop_positions[i-1]['pos']           # delta I
        B += cross(dI, dR) / mag(dR)**3
    return 10*B

## Display the magnetic field at a few positions (on the x-y plane)
showfields=1
if showfields:
    #print Field(r0)
    for y in arange(-1.3,1.4,0.2):
        for x in arange(-1.3,1.4,0.2):
            rx=vector(x,y,0)
            B=Field(rx,loop)
            B=B/100.0
            c=color.red
            if mag(B)>0.3:
                B*=0.3/mag(B)
                c=color.magenta
            arrow(pos=rx,axis=B,color=c)

## ============================================

## Model the motion of a charged particle in the magnetic field

## Take out all # below where appropriate and complete the program

## constants
q = -10.0
m = 1.0

## initial conditions
t = 0
r = vector(0.8, -0.5, 0.0)
v = vector(0.0, 0.0, 0.5)

## integrate
dt = 1e-3

trail = curve(pos=r, radius=0.005, color=color.green)
KE = gcurve()
K = (1/2)*m*mag(v)**2

while t < 30:
    ## update clock time
    t += dt
    
    ## B field at r
    B = Field(r,loop)
    
    magB = mag(B)
    Bhat = B/magB
    f = q * magB/m
    theta = f*dt
    sintheta = sin(theta)
    costheta = cos(theta)
    v += sintheta * cross(v, Bhat) + (1 - costheta) * cross(cross(v, Bhat), Bhat)
    r += v*dt
    
    ### update motion
    #F1 = q*v.cross(B)
    #dv = F1 *dt/m
    
    #F2 = q * cross(v+dv, B)
    #v += 0.5 * (F1+F2)*dt/m
    #r += v*dt
    
    trail.append(pos=r)
    
    K = (1/2)*m*mag(v)**2
    KE.plot(pos=(t, K))
