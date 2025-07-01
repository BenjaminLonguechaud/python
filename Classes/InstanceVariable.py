class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val    # Is _ExampleClass__first

    def set_second(self, val):
        self.__second = val   # Is _ExampleClass__second


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5  # Is __third

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

print(example_object_1._ExampleClass__first)
print(example_object_3.__third)
