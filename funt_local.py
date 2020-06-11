x = 50

def function():
    global x
    
    print('x = ', x)
    x = 2 
    print('Заменяем глобальное значение x на ', x)

function()
print('Значеине x состовляет', x)