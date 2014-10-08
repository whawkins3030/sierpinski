#!/usr/bin/env python3

# Oct 7 2014
# Prints the mod2 version of Pascal's triangle a.k.a. Sierpinski's triangle.
# Accepts multiple command line args in bash-- eg: "python3 pascal.py 5 10 20"

import sys

def printPascal(n):
	row = [1]
	printRow(row, n)
	for x in range(n-1):
		row = getNewRow(row)
		printRow(row, n)

def getNewRow(prevRow):
	return [prevRow[0]] + [(prevRow[i] + prevRow[i+1])%2 for i in range(len(prevRow)-1)] + [prevRow[-1]]

def printRow(row, n):
	r = ' '.join(str(elem) for elem in row)
	line = ' '*(((2*n+1)-len(r))//2) + r + ' '*(((2*n+1)-len(r))//2)
	print(line)

def main():
	for i in range(1,len(sys.argv)):
		printPascal(eval(sys.argv[i]))

main()