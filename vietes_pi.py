# Emily Snodgrass
# 10/20/21

import math

# this program uses Viete's pi formula to estimate pi to the chosen number of factors
# input - let user provide number of factors in the calculation
# output - aproximate value of pi

max = float(input("How many factors should be used to calculate pi?\n"))

count = 1
vp = 1
rt2 = 0

while (count <= max):
	vp = ((math.sqrt(2 + rt2)) / 2) * vp
	count = count + 1
	rt2 = math.sqrt(2 + rt2)
print("Pi calculated to", count - 1, "factor(s) of Viete's pi formula is", 2/vp)