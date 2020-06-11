while True:
    s = input('Введите что-нибудь: ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('Введённая сторка достаточной длины')
print('Завершение')