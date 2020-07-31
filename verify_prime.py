#!/usr/local/bin/python3.7


def isPrime(A):
    prime_flag = True
    for i in range(2, int((A)**(0.5)+1)):
        if A%i == 0:
            prime_flag=False
            break
    if A==1:
        return 0
    else:
        return prime_flag

print(isPrime(11))
