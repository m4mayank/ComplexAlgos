#!/usr/local/bin/python3.7

#Example:
#    if N = 7,
#    all primes till 7 = {2, 3, 5, 7}
#    Make sure the returned array is sorted.

def sieve(A):
    if A==1:
        return []
    else:
        primes = [1]*(A+1)
        primes[0] = 0
        primes[1] = 0
        for i in range(2, int((A)**(0.5))+1):
            if primes[i] == 1:
                j = 2
                while(i*j <= A):
                    primes[i*j]=0
                    j+=1
        return [i for i in range(0, len(primes)) if primes[i]==1]

print(sieve(10))

