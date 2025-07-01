
""" A closure is a technique which allows the storing of values in spite of the fact """ 
""" that the context in which they have been created does not exist anymore.         """

def outer(par):
    loc = par

    def inner(value):
        return loc + value
    return inner


var = 1
fun = outer(var)
print(fun(3))

