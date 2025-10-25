# 在此文件中实现 PrimeList 函数
   import math

def PrimeList(N):
    primes = []
    for i in range(2, N):
        is_prime = True
        sqrt_i = int(math.sqrt(i)) + 1
        for j in range(2, sqrt_i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(i))
    return ' '.join(primes) 
