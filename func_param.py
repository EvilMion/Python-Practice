x = 50

def function(x):
    print('x равен', x)
    x = 2
    print('Замена локального x на ', x)

function(x)
print('x по-прежнему', x)