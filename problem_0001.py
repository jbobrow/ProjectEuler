# Project Euler - Problem 1
#
# by Jonathan Bobrow
# March 19, 2015

sum = 0

for x in range(1, 1000):
	if (x % 3 == 0) or (x % 5 == 0):
		sum += x

print(sum)
