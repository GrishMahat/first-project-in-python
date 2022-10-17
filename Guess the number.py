#this is my fist python Project

import random

r = random.randint(0,25)
w = True

print(r)
while w:
	d = int(input("enter number 0 to 25:  "))
	if r == d:
		print("you win") 
		w = False
		
	elif d > 25:
		print("too greater num")
		

	elif r < d:
		print("greater")
		
	elif r > d:
		print("less")
	
	
	
	
