print('Просто присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist

del shoplist[0]

print('shoplist', shoplist)
print('mylist', mylist)

print('Копирование при помощи полной вырезки')
mylist = shoplist[:]
del mylist[0]

print('shoplist', shoplist)
print('mylist', mylist)