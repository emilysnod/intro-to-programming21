# Emily Snodgrass
# CS161

#print the largest number in a series of entries or "no data" if no data was entered

largest = 0
totalEntries = 0
entryValue = float(input())

while (entryValue != -1): # keep allowing entries until -1 is entered
	if (entryValue > largest): # compare numbers
		largest = entryValue # remember largest
	
	totalEntries = totalEntries + 1 # increment total number of entries

	entryValue = float(input()) # get another data point

if(totalEntries == 0):
	print("No Data")
else:
	print("The Largest number entered is", largest)