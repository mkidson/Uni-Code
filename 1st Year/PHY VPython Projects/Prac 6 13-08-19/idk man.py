from vpython import *
graph.autoscale = 20

# constants
oofpez = 9e9
qproton = 1.6e-19
Escale = 0.5e-19
d = 0.5e-9

# objects
plus = sphere(pos=vector(.1e-9,0,0), radius=.3e-10, color=vector(1,0,0), charge=qproton)
minus = sphere(pos=vector(-.1e-9,0,0), radius=.3e-10, color=vector(0,0,1), charge=-qproton)

# initial values
locations = [vector(d,0,0), vector(-d,0,0), vector(d,d,0), vector(-d,-d,0), vector(d,-d,0), vector(-d,d,0), vector(0,d,0), vector(0,-d,0), vector(0,0,d), vector(0,0,-d), vector(0,d,d), vector(0,d,-d), vector(0,-d,d), vector(0,-d,-d)]
    

gg = graph(x=0, y=800, height=300, ymax=10e-19, ymin=-10e-19)
Kgraf = gcurve(color=color.magenta)
Ugraf = gcurve(color=color.green)
Egraf = gcurve(color=color.yellow)

charges = [plus, minus]

for pt in locations:
    E = vector(0,0,0)
    for q in charges:
        r = pt-q.pos
        E += oofpez*(q.charge/mag(r)**2)*norm(r)
    Earrow = arrow(pos=pt, color=color.orange, axis=E*Escale, shaftwidth=0.02e-9)
    
    
proton = sphere(pos=vector(0,0.3e-9,0), radius=.2e-10, color=vector(1,0,0), charge=1.6e-19, m=1.7e-27, p=vector(0,0,0), make_trail=True)

dt = 1e-17
t=0

while t < 1.5e-12:
    rate(1000)
    t+=dt
    E = vector(0,0,0)
    
    U = 0
    for q in charges:
        r = proton.pos - q.pos
        E += oofpez*(q.charge/mag(r)**2)*norm(r)
    
        U += oofpez*q.charge*proton.charge/mag(r)
    
    Ugraf.plot(pos=(t,U))        
        
    F = proton.charge*E
    proton.p += F*dt
    proton.pos += (proton.p/proton.m)*dt
    
    K = mag(proton.p)**2/(2*proton.m)
    Kgraf.plot(pos=(t,K))
    
    E = K + U
    Egraf.plot(pos=(t,E))