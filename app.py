# Import Library & Extension
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# Import Function
from streamcipher import swap,turnIntoASCII,ksa,prga,result
from extendedStream import swapExt,turnIntoASCIIExt,ksaExt,prgaExt,resultExt
from vigenere import enkripsiVig
# from extendedStreamFunc import *

# Tampilan Halaman Utama
root = tk.Tk()
root.title("Stream Cipher")
canvas = tk.Canvas(root, height=580, width=720, bg="#C0D1EB")
canvas.pack()

frame = tk.Frame(root, bg="#E1EAF7")
frame.place(relwidth=0.9, relheight=0.8, relx=0.05, rely=0.05)

titleText = Text(frame, height=10, width=52)
labelTitle = Label(frame, text="Tugas 2 II4031 Kriptografi dan Koding")
labelTitle.config(font = ("Arial", 24))
labelTitle.pack()

# Add Function Upload File
def UploadAction(event=None):
    tf = filedialog.askopenfilename(initialdir="C:/Users/MainFrame/Desktop/",
        title="Select a File",
        filetypes=(("All Files", "*.*"),))
    pathh.insert(END, tf)
    return (tf)

# Add Function Upload Text
def UploadText(event=None):
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    inputtxt.delete("1.0","end")
    inputtxt.insert(END, data)
    tf.close()

pathh = Entry(root)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)

# Add Function Encrypt - Decrypt
def encryptDecryptText():
    INPUT = inputtxt.get("1.0", "end-1c")
    # print(INPUT)
    KUNCI = inputkunci.get("1.0", "end-1c")
    # print(KUNCI)
    kata = turnIntoASCII(INPUT)
    kunci = turnIntoASCII(KUNCI)
    default = turnIntoASCII('haniftasya')
    kunci = enkripsiVig(kunci,default)
    s = ksa(kunci)
    c = prga(s,kata)
    hasil = result(kata,c)
    
    Output.delete("1.0","end")
    Output.insert(END, hasil)

def encryptDecryptNonText():
    dirPath = UploadAction()
    print(dirPath)
    INPUT = open(dirPath,'rb')
    KUNCI = inputkunci.get("1.0", "end-1c")
    # print(KUNCI)
    kata = bytearray(INPUT.read())
    kunci = turnIntoASCIIExt(KUNCI)
    default = turnIntoASCIIExt('haniftasya')

    INPUT.close()

    kunci = enkripsiVig(kunci,default)
    s = ksaExt(kunci)
    c = prgaExt(s,kata)

    kata = resultExt(kata,c)
    
    # Overwrite file
    f = open(dirPath,'wb')
    f.write(kata)
    f.close

    # Message to label
    Output.delete("1.0","end")
    Output.insert(END, "File has been overwritten")


# Add Button, Label
l = Label(frame, text = "Masukkan karakter untuk didekripsi/enkripsi")
inputtxt = Text(frame, height = 5, width = 25, bg = "light yellow")
inputtxt.insert(END, "Ketik kalimat di sini")
inputkunci = Text(frame, height = 5, width = 25, bg = "light yellow")
inputkunci.insert(END, "Ketikkan kunci di sini")
Output = Text(frame, height = 5, width = 25, bg = "light cyan")
    
l.pack()
inputtxt.pack()
inputkunci.pack()
Output.pack()

uploadTextButton = tk.Button(frame, text = "Upload File for Text", padx=10, pady=5, fg="black", bg="white", command = UploadText)
uploadTextButton.pack(pady=10)
encryptDecryptButton = tk.Button(frame, text = "Encrypt/Decrypt", padx=10, pady=5, fg="black", bg="white", command = encryptDecryptText)
encryptDecryptButton.pack(pady=10)
encryptFileButton = tk.Button(frame, text = "Upload File and Encrypt/Decrypt", padx=10, pady=5, fg="black", bg="white", command = encryptDecryptNonText)
encryptFileButton.pack(pady=10)


root.mainloop()