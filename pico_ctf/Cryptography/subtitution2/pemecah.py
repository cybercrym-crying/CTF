asli = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
subtitusi = "TKZBFVRAXJCPGLQSIYENWUMOHD"
flag_acak = "sxzqZNV{L6Y4G_4L41H515_15_73B10W5_8F1KV808}"
flag_asli = ""
for i in range(0, len(flag_acak)):
    if flag_acak[i].islower() and flag_acak[i] in asli.lower():
        print(asli[subtitusi.lower().find(flag_acak[i])].lower(), end="")
    elif flag_acak[i].isupper() and flag_acak[i] in asli:
        print(asli[subtitusi.find(flag_acak[i])], end="")
    else:
        print(flag_acak[i], end="")
