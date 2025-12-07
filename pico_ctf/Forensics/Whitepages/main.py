with open("whitepages.txt","rb") as f:
    data= f.read()

data_hex = data.hex()
string = str(data_hex)
simpan = ""
for i in range(0,len(data_hex),2):
    simpan +=string[i:i+2]
    if simpan == "20":
        print(1,end="")
        simpan = ""
    elif  len(simpan) == 6:
        print(0,end="")
        simpan = ""


