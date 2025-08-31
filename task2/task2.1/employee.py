#!/usr/bin/env python3

from random import randint

class Employee:
    def __init__(self, name, family, manager=None):
        self._name =name 
        self._id =randint(1000,9999)
        self._family=family.copy()
        self._manager=manager
        self.salary=2500
        
    @property
    def id(self)->int:   
    
     return self._id

    @property
    def family(self)->dict:
        return self._family.copy()
    
    def apply_raise(self,managed_employee:'Employee',raise_percent:int):

       if managed_employee._manager is not self:
           return f"{self._name} is not the manager of {managed_employee._name}"
      
       #apply raise
       managed_employee.salary=managed_employee.salary+managed_employee.salary*(raise_percent/100)
       print(f"new salary is {managed_employee.salary}")
       return True
  
  
##### Test code: #####
if __name__ == '__main__':
    boss = Employee('Jane Redmond', {}) 
    name = 'John Smith'
    family = {
        'Son': {
            'Insured': True,
            'Age': 16
        },
        'Wife': {
            'Insured': False,
            'Age': 32
        }
    } 
    my_employee = Employee(name, family, boss)
    not_boss = Employee('Adam Cater', {})

    # do not change:
    print(id(my_employee.family))
    print(id(my_employee._family))  # should be different
    boss.apply_raise(my_employee, 25)
    print(not_boss.apply_raise(my_employee, 25))


        