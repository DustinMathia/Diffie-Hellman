from random import randint

def step1(g, n, x = None):
    n = int(n)
    g = int(g)
    if x == None:
        x = randint(1, n-1)
        X = g ^ x % n
    else:
        X = g ^ x % n
    print('\nShare number:\n%s\n' % X)
    step2(x, n)

def step2(x, n):
    Y = input('\nParty 2 number:\n')
    k = int(Y) ^ x % n
    print('\nShared key is:\n\n%s' % k)

def start():
    g = input('\nPrimitive root:\n')
    n = input('\nPrime:\n')
    step1(g, n)

start()