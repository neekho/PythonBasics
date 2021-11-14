#Strings in Python

#can use single quotes
my_message = "Hello Python"

#can use doubles qoutes instead of single quotes or just use ""
single_quotes = 'Nikho\'s Reviewer in Python'

print("Hello Python")
print(my_message + " from variable.") # concat strings.

# some string methods:
# turns the message to all lower case.
print("\n" + my_message.lower())

# count() searches for the passed argument in a string and returns it as an int.
print("\n" + str(my_message.count("Python"))) # returns 1

#modifying a string message using replace()
replaced_msg = my_message.replace("Python", "Java")
# also can be my_message = my_message.replace("Python", "Java")
print("\n" + replaced_msg)

# using format.()  as an alternate to + concat
greet_message = "\n{}, and {} is awesome".format(my_message, single_quotes)
print(greet_message)

# f string also as an alternate
greet_message = f"{my_message}, and {single_quotes} is awesome"
print(greet_message)

#printing the length of a string using len()
print("\n" + str(len(my_message)))
print(len("len"))

#accessing indivual characters in a string via slicing:
print("\n" + str(my_message[0:5])) # prints out "Hello"
print(my_message[5:]) # prints out "Python"

# learn more about string methods using help(str)
print(help(str))