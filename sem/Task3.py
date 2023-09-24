import math

def main():
    with (
        open('names.txt', 'r', encoding='utf-8') as f1,
        open('nums.txt', 'r', encoding='utf-8') as f2,
        open(' res.txt', 'w', encoding='utf-8') as f3
          ):
        count_f1=0
        count_f2=0
        while True:
            name=f1.readline()[:-1]
            num=f2.readline().split('|')
            print(f'{name = }')
            print(f'{num = }')
            if name=='' and num[0]=='':
                break
            if name=='' and len(num)>1 and count_f2==0:
                f1.seek(0)
                count_f1+=1
                name=f1.readline().strip()
            elif name=='' and len(num)>1 and count_f2>0:
                break
            if num[0]=='' and name!='' and count_f1==0:
                f2.seek(0)
                count_f2+=1
                num=f2.readline().split('|')
            elif num[0]=='' and name!='' and count_f1>0:
                break
                
            num_res=int(num[0])*float(num[1])
            print(num_res)
            if num_res<0:
                num_res=math.fabs(num_res)
                f3.write(f'{name.lower()}  {num_res}\n')
            else:
                num_res=round(num_res)
                f3.write(f'{name.upper()}  {num_res}\n')
            



if __name__ == "__main__":
    main()