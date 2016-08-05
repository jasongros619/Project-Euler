import time
start=time.clock()


#returns list of primes <= limit
def primeSieve(limit):
    if limit < 2: return []
    if limit < 3: return [2]
    size = (limit - 3) // 2
    sieve = [True] * (size + 1)


    maxint=int(limit**0.5)
    for i in range( (maxint - 1) // 2 ):
        if sieve[i]:
            prime = 2 * i + 3
            start = prime * (i + 1) + i
            sieve[start::prime] = [False] * ((size - start) // prime + 1)
    return [2] + [2 * i + 3 for i, v in enumerate(sieve) if v]

#primality check for n < 3,215,031,751
def miller_rabin(n):
    if n in [2,3,5,7]:
        return True
    if not n % 2 or n==1:
        return False
    
    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for a in [2,3,5,7]:
        if not check(a, s, d, n):
            return False
    return True

#checks prime1 with every prime in *arr if the primes
#concatenated with prime1 in both orders is prime
def check(prime1,*arr):
    for prime in arr:
        concat1 = int( str(prime1) + str(prime) )
        concat2 = int( str(prime) + str(prime1) )
        if not(miller_rabin(concat1) and miller_rabin(concat2)):
            return False
    return True
    

#All primes(but 3) in an answer must be the same mod 3
#Any two primes, p1 and p2 in the answer (excluding 11) must follow the
#property: (p1 + p2) and (p1 - p2) are not mutliples of 11

#Now to seperate all primes by prime%3 and prime%11
#where seperate[a][b] = list of all primes such that
#p %  3 == a + 1
#p % 11 == b + 1
seperate = [ [[],[],[],[],[]], [[],[],[],[],[]] ]
for prime in primeSieve(30000):
    a = prime % 3
    b = prime % 11
    b = 11 - b if b > 5 else b
    seperate[a-1][b-1].append( prime )

#Do a depth first search
#looking for a group of 5 that will work
def findAnswer():
    for mod3 in seperate:
        # mod3 is primes(not 3) with the same value mod 3
        # it is divided into lists of values mod 11
        for prime1 in mod3[0]:
            for prime2 in mod3[1]:
                if check(prime1, prime2):
                    for prime3 in mod3[2]:
                        if check(prime3,prime1,prime2):
                            for prime4 in mod3[3]:
                                if check(prime4,prime1,prime2,prime3):
                                    for prime5 in mod3[4]:
                                        if check(prime5,prime1,prime2,prime3,prime4):
                                            return (prime5,prime1,prime2,prime3,prime4)
ans = findAnswer()
print(sum(ans),time.clock()-start)

