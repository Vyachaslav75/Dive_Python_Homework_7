from pathlib import Path
import os
import shutil


def main():
    dir_name='1'
    type_files = {
        'video' : ['.mkv', '.avi', '.wmv'],
        'image' : ['.jpg', '.png', '.bmp'],
        'text': ['.txt', '.rtf', '.pdf']
    }
    mover(dir_name, type_files)


def mover(dir_name, type_files):
    if Path(dir_name).is_dir():
        os.chdir(dir_name)
        for key, item in type_files.items():
            if not Path(key).exists():
                Path.mkdir(key)
            for i in item:
                f_list=Path().cwd().glob(f'*{i}')
                for j in f_list:
                    f_name = Path(j).name
                    shutil.move(f_name, f'{key}/')
        os.chdir('..')
        
    

if __name__ == "__main__":
    main()