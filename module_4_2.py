def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    return inner_function()

test_function()
#inner_function - функция не вызывается, так как является объемлющим пространсвом имён






            



    















