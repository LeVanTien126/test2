import numpy as np
def mutable_fun(str,intval, tup, mylist, myarr):

    str = 'hello'
    intval = 10
    tup = (3, 5)
    mylist[0] = 100
    myarr[0] = 5

s = 'World'
a = 100
t = (3, 4, 5)
li = [2, 3, 'a']
arr = np.array([0, 1, 2])
#call function
mutable_fun(s ,a, t, li, arr)
print(s, a, t, li,arr, sep='\n')

def inverse(*numbers):
    print('Original numbers: ', numbers, end='\n')
    print('Reverse numbers: ')
    for n in numbers:
        n = 1/n
        print(n, end='')
        print()
    x =5
    inverse(x)

    inverse(x, 10.0, 7.0, np.array([1.0, 2.0, 3.0]))

def find_superior(li, compare):
    sup = li[0]
    for n in li:
        if (compare(n,sup)):
            sup = n
    return sup
def less_than(a, b):
    return a < b

def greater_than(a, b):
    return a > b
