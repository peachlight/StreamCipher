def enkripsiVig (kata,kunci):
    hasil = []
    sisa = len(kata)-len(kunci)
    if sisa > 0:
        for i in range (sisa):
            kunci.append(kunci[i])

    for i in range (len(kata)):
        temp = (kata[i] + kunci[i])%256
        hasil.append(temp)
    return hasil