# Emily Snodgrass

# find the most frequently occuring number (the mode) in a series of 
# numbers entered by the user
freq = []
index = 0
size = 11

# create a list of length 11 filled with zeros
while(index < size):
	freq.append(0)
	index = index + 1

# count how many times each number appears as data is entered
data = int(input("Input some numbers between 0 and 10\n(enter a negative to stop)\n"))
while (data >= 0 and data < size):
	freq[data] = freq[data] + 1
	data = int(input())

#find the largest frequency (mode)
index = 0
mode = 0
while (index < size):
	if (freq[index] > mode):
		mode = freq[index]
	index = index + 1

# print all numbers with the largest frequency
index = 0
print("Mode(s) =", end=" ")
while (index < size and mode > 0):
	if (freq[index] == mode):
		print(index, end=" ")
	index = index + 1

if (mode == 0):
	print("No data")