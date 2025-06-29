import tkinter as tk

root=tk.Tk()

root.geometry("600x800")

tekst = ""
lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A',
        'a' : 'z', 'b' : 'y', 'c' : 'x', 'd' : 'w', 'e' : 'v',
        'f' : 'u', 'g' : 't', 'h' : 's', 'i' : 'r', 'j' : 'q',
        'k' : 'p', 'l' : 'o', 'm' : 'n', 'n' : 'm', 'o' : 'l',
        'p' : 'k', 'q' : 'j', 'r' : 'i', 's' : 'h', 't' : 'g',
        'u' : 'f', 'v' : 'e', 'w' : 'd', 'x' : 'c', 'y' : 'b',
        'z' : 'a'}
 
def atbash(message):
    cipher = ''
    for letter in message:
        # checks for space
        if(letter != ' '):
            #adds the corresponding letter from the lookup_table
            cipher += lookup_table[letter]
        else:
            # adds space
            cipher += ' '
 
    return cipher

def Submit():  # potwierdzenie klucza
    global  EncTekst, tekst, tktekst
    tekst = str(tktekst.get())
    tktekst.set("")
    EncTekst.set(atbash(tekst))
    print(tekst)
    output = str(EncTekst.get())
    with open('output.txt', 'a') as f:
        f.write(output+"\n")
        f.close

tktekst = tk.StringVar()
EncTekst = tk.StringVar()
EncTekst.set(atbash(tekst))


L_EnterShift = tk.Label(root,text="Enter text", font = ('arial',14,'bold'))
E_EnterShift = tk.Entry(root,textvariable=tktekst, font = ('arial',14,'bold'),bg = "lightgray")
B_Submit = tk.Button(root,text="Submit",font = ('arial',14,'bold'), command=lambda:Submit())
L_ShowEncrypted = tk.Label(root, textvariable = EncTekst, font = ('arial',14,'bold'))


L_EnterShift.place(x=250,y=0)
E_EnterShift.place(x=180,y=50)
B_Submit.place(x=250,y=80)
L_ShowEncrypted.place(x=200,y=150)



root.mainloop()