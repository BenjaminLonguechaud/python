
def Fibo(n):
    f1 = f2 = 1
    for i in range(n):
        if i in [0,1]:
            yield 1
        else:
            n = f1 + f2
            f1, f2 = f2, n
            yield n


fiboList = list(Fibo(10))
print(fiboList)


""" List comprehension"""
list10 = [10 ** ex for ex in range(6)]
print(list10)

""" Generator, not a list because of () """
listBin = (1 if ex % 2 == 0 else 0 for ex in range(10))
for i in listBin:
    print(i, end=" ")
# print(listBin)   Can't work
