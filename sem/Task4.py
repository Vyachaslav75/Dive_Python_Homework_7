from string import ascii_letters as al
from random import randint as ri, randbytes as rb
from pathlib import Path
import os


def main():
    # create_files('txt', 2, 7, 256, 512, 3)
    # print(gen_name(6, 30))
    # print(al[26])
    file_touple = (('txt', 2), ('img', 3), ('dbf', 4))
    gen_files(file_touple, '2')


def create_files(ext, min_len=6, max_len=30, min_byte=256, max_byte=4096, count_files=42):
    for _ in range(count_files):
        file_name = gen_name(min_len, max_len)+'.'+ext
        rw_bytes = rb(ri(min_byte, max_byte))
        if Path(file_name).exists():
            file_name = '1_' + file_name
        with open(file_name, 'wb') as f:
            f.write(rw_bytes)


def gen_name(min_len=6, max_len=30):
    name_f = ''
    for _ in range(ri(min_len, max_len)):
        name_f += al[ri(0, 26)]
    return name_f


def gen_files(ext_count, dir_path=''):
    if dir_path != '' and not Path(dir_path).exists():
        Path.mkdir(dir_path)
        os.chdir(dir_path)
    elif Path(dir_path).exists() and Path(dir_path).is_dir():
        os.chdir(dir_path)

    for i in ext_count:
        create_files(ext=i[0], count_files=i[1])
    os.chdir('..')


if __name__ == "__main__":
    main()
