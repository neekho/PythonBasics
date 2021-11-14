# Working numbers in Python.
# +	 Addition	     x + y
# -	 Subtraction	 x - y
# *	 Multiplication	 x * y
# /	 Division	     x / y
# %	 Modulus	     x % y
# ** Exponentiation	 x ** y
# // Floor division	 x // y
my_int = 3
pi = 3.14

print(type(my_int))
print(type(pi))

# % modulus operator - returns the remainder in a dividing
print(2 % 2) # returns 0
print(4 % 3) # 4 / 3 = 1.333 : so return 1

# ** exponentation operator
# multiplies the first number by the second number
print(2 ** 4) # returns 16
print(3 ** 3) # returns 27

# // floor division operator
print(4 / 3) # returns 1.3
print(4 //3) # returns 1

# built-in methods for int
print(abs(-5))

#round up/down a float to its nearest decimal point
print(round(3.65))


# determine if an int is even or odd
input_number = int(input("Enter Number: "))

if input_number % 2 == 0:
     print(f"{input_number} is even an even number")

elif input_number % 2 != 0:
     print(f"{input_number} is an odd number")