# Code for proving Robin's theorum for a suitable range of natural numbers 

from math import log
import numpy as np
import matplotlib.pyplot as plt


def factorize(n, primes):
    factors = []
    for p in primes:
        if p*p > n: break
        i = 0
        while n % p == 0:
            n //= p
            i+=1
        if i > 0:
            factors.append((p, i));
    if n > 1: factors.append((n, 1))
    
    return factors


def divisors(factors):
    div = [1]
    for (p, r) in factors:
        div = [d * p**e for d in div for e in range(r + 1)]
    return div


def list_to_number(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

gamma = float(0.57721566490153286060651209008240243104215933593992)

secVal = list(); sig = list()
pwData = float(pow(1e+1, gamma))

n = 2
numList = list()
while n < 10000:
    secVal.append(pwData*n*log(log(n)))
    sig.append(sum(divisors(factorize(n, list_to_number(n)))))
    n = n + 1
    numList.append(n)

plt.plot(numList, secVal, label="e^y*n*lnln(n)")
plt.plot(numList, sig, label="Sigma(n)")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)


plt.savefig('fig.png')


