import tkinter as tk

root=tk.Tk()

root.geometry("600x800")

def encryptRailFence(text, key):
 
    # create the matrix to cipher
    # plain text key = rows ,
    # length(text) = columns
    # filling the rail matrix
    # to distinguish filled
    # spaces from blank ones
    rail = [['\n' for i in range(len(text))]
                for j in range(key)]
     
    # to find the direction
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
         
        # check the direction of flow
        # reverse the direction if we've just
        # filled the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
         
        # fill the corresponding alphabet
        rail[row][col] = text[i]
        col += 1
         
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher
    # using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))

def Submit():  # potwierdzenie klucza
    global  EncTekst, tekst, tktekst, klucz, tkklucz
    tekst = str(tktekst.get())
    klucz = int(tkklucz.get())
    EncTekst.set(encryptRailFence(tekst, klucz))
    print(tekst)
    output = str(EncTekst.get())
    with open('output.txt', 'a') as f:
        f.write(output+"\n")
        f.close

tekst = ""
klucz = 0
tkklucz = tk.StringVar()
tktekst = tk.StringVar()
EncTekst = tk.StringVar()


L_EnterText = tk.Label(root,text="Enter text", font = ('arial',14,'bold'))
E_EnterText = tk.Entry(root,textvariable=tktekst, font = ('arial',14,'bold'),bg = "lightgray")
L_EnterShift = tk.Label(root,text="Enter key", font = ('arial',14,'bold'))
E_EnterShift = tk.Entry(root,textvariable=tkklucz, font = ('arial',14,'bold'),bg = "lightgray")
B_Submit = tk.Button(root,text="Submit",font = ('arial',14,'bold'), command=lambda:Submit())
L_ShowEncrypted = tk.Label(root, textvariable = EncTekst, font = ('arial',14,'bold'))


L_EnterText.place(x=250,y=0)
E_EnterText.place(x=180,y=50)
L_EnterShift.place(x=250,y=100)
E_EnterShift.place(x=180,y=150)
B_Submit.place(x=250,y=180)
L_ShowEncrypted.place(x=200,y=250)



root.mainloop()