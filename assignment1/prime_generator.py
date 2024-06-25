def prime_generator(limit):
   
    for num in range(2, limit):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num


limit = int(input("eneter limit:"))
for prime in prime_generator(limit):
    print(prime)
