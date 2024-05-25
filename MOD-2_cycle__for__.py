
# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"




numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for index in range(1, len(numbers)):  # Начинаем цикл с индекса 1, чтобы пропустить первое число (1)
    is_prime = True                   # если проводить проверку с учетом еденицы, она определяется как True и попадает в первый список.
    for j in range(2, index):         
        if numbers[index] % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(numbers[index])
    else:
        not_primes.append(numbers[index])

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')




