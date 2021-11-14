#Lists are mutables, while tuples are immutable.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.
# When we say that tuples are ordered,
# it means that the items have a defined order, and that order will not change.


# Lists for modifaction
# Tuples for looping, accessing and just storing.


#Mutable List
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)


#Immutable Tuple
#tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
#tuple_2 = tuple_1

#print(tuple_1)
#print(tuple_2)

#tuple_1[0] = 'Art'

#print(tuple_1)
#print(tuple_2)

# Declaring lists, tuples, and sets
# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()