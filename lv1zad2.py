try:
    print("Unesi broj izmedu 0.0 i 1.0")
    ocjena=float(input())
    if ocjena <= 1.0 and ocjena >=0.9 :
        print("Kategorija A")
    elif ocjena < 0.9 and ocjena >=0.8 :
        print("Kategorija B") 
    elif ocjena < 0.8 and ocjena >=0.7 :
        print("Kategorija C")
    elif ocjena < 0.7 and ocjena >=0.6 :
        print("Kategorija D") 
    elif ocjena < 0.6  :
        print("Kategorija F") 
    elif ocjena <0.0 or ocjena >1.0:
        print("Broj nije u intervalu")
except:
    print("Niste unijeli broj")