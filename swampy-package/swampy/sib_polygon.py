# Polygon excercise from Week 0

# Name:


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

def polygon(turtle, l, n):
		for i in range(n):
			fd(turtle, l)
			rt(turtle, 360/n)
#polygon(bob, 50, 8)
 
def circle(turtle, l, n):
	for i in range(n):
		fd(turtle, l/n)
		rt(turtle, 360/n)
#circle(bob, 100, 50)

def arc(turtle, l, n, theta):
	for i in range(n*theta/360):
		fd(turtle, l/n)
		rt(turtle, 360/n)
arc(bob, 100, 50, 90)





	











wait_for_user()					
