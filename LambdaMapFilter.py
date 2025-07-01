
# lambdas should not be assigned to variables
def two() : return 2
twol = lambda : 2
def sqr(x) :  return x * x
sqrl = lambda a : a * a
def pwr(x, y) : return x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))


def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)


""" Map function """
inputList = [x for x in range(5)]
outputList = map(lambda x: 2**x, inputList)
for x in outputList:
    print(x, end=" ")
print(x, end="\n")

""" Filter function """
example_list = filter(lambda x: x > 2, [x for x in range(5)])
for x in example_list:
    print(x, end=" ")
print()

short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)