from string import ascii_letters as al
from random import randint as ri


def main():
    with open('names.txt', 'w', encoding='utf-8') as f:
        for _ in range(10):
            f.write(f'{gen_names()}\n')


def gen_names():
    vowels = ['a', 'e', 'i', 'u', 'o', 'y']
    len_name = ri(4, 7)
    name = ''
    for i in range(len_name):
        if i == 0:
            name = al[ri(26, 51)]
        else:
            if i%2!=0:
                name += vowels[ri(0, 5)]
            else:
                name += al[ri(0, 27)]
    return name


if __name__ == "__main__":
    main()
