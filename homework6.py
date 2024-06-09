# Работа с словарём
my_dict = {'Robert': 1999, 'Ravil': 2004, 'Kira': 2006}
print('Dict:',my_dict)
print('Existing value:', my_dict['Ravil'])
print('Not existing value:',my_dict.get('Oxsana'))
my_dict.update({'Oxsana': 1976,
                'Rustam': 1976})
a = my_dict.pop('Ravil')
print('Deleted value:',a)
print('Modified dictionary: ',my_dict)
# Работа с множеством
my_set = {1, 'beginer', 4.1}
print('Set:', my_set)
my_set.add(13)
my_set.add((1, 2, 3))
my_set.discard(1)
print('Modifical set:', my_set)
