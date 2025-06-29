import tkinter as tk

root=tk.Tk()

root.geometry("600x800")

tekst = ""

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
    global shift, EncTekst, tekst, tktekst
    tekst = str(tktekst.get())
    tktekst.set("")
    EncTekst.set(encrypt(tekst,shift))
    output = str(EncTekst.get())
    with open('output.txt', 'a') as f:
        f.write(output+"\n")
        f.close

tktekst = tk.StringVar()
shift = 13
EncTekst = tk.StringVar()
EncTekst.set(encrypt(tekst,shift))


L_EnterShift = tk.Label(root,text="Enter text", font = ('arial',14,'bold'))
E_EnterShift = tk.Entry(root,textvariable=tktekst, font = ('arial',14,'bold'),bg = "lightgray")
B_Submit = tk.Button(root,text="Submit",font = ('arial',14,'bold'), command=lambda:Submit())
L_ShowEncrypted = tk.Label(root, textvariable = EncTekst, font = ('arial',14,'bold'))


L_EnterShift.place(x=250,y=0)
E_EnterShift.place(x=180,y=50)
B_Submit.place(x=250,y=80)
L_ShowEncrypted.place(x=250,y=150)



root.mainloop()