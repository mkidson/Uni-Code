from vpython import *

## Scene setup
scene.width = 600
scene.height = 480
scene.x = scene.y = 0
scene.forward = vector(-0.2,-0.5,-1)
scene.background = color.black

## Main scale factors
xmax = 0.5
dx = xmax/5

## Comment 1:
grid = [ ]
for x in arange(-xmax, xmax+dx, dx):
    grid.append(curve(pos=[vector(x, 0, -xmax), vector(x, 0, xmax)], color=vector(.7, .7, .7)))
for z in arange(-xmax, xmax+dx, dx):
    grid.append(curve(pos=[vector(-xmax, 0, z), vector(xmax, 0, z)], color=vector(.7, .7, .7)))

## E field
E0 = vector(0, 1e-6, 0)

## Comment 2:
efield = [ ]
escale = 1e5
for x in arange(-xmax, xmax+dx, 2*dx):
    for z in arange(-xmax, xmax+dx, 2*dx):
        efield.append(arrow(pos=vector(x, 0, z), axis=E0*escale, color=vector(1, 1, 0)))

## Particle properties
particle = sphere(pos=vector(-xmax*2,2*dx,xmax/8.), color=vector(1,0,0), radius = dx/8.)
particle.charge = 1.6e-19
particle.mass = 1.7e-27
particle.velocity = vector(10, 0, 0)

## Force vector arrow
farrow = arrow(pos=particle.pos, axis=vector(0,0,0), color=vector(0.6,0.6,0.6))
fscale = 0.5e24

## Velocity vector arrow
varrow = arrow(pos=particle.pos, axis=vector(0,0,0), color=color.green)
vscale = 1e-2

## Comment 3:
dt = 1e-3

## Particle trail
particle.trail = curve(color=particle.color)

## Main calculation
t = 0
while t < 1:
    if -xmax < particle.pos.x < xmax and -xmax < particle.pos.z < xmax:
        E = E0
    else:
        E = vector(0,0,0)

## Calculate force on particle
    F = E

## Update velocity of particle
    particle.velocity =

## Update position of particle
    particle.pos =

    particle.trail.append(pos=particle.pos)
    t = t + dt
    Fmag=mag(F)
    vmag = mag(particle.velocity)

## Scaling and moving arrows
    farrow.pos = particle.pos
    farrow.axis = F*fscale
    varrow.pos = particle.pos
    varrow.axis = particle.velocity*vscale
