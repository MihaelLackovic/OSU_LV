import numpy as np
import matplotlib . pyplot as plt

a=np.loadtxt('data.csv',skiprows=1,delimiter=',')
print(a)
print (len(a))
visina=np.array(a[:,1])
tezina=np.array(a[:,2])
plt.figure()
plt.scatter(visina,tezina)
plt.xlabel("Visina")
plt.ylabel("Tezina")
plt.title("Omjer visine i težine")


visina2=visina[:50:]
print(visina2)
tezina2=tezina[:50:]
print(tezina2)

plt.scatter(visina2,tezina2)
plt.xlabel("Visina")
plt.ylabel("Tezina")
plt.title("Omjer visine i težine svakog 50.")
plt.figure()
plt.show()

