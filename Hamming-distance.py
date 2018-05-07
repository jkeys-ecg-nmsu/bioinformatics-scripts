import sys

#ensure sufficient arguments
if (len(sys.argv) < 3): 
	print("give some valid arguments pliz")

#open the files
f1 = open(str(sys.argv[1]), 'r')
f2 = open(str(sys.argv[2]), 'r')

#convert the inputs to eliminate alphabetal case problem
str1 = (f1.read()).upper()	 
str2 = (f2.read()).upper()

#ensure valid inputs
if (len(str1) != len(str2)):
	print("Hamming Distance requires equal length string inputs, exiting...")
	sys.exit()

numMismatch = 0

for c1, c2 in zip(str1, str2):
	if c1 != c2:
		numMismatch += 1

print("hamming distance: " + str(numMismatch))