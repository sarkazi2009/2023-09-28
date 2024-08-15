first = (input('Введите число: '))
second = (input('Еще одно: '))
third = (input('Третье пожалуйста: '))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second or first != third or second != third:
    print(0)






