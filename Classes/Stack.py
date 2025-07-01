
""" Stack.py """
""" Manage stack as internal list """

class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        self.__stack = []

    def push(self, new_elem):
        self.__stack.append(new_elem)

    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val

""" Inheritied from the class Stack """

class StackWithSum(Stack):
    def __init__(self):
        super().__init__() # or Stack.__init__(self)
        self.__sum = 0

    def push(self, new_elem):
        super().push(new_elem) # or Stack.push(self, new_elem)
        self.__sum += new_elem

    def pop(self):
        val = super().pop() # or Stack.pop(self)
        self.__sum -= val
        return val

    def getSum(self):
        return self.__sum

""" isInstance """
stack1 = Stack()
stack2 = StackWithSum()     
print(isinstance(stack1, Stack))
print(isinstance(stack1, StackWithSum))
print(isinstance(stack2, Stack))
print(issubclass(StackWithSum, Stack))

print(isinstance(stack1, Stack))

""" is """
stack3 = stack2
print(stack3 is stack2)

string_1 = "Mary had a little lamb"
string_2 = "Mary had a little lamb"
string_3 = "Mary had a little "
string_3 += "lamb"
print(string_1 == string_2, string_1 is string_2, string_1 is string_3)



class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " says: Woof!"


class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " Don't run away, Little Lamb!"


class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " Stay where you are, Mister Intruder!"

class LowlandDog(SheepDog):
    def __str__(self):
        return Dog.__str__(self) + " I don't like mountains!"

rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")
