import random

def main():
    write_num_file(10, 'nums.txt')


def write_num_file(str_count, file_name):
    
    for _ in range(str_count):
        num1=random.randint (-1000, 1001)
        num2=random.uniform(-1000, 1001)
        
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(f'{num1}|{num2}\n')
            
        
        

if __name__ == "__main__":
    main()