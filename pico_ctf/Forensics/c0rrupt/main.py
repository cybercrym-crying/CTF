import binascii

# chunk type + data pHYs
data = bytes.fromhex("70485973000016250000162501")
crc = binascii.crc32(data) & 0xFFFFFFFF
print(hex(crc))  # CRC 4 byte yang bisa ditulis ke file

