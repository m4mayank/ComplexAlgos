#!/usr/local/bin/python3.7

def sieve(A):
    if A==1:
        return []
    else:
        primes = [1]*(A+1)
        primes[0] = 0
        primes[1] = 0
        for i in range(2, int((A)**(0.5))+1):
            if primes[i] == 1:
                j = i
                while(i*j <= A):
                    primes[i*j]=0
                    j+=1
        return [i for i in range(0, len(primes)) if primes[i]==1]


def primesum(A):
    llist = sieve(A)
    for i in range(len(llist)-1, -1, -1):
        if (A-llist[i]) in llist:
            return[A-llist[i], llist[i]]

print(primesum(16777214))
