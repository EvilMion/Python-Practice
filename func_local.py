def function_outer():
    x = 2
    print('X =', x)

    def function_inner():
        nonlocal x
        x = 5

    function_inner()
    print('Локальное X сменилось на ', x)

function_outer()