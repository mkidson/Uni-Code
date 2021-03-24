from vpython import *

#PHY1004W Springs laboratory - Python 3 Code

# Writing to file ... remove the # from the two lines below to enbale writing to file (and also right at the bottom of the code):
# print 'The raw, simulated data will be output to a text file.'
# Fout = open(raw_input('Enter file name: '), 'w');

# Plot setup
graph(x=0, y=0, width=600, height=550,
             title='Position-Time Graph', xtitle='t(s)', ytitle='y(m)',
             xmax=10., xmin=0., ymax=0.1, ymin=-0.1,
             foreground=color.white, background=color.black)

VPlot = gcurve(color=color.yellow)

# Scene setup
scene.title = 'Vertical spring-mass system'
scene.width = 500
scene.height = 500
scene.autoscale = 1                 ##0 means autoscaling is OFF
scene.userzoom = 1                  ##0 means user cannot zoom
scene.userspin = 1                  ##0 means user cannot spin
scene.visible = 1

top = vector(0,0.1,0)              # where top of spring is held

# dimensions of the spring have been altered to make the system easier to observe
Lspring = 0.1                      # relaxed length of spring in metres
Rspring = 0.01                     # radius of spring in metres
Dspring = 0.001                    # thickness of spring wire in metres

Mspring = 0.0085                    # mass of spring in kilograms (ps)
Mbob = 0.1                          # mass of bob in kilograms (p0)
Meffective = Mbob + Mspring/3       # effective mass (pe)

k = 3.45                            # spring constant in N/m
A = 0.05                            # amplitude of motion in metres

support = box(pos=top+vector(0,0.001,0), size=vector(0.040,0.002,0.040), color=color.green)
spring = helix(pos=top, axis=vector(0,-Lspring,0), coils=20, radius=Rspring, thickness=Dspring, length=Lspring, color=vector(1,0.7,0.2))
bob = cylinder(pos = vector(0,0,0), vel = vector(0,0,0), mass = Mbob, axis = vector(0,-0.02,0), radius = 0.008, color = color.red)

# Time step
t = 0                               # elapsed time
t_max = 10                          # seconds
dt = 0.01                           # seconds

# Initial conditions
bob.pos = vector(0,-A,0)
bob.p = Meffective*bob.vel


# Calculations
while t < t_max:
    rate(100)
    t = t + dt
    bob.pos.x = bob.pos.z = 0
    bob.pos.y = bob.pos.y + bob.p.y/Meffective * dt
    bob.p.x = bob.p.z = 0
    bob.p.y = bob.p.y + -k*bob.pos.y * dt
    spring.length = mag(bob.pos - spring.pos)

# Plotting
    VPlot.plot(pos=(t, bob.pos.y))

# Writing to file ... remove the # from the two lines below to enbale writing to file:
#    Fout.write(str("%7.3f" % t) + str("%10.5f" % bob.pos.y)+'\n');

# Fout.close()
