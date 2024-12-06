def linear_sieve(n):
    # `is_prime` arrayini yaradın, əvvəlcə hamısını True olaraq təyin edin
    is_prime = [True] * (n + 1)
    primes = []  # Asalları saxlamaq üçün siyahı
    
    # 0 və 1 asallar deyil, onlar False olaraq təyin edilir
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, n + 1):
        if is_prime[i]:  # Əgər i asal saydırsa
            primes.append(i)
        # i sayının çoxluqlarını False edirik, yalnız asallarla işləyirik
        for p in primes:
            if i * p > n: 
                break
            is_prime[i * p] = False
            if i % p == 0:  # Bu halda, daha böyük çoxluqları keçirik
                break
    return primes

# Nümunə istifadəsi:
n = 30
primes = linear_sieve(n)
print(f"Asallar: {primes}")
