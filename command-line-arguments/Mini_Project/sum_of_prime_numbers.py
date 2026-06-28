import sys

if len(sys.argv) != 11:
    print("Usage: python script.py <10 numbers>")
else:
    sum = 0

    for i in range(1, 11):
        num = int(sys.argv[i])

        if num > 1:
            prime = True

            for j in range(2, num):
                if num % j == 0:
                    prime = False
                    break

            if prime:
                sum += num

    print("Sum of prime numbers:", sum)