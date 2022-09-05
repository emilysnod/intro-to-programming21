# Emily Snodgrass
# 11/18/21

# takes a list of numbers entered by the user and checks if the last
# number entered appears in the list before
data = []
size = 0
entry = float(input("Please enter your values.\n"))
flag = 0
index = 0

if (entry >= 0):
	# create list of values
	while (entry >= 0):
		data.append(entry)
		size = size + 1
		entry = float(input())
	last = data[size-1]

	# check each element in the array and compare with last value
	while (index < size-2):
		# set flag to 1 if values match
		if (data[index] == last):
			flag = 1
		index = index + 1
	print("Does the last number appear before in the list?")

	if (flag == 1):
		print("Yes!")
	else:
		print("No!")
else:
	print("No data")