from vpython import *

cricketball = sphere(pos=vector(5,6,2), radius=0.20, color=color.white)
tennisball = sphere(pos=vector(-3,-1,3.5), radius=0.15, color=color.green)

bt = arrow(pos=cricketball.pos, axis=tennisball.pos-cricketball.pos, color=color.red)

