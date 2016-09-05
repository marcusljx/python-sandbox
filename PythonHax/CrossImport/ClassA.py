""" Sandbox :: ClassA

Description:
    Solution for problem at http://stackoverflow.com/questions/8980676/dynamically-bind-method-to-class-instance-in-python

Author:
    marcusljx

Created:
    2016-09-01

Doctests:
>>> A = ClassA()
>>> print(A.calling_method())
3
"""

class ClassA(object):
    def __init__(self):
        super(ClassA, self).__init__()

        self.a = 1
        self.b = 2

    from PythonHax.CrossImport.moduleB import meth2 as meth1

    def calling_method(self):
        return self.meth1()
