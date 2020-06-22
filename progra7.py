import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import random
from time import time
from progra5 import insertSort

datos = [ii*100 for ii in range(1,21)]
tiempo_is = []

for ii in datos:
    lista_is = random.sample(range(0,10000000), ii)
    t0 = time()
    insertSort(lista_is)
    tiempo_is.append(round(time()-t0,6))

print("Tiempos parciales de ejecución en insert sort {} [s]".format(tiempo_is))
fig, ax = plt.subplots()
ax.plot(datos, tiempo_is, label="insert sort", marker="*", color="r")
ax.set_xlabel("Datos")
ax.set_ylabel("Tiempo")
ax.grid(True)
ax.legend(loc=2)

plt.title("Tiempos de ejecución [s] inser sort")
plt.show()