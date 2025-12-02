with open("challengefile","rb") as f:
    data = f.read()

data_hex = data.hex()
simpan_hex = str(data_hex)
var = ""
buffer = ""
for i in range(0,len(simpan_hex),2):
    var = simpan_hex[i:i+2] + var 
    if len(var) == 8:
        buffer = buffer + var
        var = ''
data_hex = bytes.fromhex(buffer+var)
with open("flag.jpg",'wb') as f:
    f.write(data_hex)
