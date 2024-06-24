
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primers = []
is_prime = True
for i in range(numbers[1], numbers[14] + 1):
    k = 0  # счётчик делителей
    for j in range(numbers[0], i+1):
        if i % j == 0:
            k += 1
        if k == 2:
            is_prime = True
        else:
            is_prime = False
    if is_prime:
        primes.append(i)
    else:
        not_primers.append(i)
print('Primers:', primes)
print('Not primers', not_primers)









