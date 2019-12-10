def find_modulo(aList, n=2, divisible=True):
    # Find and print all numbers in aList which divisible by n
    for x in aList:
        if divisible:
            if x % n == 0:
                print(x, end=' ')
        else:
            if x % n != 0:
                print(x, end=' ')
    print()

aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
find_modulo(aList) #Print all evens

find_modulo(aList, n=3) #print all numbers divisible by 3

find_modulo(aList, n=3, divisible=False)    #print all numbers not divisible by 3

find_modulo(aList, divisible=False) #print all odds

