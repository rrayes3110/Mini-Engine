from JustEngine import *


sim = Simulation(400, 800, "Titulooo", True)


ball = Object(20, 20, (200, 200), 2, 0, 0, "yellow", sim, hitBorder=True, circle=True, COR = 1)
ball2 = Object(20, 20, (215, 185), 2, 0, 0, "red", sim, hitBorder=True, circle=True, COR = 1)
ball3 = Object(20, 20, (185, 185), 2, 0, 0, "green", sim, hitBorder=True, circle=True, COR = 1) 
ball4 = Object(20, 20, (200, 170), 2, 0, 0, "blue", sim, hitBorder=True, circle=True, COR = 1)
ball5= Object(20, 20, (230, 170), 2, 0, 0, "black", sim, hitBorder=True, circle=True, COR = 1)
ball6 = Object(20, 20, (170, 170), 2, 0, 0, "orange", sim, hitBorder=True, circle=True, COR = 1)
ball7 = Object(20, 20, (200, 600), 10, 200, 270, "white", sim, hitBorder=True, circle=True, COR = 1)

sim.calculate(20, 0.001)
sim.run(speed=2)
