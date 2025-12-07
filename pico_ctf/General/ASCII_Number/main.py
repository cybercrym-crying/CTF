with open("hex.txt", "r") as f:
    hex = f.read().replace(" ","")
simpan = ""

for i in range(0,len(hex),2):
    if hex[i:i+2] !="0x":
        simpan += hex[i:i+2]
print(simpan)
