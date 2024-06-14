
first = int(input('Введите первое число:'))
second = int(input('Введите второе число:'))
thirt = int(input('Введите третье число:'))
if first == second == thirt:
    print(3)
elif first == second != thirt or first != second == thirt or first == thirt != second:
    print(2)
else:
    print(0)
