'''
Created on 10 Nov 2016

@author: Erick
'''

def checkPrime(s, primes):
    for prime in primes:
        if s % prime == 0:
            return False
        
    return True


def isPrime(num):
    primes = []
    
    s = 2
    while s < num:
        result = checkPrime(s, primes);
        if result :
            primes.append(s)
        s = s + 1
    
    isPrime = False;
    
    print("isPrime:" + str(isPrime));
    print("primes" + str(primes));


if __name__ == '__main__':
    isPrime(100);