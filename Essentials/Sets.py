# Sets
#A set is a collection which is both unordered and unindexed.
# Removes duplicates.
# Sees if a value is present more fast.
# Set items are unordered, unchangeable, and do not allow duplicate values

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

# shows both existing values in a pair of sets
print(cs_courses.intersection(art_courses)) # prints out History and Math

# shows unique values in a set (left side)
print(cs_courses.difference(art_courses)) # returns physics and compsci

print(art_courses.difference(cs_courses)) # returns design and art

# shows all values in a pair of set
print(cs_courses.union(art_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Declaring lists, tuples, and sets
# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()