def main():
	n = int(input("Enter the number of desired branches:"))

	for x in range(n):

		print((" " * (n - x)),('#' * (2*x+1)))

	print(n*" ", "#")
	
	main()
	