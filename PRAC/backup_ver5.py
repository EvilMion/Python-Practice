# Импорт нужных библиотек
import zipfile
import time
import os

path = 'C:\\Users\EvilMion\Desktop\pyth1'
os.chdir(path)

file_list = os.listdir(path)

direction_target = 'C:\\Users\EvilMion\Desktop\pyth2'

comment = input('Введите комментарий: ')
if len(comment) == 0:
    file_name = direction_target + time.strftime('%Y%m%d') + '.zip'
else:
    file_name = direction_target + comment.capitalize() + time.strftime('%Y%m%d') + '.zip'

new_zip = zipfile.ZipFile(file_name, 'w')

for i in file_list:
    new_zip.write(i)

new_zip.close()