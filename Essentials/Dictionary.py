# HashMap equivalent to Java
# Key : Value pairs.
# 'Philippines': 'Manila' etc
# Values can be any object

#empty dict

empty_dict = {}
print(type(empty_dict)) #<class 'dict'> belongs to dict class.

# sample dictionary
sample_dictionary = {

    'name': 'Mittens',
    'age': 5,
    'is_alien': False,
    'colors': ['White', 'Brown', 'Black']
}

# NESTED Dictionary
employees = {

   'employee_one': {
       'name': 'Nikho',
       'age': 21,
       'languages': ['C', 'Python']
   },
   'employee_two': {
       'name': 'Chris',
       'age': 24,
       'languages': ['Java', 'C++']
   }
  
}

for employee_num, employee_info in employees.items():

    employee_name = employee_info['name']
    employee_age = employee_info['age']
    employee_language = employee_info['languages']

    print(employee_num, employee_name, employee_age, end='')

    for languages in employee_info['languages']:
        print(languages)