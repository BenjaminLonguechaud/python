class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1

class ExampleClassPrivate:
    # Class vaviable
    __counter = 0
    publicVariable = ""
    def __init__(self, val = 1):
        # Local variable
        increment = 1
        # Instance variable
        self.__first = val
        self.publicVariable = "Public Variable"
        ExampleClassPrivate.__counter += increment
        if val == 2:
            # Public variable
            self.second = val

    # Private method
    def __privateReset(self, resetValue = 0):
        self.__first = resetValue

    # Public methods
    def getFirst(self):
        self.__privateReset()
        return self.__first
    
    def getSecond(self):
        return self.second


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

example_object_4 = ExampleClassPrivate()
example_object_5 = ExampleClassPrivate(2)
example_object_6 = ExampleClassPrivate(4)
print(example_object_6.getFirst())
print(example_object_6.publicVariable)
print(example_object_5.getSecond())

print("dict: ", ExampleClass.__dict__)
print("name: ", ExampleClass.__name__)
print("module: ", ExampleClass.__module__)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

print(example_object_4.__dict__, example_object_4._ExampleClassPrivate__counter)
print(example_object_5.__dict__, example_object_5._ExampleClassPrivate__counter)
print(example_object_6.__dict__, example_object_6._ExampleClassPrivate__counter)

if hasattr(example_object_4, 'second'):     # Check Instance variable
    print("example_object_4.second exists")
if hasattr(example_object_5, 'second'):
    print("example_object_5.second exists")
if hasattr(ExampleClass, 'counter'):     # Check Class variable
    print("ExampleClass.counter exists")
if hasattr(ExampleClassPrivate, '_ExampleClassPrivate__counter'):     
    print("_ExampleClassPrivate__counter exists")
