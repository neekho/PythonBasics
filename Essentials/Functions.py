# Functions and Parameters in Python.
def add_numbers(a, b):
    return a + b


def add_numbers2(*numbers):

    sum = 0
    for num in numbers:
        sum+= num
    print(sum)

# Difference between the two methods.

print(add_numbers(5, 10))
add_numbers2(5, 2, 3)



#aweae