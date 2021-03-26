# import os
# folder = r'C:\Python39\Lib\site-packages'
# py_files = [
#     item
#     for item in os.listdir(folder)
#     if item.lower().endswith('.py')
# ]
# print(py_files, type(py_files))  # поиск в папке элементов заканчивающихся на .ру
#
# py_files = [
#     os.path.join(folder, item)
#     for item in os.listdir(folder)
#     if item.lower().endswith('.py')
#     ]
# print(py_files)  # поиск и показ пути
#
# dirs = [
#     item
#     for item in os.listdir(folder)
#     if os.path.isdir((os.path.join(folder, item)))
# ]
# print(dirs, type(dirs))

import os

dir_name = 'sample_dir'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

dir_path = os.path.join('data', 'src')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

dir_name = 'first_dir'
new_dir_name = 'first_out_dir'
if os.path.exists(dir_name) and not os.path.exists(new_dir_name):
    os.rename(dir_name, new_dir_name)


