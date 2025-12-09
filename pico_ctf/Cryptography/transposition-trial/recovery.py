teks = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V9AAB1F8}7"
simpan = ""
for i in range(0, len(teks), 3):
    buffer = teks[i : i + 3]
    print(buffer[2] + buffer[0:2], end="")
