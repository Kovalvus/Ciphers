# boards containing all letters (prolly could be done more easily)
l1 = [1,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
l2 = [2,"b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a"]
l3 = [3,"c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b"]
l4 = [4,"d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c"]
l5 = [5,"e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d"]
l6 = [6,"f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e"]
l7 = [7,"g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f"]
l8 = [8,"h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g"]
l9 = [9,"i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h"]
l10 = [10,"j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i"]
l11 = [11,"k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j"]
l12 = [12,"l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k"]
l13 = [13,"m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l"]
l14 = [14,"n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
l15 = [15,"o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
l16 = [16,"p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]
l17 = [17,"q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
l18 = [18,"r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"]
l19 = [19,"s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
l20 = [20,"t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]
l21 = [21,"u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t"]
l22 = [22,"v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u"]
l23 = [23,"w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v"]
l24 = [24,"x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]
l25 = [25,"y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]
l26 = [26,"z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]

l0 = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26,l1]    # list with all lists for easier access

EncOrDec = 0    # var for checking if user is currently encoding or decoding, 0 - encoding, 1 - decoding

start = str(input("Chcesz zakodować czy dekodować wiadomość? \nWpisz 1 jeśli zakodować, 2 jeśli dekodować: "))

if (start == "1"):
    EncOrDec = 0
elif (start == "2"):
    EncOrDec = 1
else:
    print("Niepoprawna odpowiedź")
    exit()

if (EncOrDec == 0):
    message = str(input("Wpisz wiadomosc do zakodowania: "))
else:
    message = str(input("Wpisz wiadomosc do zdekodowania: "))
key = str(input("Podaj klucz: "))



a = 0   # variables needed for the encoding loop (explained below)
i = 0
output = ""

def encoding():
    global a,i, message, key, output, EncOrDec

    message2 = message.replace(" ","0")   # changing whitespaces into 0 to make them easier to detect

    messagel = len(message2.replace("0",""))
    keyl = len(key)

    key = key * ((messagel // keyl)+1)
    key = key[:messagel]    # making the key the same length as the message

    x = 0   # temp variable, used for making it so the program won't run for too many letters (won't try to encrypt blank spaces)
    z = 0   # temp variable, same as x, but this one goes up by 1 when encountering a blank space, used instead of x so the program won't end prematurely

    while (x < messagel):   # getting letters from message and key
        letter1 = message2[z]
        letter2 = key[x]
        if(letter1 == "0"):
            while(letter1 == "0"):
                z += 1
                letter1 = message2[z]   # z goes up by 1 to skip the space and get an actual letter
                output += " "

        x += 1  # both temp vars go up by 1 to match the current localization in the message that's being encrypted
        z += 1
        a = 0   # temp var, used only for controlling the encoding process for letter1 (gets switched into 1 when encoding ends)
        i = 0   # temp var, used for searching through the lists containing all letters

        # encoding
        while (a == 0): # first loop going through lists to find the one that matches letter1 as [1]
            if ((l0[i])[1] == letter1): # l0 - list containing all 26 letter boards, i - checking inside said boards, [1] - position 1 in those boards, this one has the first letter of the board
                list1 = (l0[i])
                i = 0
                while (a == 0): # second loop going through lists to find the one that matches letter2 as [1]
                    if ((l0[i])[1] == letter2):
                        list2 = (l0[i])
                        output += list1[(list2[0])]
                        a = 1
                    else:
                        i = i+1
            else:
                i = i+1

    if (EncOrDec == 0):     # changing "0" back to spaces
        print("Encoded message: ",output.replace("0"," "))
    else:
        print("Decoded message: ",output.replace("0"," "))

def decoding():
    global a,i, message, key, output, EncOrDec

    keyl = len(key)
    x = 0
    a = 0
    i = 0

    while (x < keyl):
        a = 0
        i = 0
        letter1 = key[x]

        while (a == 0):     # "inverting" the key by using the formula: K2(i) = [26 – K(i)] mod 26 
            # gdzie K(i) – kolejna litera słowa kluczowego, numerowane A=0, B=1 itd., a K2(i) – kolejna litera hasła „odwróconego”. 26 oznacza liczbę liter alfabetu łacińskiego. 
                if ((l0[i])[1] == letter1):
                    invletter = (l0[(26 - (l0[i])[0] + 1)])[1]  # formula is changed up a bit to work with my way of numbering the lists
                    output += invletter
                    a = 1
                else:
                    i += 1
        
        x += 1
    
    key = output    # changing the key into the "inverted" version
    a = 0
    i = 0
    output = ""

    # decoding by encoding the encrypted message but now with the "inverted" key
    encoding()

if (EncOrDec == 0):
    encoding()
else:
    decoding()