n = int(input("Please put in a positive number: "))


def number(n): 
    counter = 0
    for i in range (1, n + 1):
        result =  getPowerOfTen(i)
        print(i, result)
        counter += result
    return counter

def getPowerOfTen(n): 
    number = 0
    while n > 0:
        n = int(n / 10)
        number = number +1
    return number

print(number(n))