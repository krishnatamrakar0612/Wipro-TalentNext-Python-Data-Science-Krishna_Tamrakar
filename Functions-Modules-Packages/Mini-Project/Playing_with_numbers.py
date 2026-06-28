# Program to check whether a given number is prime or not.

def is_prime(number):
    if number <= 1:
        print("Not Prime")
        return

    for i in range(2, number):
        if number % i == 0:
            print("Not Prime")
            return

    print("Prime")


number = int(input("Enter a number: "))
is_prime(number)