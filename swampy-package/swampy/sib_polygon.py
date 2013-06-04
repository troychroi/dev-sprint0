# Polygon excercise from Week 0

# Name:

from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()	
ray = Turtle()
jay = Turtle()			
bob.delay = 0.01
ray.delay = 0.01
jay.delay = 0.01


# This is where you put code to move bob

def curve(turtle, l, n):
	fd(turtle, l/n)
	rt(turtle, 360.00/n)


def polygon(turtle, l, n):
		for i in range(n):
			fd(turtle, l)
			rt(turtle, 360.00/n)
polygon(ray, 50, 8)
 
def circle(turtle, l, n):
	for i in range(n):
		curve(turtle, l, n)
circle(jay, 600, 300)


def arc(turtle, l, n, theta):
	for i in range(n*theta/360):
		curve(turtle, l, n)
arc(bob, 100, 50, 180)





	











wait_for_user()					
