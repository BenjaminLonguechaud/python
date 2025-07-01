
''' Introspection, which is the ability of a program to examine the
    type or properties of an object at runtime; '''
''' Reflection, which goes a step further, and is the ability of a
    program to manipulate the values, properties and/or functions of an object at runtime.'''

class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)