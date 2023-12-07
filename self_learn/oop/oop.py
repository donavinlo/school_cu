# Python Object Oriented Programming

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    #Creating a method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee("Donavin", "ODay", 70000)
emp_2 = Employee("Linda", "ODay", 20000)


print(emp_1.fullname())
