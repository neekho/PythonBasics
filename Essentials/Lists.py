# -------------------START.         LISTS       -------------------------------

# Declaring a list
transportation = ["bike", "car", "jeep"]

# Accessing an element.
print("Element at index[1]: " + transportation[1])

# Modifying an element.
transportation[1] = "airplane"
print("Element at index[1] after modification: " + transportation[1])

# APPENEDING or ADDING to a list dynamically
socialMedias = []
socialMedias.append("Facebook")
socialMedias.append("Instagram")
socialMedias.append("Twiter")

# START OF REMOVING ELEMEMTS

# REMOVING ELEMENT to a list using del keywowrd

print("\n\ndel keyword demo:" + "\n" + str(socialMedias))
print("AFTER USING del keyword:")
del socialMedias[0]
print(socialMedias)

# END OF del keyword

# REMOVING an item using the pop() method
# In a web application, you might want to
#remove a user from a list of active members
# and then add that user to a list of inactive members.
# The pop() method removes the last item in a list,
# but it lets you work with that item after removing it.

marleyWarriors = ["Annie", "Bertholdt", "Reiner", "Marcel"]

print("\nusing pop() method:\n" + str(marleyWarriors))

deadMarleyWarrior = marleyWarriors.pop(3)
print(marleyWarriors)
print(f"Rest in Peace: {deadMarleyWarrior}")

# END OF pop() method

# REMOVING an Item by Value
brandCars = ["audi", "honda", "tesla", "ferrari"]

print("\n\nremove() method: " + "\n" + str(brandCars))

unavailable_brand = "tesla"
brandCars.remove(unavailable_brand)

print(brandCars)
print(f"A {unavailable_brand} is currently unavailable to my country.")

# END OF remove() method
# END OF REMOVING ELEMENTS


# START OF SORTING LISTS

# sort() METHOD:

fruits = ["mango", "avocado", "apple", "durian", "orange", "banana"]
print("\n\nFruit list before sort(): " + str(fruits))
fruits.sort()
# The sort() method, shown at you, changes the order of the list permanently.
print("Fruit list after sort(): " + str(fruits))

random_numbers = [4, 2, 5, 1, 3]

# ascending order.
random_numbers.sort()
print(random_numbers)

# descending order.
random_numbers.sort(reverse=True)
print(random_numbers)

# end of sort() method.


# sorted() METHOD:
# for temporary sorting use sorted() instead of sort() method.
carCompanies = ["toyota", "tesla", "lambo", "audi", "ferrari", "bmw"]

print("\n\nHere is the original list: " + str(carCompanies))
print("Here is the sorted list: " + str(sorted(carCompanies)))
print("Here is the original list again: " + str(carCompanies))

# end of sorted() method


# LIST REVERSAL
# The reverse() method changes the order of a list permanently,
# but you can revert to the original order anytime by applying reverse() to the same list a second time.
# Using reverse():

grades = [85, 90, 96, 88]

print("\n\nGrade list before reverse(): " + str(grades))

grades.reverse()
print("Grade list after reverse(): " + str(grades))

# END OF LIST REVERSAL
# END OF SORTING LISTS

# START OF CHECKING OF VALUES or INDEX IN A LIST
subjects = ["Science", "Arts", "Math"]

# using in keyword, returns true/false
print("\n")
print("Programming" in subjects) # returns false

# using .index() to find the passed argument's index.
print(subjects.index("Science")) # returns 0

# --------------------------------WORKING WITH LISTS-------------------------------------
# LOOPING THROUGH A LIST

touristSpots = ["tagaytay", "baguio", "vigan"]

print("\n\nLooping through a list:")
for places in touristSpots:
    print(places.title() + ", PH")
print("Awesome places !")  # Outside of indentation

# print a list with its indexes and matching values:
print("index value")
for index, places in enumerate(touristSpots):
    print(index, places)
print("end of loop.")
# END OF LOOPING THROUGH LISTS

# assigning a list to a string variable.
touristSpots_str = ", ".join(touristSpots)
print(f"\n\n{touristSpots_str}")

DELIMITER = "."
print(DELIMITER.join(touristSpots).upper())