import pandas as pd
import matplotlib.pyplot as plt


LibrosUN=pd.read_csv('c:/Users/USUARIO/Downloads/datosbiblioteca4.csv', delimiter=';', low_memory=False)
BIBLIOTECA=LibrosUN['BIBLIOTECA']
PRECIO_UNIT_68=LibrosUN['PRECIO_UNIT_68']
DEPRECIACION=LibrosUN['DEPRECIACION']
Costo = pd.to_numeric(PRECIO_UNIT_68, errors='coerce')
Depreciacion = pd.to_numeric(DEPRECIACION, errors='coerce')

suma_COSTO = Costo.sum()
suma_DEPRECIACION = Depreciacion.sum()
print(Depreciacion)
Mensaje=f"El costo es {suma_COSTO} y la depreciación es {suma_DEPRECIACION}"
print(Mensaje)

columna_x = LibrosUN['BIBLIOTECA']
columna_y = LibrosUN['PRECIO_UNIT_68']

# Graficar los datos
plt.bar(columna_x, columna_y)
plt.xlabel('BIBLIOTECA')
plt.ylabel('PRECIO_UNIT_68')
plt.title('Gráfico de dispersión de columna_x vs columna_y')
plt.show()