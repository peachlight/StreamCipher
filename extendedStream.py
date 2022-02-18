from vigenere import enkripsiVig


def swapExt (l, position1, position2):
    l[position1], l[position2] = l[position2], l[position1]
    
    return l

def turnIntoASCIIExt (input):
    temp = []
    for huruf in input:
        temp.append(ord(huruf))
    
    return temp

def ksaExt (kunci):
    s = []

    for a in range (256):
        s.append(a)
    
    j = 0
    for i in range (256):
        j = (j + s[i] + kunci[i % len(kunci)]) % 256
        swapExt(s,i,j)
    
    return s

def prgaExt (s,kata):
    i = 0
    j = 0
    c = []
    for idx in range (len(kata)):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        swapExt(s,i,j)
        t = (s[i] + s[j]) % 256
        u = s[t]
        c.append(u)
    return c

def resultExt (kata,c):
    for idx, plaintext in enumerate(kata):
        kata[idx]= plaintext ^ c[idx]
    return kata

# inputKata = str(input("Masukan text: "))



# f = open('C:/Users/mhani/UTS TST/StreamCipher/Coba1.png','rb')

# kata = bytearray(f.read())
# inputKey = str(input("Masukan text: "))
# inputdefault = 'haniftasya'

# f.close()

# # kata = turnIntoASCII(inputKata)
# kunci = turnIntoASCII(inputKey)
# default = turnIntoASCII(inputdefault)
# # kunci = modifKunci(kata,kunci)

# kunci = enkripsiVig(kunci,default)
# # print(kunci)

# s = ksa(kunci)
# c = prga(s,kata)

# # print(kata)
# # print(c)

# kata = result(kata,c)

# f = open('C:/Users/mhani/UTS TST/StreamCipher/Coba1.png','wb')
# f.write(kata)
# f.close