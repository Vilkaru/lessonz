# 3.Элементы кортежа нельзя изменить, потому что кортеж является неизменяемой последовательностью

immutable_var = (1, 'urban', True, 1.2)
print('Immutable tuple: ',immutable_var)
mutable_list = [1, 'urban', True, 1.2]
mutable_list.append('Modified')
print('Mutable list:',mutable_list)