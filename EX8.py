def somme_varargs(*args):
    return sum(args)

test1 = somme_varargs(1, 2, 3, 4, 5)
test2 = somme_varargs(15.1, 18.5, 28.7)
print("Somme 1 :", test1)
print("Somme 2 :", test2)