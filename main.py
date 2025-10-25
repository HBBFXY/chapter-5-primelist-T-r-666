# 在此文件中实现 PrimeList 函数

def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
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
