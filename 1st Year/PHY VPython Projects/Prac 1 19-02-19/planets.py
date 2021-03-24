from vpython import *

sun = sphere(pos=vector(0,0,0), radius=7e9, color=color.yellow)
mercury = sphere(pos=vector(5.8e10,0,0), radius=4e9, color=color.red)
venus = sphere(pos=vector(-1.1e11,0,0), radius=6e9, color=color.orange)
earth = sphere(pos=vector(0,1.5e11,0), radius=6.4e9, color=color.blue)

a1 = arrow(pos=earth.pos, axis=mercury.pos-earth.pos, color=color.white)
a2 = arrow(pos=earth.pos, axis=0.5*(venus.pos-earth.pos), color=color.cyan)

step = 0

deltar = vector(1e9,1e9,0)
while step < 100:
    step += 1
    mercury.pos += deltar
    rate(20)
    a1.axis = mercury.pos-earth.pos
    print(step)
    
print("End of program, step =", step)
