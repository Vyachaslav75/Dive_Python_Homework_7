from pathlib import Path
import shutil


def main():
    new_name = 'NEW'
    count_num = 5
    type_now = 'txt'
    type_new = 'rtf'
    name_diap = [2, 5]
    renamer(new_name, count_num, type_now, type_new, name_diap)


def renamer(new_name, count_num, type_now, type_new, name_diap):
    
    f_list=Path().cwd().glob(f'*{type_now}')
    files_count=1
    for j in f_list:
        f_name = Path(j).name.split('.')
        
        if len(f_name[0])>name_diap[0] and len(f_name[0])>=name_diap[1]:
            new_f_name = f_name[0][name_diap[0]: name_diap[1]]
            
        elif len(f_name[0])>name_diap[0] and len(f_name[0])<name_diap[1]:
            new_f_name = f_name[0][name_diap[0]:]
        new_f_name+=new_name
        count_num_str='0'*(count_num-len(str(files_count))) + str(files_count)
        new_f_name+=count_num_str + f'.{type_new}'
        shutil.move(f'{f_name[0]}.{f_name[1]}', new_f_name)
        
    

if __name__ == "__main__":
    main()