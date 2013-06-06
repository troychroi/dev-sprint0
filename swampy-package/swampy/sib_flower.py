# Flower excercise (4.2) from Week 0

# Name:


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				
bob.delay = 0.01 

import math

def polyline(turtle, n, l, angle):
	for i in range(n):
		fd(turtle, l)
		lt(turtle, angle)

def arc(turtle, r, angle):
	arc_length = 2 * math.pi * r * abs(angle) / 360
	n = int(arc_length / 4) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	lt(turtle, step_angle/2)
	polyline(turtle, n, step_length, step_angle)
	rt(turtle, step_angle/2)

def petal(turtle, r, angle):
	for i in range(2):
		arc(turtle, r, angle)
		lt(turtle, 180-angle)

def flower(turtle, n, r, angle):
	for i in range(n):
		petal(turtle, r, angle)
		lt(turtle, 360.00/n)
def move(turtle, l):
	pu(turtle)
	fd(turtle, l)
	pd(turtle)

move(bob, 100)
flower(bob, 20, 140.00, 20.00)




# This is where you put code to move bob



wait_for_user()					

