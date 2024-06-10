import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_libros = pd.read_csv("C:\\Users\\USUARIO\\Documents\\Alberto Lara - Python\\Lectura_base_datos\\Mat_Normalizado4.CSV")

#print(df_libros["PRECIO__68"])
#Lo que hace es asignar solo precios a la columna precio 68 y si hay valores que no son numéricos, los devuelve como error
#df_libros['PRECIO__68'] = pd.to_numeric(df_libros['PRECIO__68'], errors='coerce')
#Ordenado_Por_Precio = df_libros.sort_values("PRECIO_68", ascending=False)
# muestra la cantidad de columnas y filas del df--> Filas_y_Columnas_totales=df_libros.shape
# Describe las medidas de tendencia --> df_info=df_libros.describe()
#consulta_libro=df_libros.loc[76124,"PRECIO_68"]

#selecciona toda la columna del costo--> Costo=df_libros.loc[:,"PRECIO_68"]
#Selecciona los libros cuyo costo sea mayor a dos milloes --> Costo_mayor_a_1_millon = df_libros.loc[df_libros["PRECIO_68"]>2000000,:]

# Grafico de linea ---> sns.lineplot(x="BIBLIOTECA",y="PRECIO_68",data=df_libros)

sns.boxplot(x="BIBLIOTECA",y="PRECIO_68",data=df_libros)
Total_libros=df_libros['BIBLIOTECA'].count()
Costo_libros=df_libros['PRECIO_68'].sum()


print(f"El costo total de los libros es de: {Costo_libros} y la cantidad de libros son: {Total_libros} " )

plt.show()