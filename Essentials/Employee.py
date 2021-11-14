# INTRODUCTION TO PYTHON CLASSES
import datetime

class Employee:

    # A variable that is shared by all instances of a class
    #Class variables are defined within a class but outside any of the class's methods.
    # CLASS VARIABLE:
    raise_amount = 1.04

    num_of_employees = 0

    fire_all_employees = False

    #CONSTRUCTOR = TO JAVA
    def __init__(self, firstname, lastname, employee_num, pay):
        # Instances variables  are variables that are different from each instance.
        # For example, the names and the pay for each employee. They have to be different.
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.employee_num = employee_num
        self.pay = pay
        self.email = f"{self.firstname}.{self.lastname}@gmail.com"

        Employee.num_of_employees += 1
        #We choose the class name (Employee) instead of (self.num_of_employees) to not allow
        #the instances of this to class to affect this variable.
        #Gives the same value regardless of any instance.

    def introduce_self(self):
        return f"I am {self.firstname} {self.lastname} and my employee number is {self.employee_num}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod # affects all instances' raise amount.
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string): # alternate constructor
        firstname, lastname, employee_num, pay = string.split('-')
        email = f'{firstname}.{lastname}@gmail.com'
        return cls(firstname, lastname, employee_num, pay)

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True

    @classmethod
    def fire_all(cls):
        cls.fire_all_employees = True
        cls.num_of_employees = 0


# emp1 and emp2 are instances of the Employee class.
emp1 = Employee("nikho", "remulla", 1000, 60000)
emp2 = Employee("adam", "apples", 1005, 100000)

#alternate arguments for Employee class.
# employee_string = "Adam-Walker-1100-70000"
# emp3 = Employee.from_string(employee_string)
# print(emp3.introduce_self())
# print(emp3.email)

Employee.fire_all()
print(f'Am I fired? {emp1.fire_all_employees}')
print(f'Am I fired? {emp2.fire_all_employees}')




# calling a method/function
print(emp1.introduce_self())
# SAME AS:
print(Employee.introduce_self(emp1))

# calling the apply_raise method
print(f"\nMy pay before apply_raise method: {emp1.pay}")
emp1.apply_raise()
print(f"My pay after apply_raise method: {emp1.pay}")

# affects all instances' raise amount.
Employee.set_raise_amount(1.06)
print(f"\nEmployee 1 Raise Amount: {emp1.raise_amount}")
print(f"Employee 2 Raise Amount: {emp2.raise_amount}")

# change the raise amount individually per instance of the Employee class.
emp1.raise_amount = 1.09
print(f"\nEmployee 1 Raise Amount: {emp1.raise_amount}")
print(f"Employee 2 Raise Amount: {emp2.raise_amount}")

# another example of using class variables.
print(f"\nCurrent amount of employees: {Employee.num_of_employees}")

# static method here:
date_argument = datetime.date(2021, 11, 14)
print(Employee.is_work_day(date_argument))

print('-------------')