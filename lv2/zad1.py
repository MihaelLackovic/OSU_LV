import numpy as np
import matplotlib . pyplot as plt

x=np.array([1,2,3,3,1])
y=np.array([1,2,2,1,1])


plt . plot (x , y , "b" , linewidth =1 , marker =".", markersize =10 )
plt . axis ([0 ,4 ,0 , 4])
plt . xlabel (" X-os ")
plt . ylabel (" Y-os ")
plt . title ( " Zadatak 1 ")
plt.show()