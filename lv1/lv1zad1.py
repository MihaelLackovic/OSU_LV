import math
print("Unesi satnicu")
novci = float(input())
print("Unesi broj sati")

sati = float(input())
print ("To je ukupno:")
ukupno=novci*sati
print (ukupno)

def total_euro(novci,sati):
    ukupno = novci*sati
    return ukupno

print(total_euro(novci,sati))