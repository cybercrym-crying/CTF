asli = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
subtitusi = "JLSQRTMAZIVHXCKBFDEYNWGPOU"

flag_acak = """SYTe (eakdy tkd sjbyndr yar thjm) jdr j yobr kt skxbnyrd ersndzyo skxbryzyzkc. Skcyreyjcye jdr bdrercyrq gzya j ery kt sajhhrcmre gazsa yrey yarzd sdrjyzwzyo, yrsaczsjh (jcq mkkmhzcm) evzhhe, jcq bdklhrx-ekhwzcm jlzhzyo. Sajhhrcmre nenjhho skwrd j cnxlrd kt sjyrmkdzre, jcq garc ekhwrq, rjsa ozrhqe j eydzcm (sjhhrq j thjm) gazsa ze enlxzyyrq yk jc kchzcr eskdzcm erdwzsr. SYTe jdr j mdrjy gjo yk hrjdc j gzqr jddjo kt skxbnyrd ersndzyo evzhhe zc j ejtr, hrmjh rcwzdkcxrcy, jcq jdr akeyrq jcq bhjorq lo xjco ersndzyo mdknbe jdkncq yar gkdhq tkd tnc jcq bdjsyzsr. Tkd yaze bdklhrx, yar thjm ze bzskSYT{TD3UN3CSO_4774SV5_4D3_S001_7JJ384LS}"""
flag_asli = ""
for i in range(0, len(flag_acak)):
    if flag_acak[i].islower() and flag_acak[i] in asli.lower():
        print(asli[subtitusi.lower().find(flag_acak[i])].lower(), end="")
    elif flag_acak[i].isupper() and flag_acak[i] in asli:
        print(asli[subtitusi.find(flag_acak[i])], end="")
    else:
        print(flag_acak[i], end="")
