import tarfile

i = 1000
while True:
    if i == 1:
        break
    with tarfile.open(f"{i}.tar","r") as t:
        t.extractall("",filter="data")
    i-=1
    
