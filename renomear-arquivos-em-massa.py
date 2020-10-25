import os
import shutil

main_folder = r'C:\Users\Wolker Dias\Desktop\Pasta teste'

cont = 0
def rename_file(file):
    global cont
    cont = cont + 1
    file_extension = os.path.splitext(file)[1] #acessa o arquivo e separa o nome da extensão. o [1] pega somente a extensão do arquivo
    file_name_numbers = 'Nome{:04d}'.format(cont)

    return f'{file_name_numbers}{file_extension}'


def file_loop(root, dirs, files):
    for file in files:
        new_file_name = rename_file(file)
        old_file_full_path = os.path.join(root, file)
        new_file_full_path = os.path.join(root, new_file_name)
        print(f'{new_file_name}')
        shutil.move(old_file_full_path, new_file_full_path)


def main_loop():
    for root, dirs, files in os.walk(main_folder):
        file_loop(root, dirs, files)


if __name__ == '__main__':
    main_loop()
