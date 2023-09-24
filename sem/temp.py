from random import randint as ri, randbytes as rb
from pathlib import Path


print(len(rb(256)))
f='Task3.py'
print(Path(f).exists())
p=Path().cwd().glob('*.py')
for i in p:
    f = Path(i).name
    print(f)

