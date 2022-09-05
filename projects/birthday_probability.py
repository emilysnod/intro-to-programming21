# Emily Snodgrass
# What is the probability that in a classroom of x people, at least 2 will be born on the same day of the year (ignore leap year)?
# In a classroom of only 23 people, the probability is about 50.7%  !

import math
import random

# create and initialize frequency table:
ft = []
k = 0
while(k < 365) :
	ft.append(0)
	k = k + 1

# Allow the user to determine class size:
print("Please type in how many people are in the class: ")
x = int(input())

success = 0

# Simulate:
c = 0
while(c < 10000):
  
	# Step 1:  re-initialize birthday frequency table
	k = 0
	while(k < 365):
		ft[k] = 0
		k = k + 1

	# Step 2:  randomly get x birthdays and update frequency table:
	k = 0
	while(k < x):
		bday = math.floor(365 * random.random())
		ft[bday] = ft[bday] + 1
		#print("bday is", bday)
		k = k + 1

	# Step 3: Check to see if this class has at least two people with same
	# b-day and update success appropriately
	k = 0
	flag = 0
	while(k < 365):
		if(ft[k] > 1):
			flag = 1
		k = k + 1

	if(flag == 1):
		success = success + 1
	c = c + 1
	#print(ft)

print("The probability that in a class of ", end="")
print(x , end="")
print(" people, at least two have the same birthday is %" , end="")
print((success/10000)*100)