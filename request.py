import sys
from random import randrange

# generates X random numbers between 1 and 10
# and returns the sum
def main():
	x = int(sys.argv[1])
	sum = 0
	for i in range(0,x):
		sum = sum + randrange(1,10)
	return sum
	
if __name__ == '__main__':
	print main()