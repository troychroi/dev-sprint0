# Polygon excercise from Week 0

# Name:


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				
bob.delay = 0.01
ray = Turtle()
jay = Turtle()

# This is where you put code to move bob

def polygon(turtle, l, n):
		for i in range(n):
			fd(turtle, l)
			rt(turtle, 360/n)
polygon(ray, 50, 8)
 
def circle(turtle, l, n):
	for i in range(n):
		fd(turtle, l/n)
		rt(turtle, 360/n)
circle(jay, 200, 100)

def arc(turtle, l, n, theta):
	for i in range(n*theta/360):
		fd(turtle, l/n)
		rt(turtle, 360/n)
arc(bob, 100, 50, 90)





	











wait_for_user()					
