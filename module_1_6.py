my_dict = {'Ivan': 1971, 'Oksana': 1985, 'Vlad': 1999}
print(my_dict)
print(my_dict['Vlad'])
print(my_dict.get('Liza'))
my_dict.update({'Svetlana': 2003, 'Alex': 1996})
print (my_dict)
a = my_dict.pop('Oksana')
print(a)
print(my_dict)

print(" \n ")

my_set = {1, 2, 3, 3, 'Forest', 'Sun', 1.5, 13.9, 'Sun', 1}
print(my_set)
my_set.update([False, (1, 2, 2, 3)])
print(my_set)
my_set.remove('Forest')
print(my_set)
my_set.discard(4)
print(my_set)
