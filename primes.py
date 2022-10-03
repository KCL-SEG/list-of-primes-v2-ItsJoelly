"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    try:
        list = []
        counter = 2
        while number_of_primes != len(list):
            if checkPrime(counter):
                list.append(counter)
            counter +=1
        return list
    except ValueError as ve:
        print("The value you entered is not a positive number!")

def checkPrime(num):
    if num == 2:
        return True
    else:
        for i in range(2,num):
            if (num%i == 0):
                return False
    return True
