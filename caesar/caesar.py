import tkinter as tk

root=tk.Tk()

root.geometry("600x800")

# zczytanie tekstu z pliku
with open('plik.txt') as f:
    tekst = f.read()

    print(tekst)

def encrypt(text,s):  # enkrypcja
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Add spaces
        elif (char == " "):
            result += " "
            
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
 

def Submit():  # potwierdzenie klucza
    global shift, S_shift, EncTekst
    try:
        shift = int(S_shift.get())
    except:
        Exception
    S_shift.set("")
    EncTekst.set(encrypt(tekst,shift))
    print(shift)
    output = str(EncTekst.get())
    with open('output.txt', 'a') as f:
        f.write(output+"\n")
        f.close


S_shift = tk.StringVar()
shift = 0
print ("Text  : " + tekst)
print ("Shift : " + str(shift))
print ("Cipher: " + encrypt(tekst,shift))
EncTekst = tk.StringVar()
EncTekst.set(encrypt(tekst,shift))


L_EnterShift = tk.Label(root,text="Enter desired shift value", font = ('arial',14,'bold'))
E_EnterShift = tk.Entry(root,textvariable=S_shift, font = ('arial',14,'bold'),bg = "lightgray")
B_Submit = tk.Button(root,text="Submit",font = ('arial',14,'bold'), command=lambda:Submit())
L_ShowEncrypted = tk.Label(root, textvariable = EncTekst, font = ('arial',14,'bold'))


L_EnterShift.place(x=180,y=0)
E_EnterShift.place(x=180,y=50)
B_Submit.place(x=250,y=80)
L_ShowEncrypted.place(x=250,y=150)



root.mainloop()