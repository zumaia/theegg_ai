# Importo la libreria
import pandas as pd

# Introducimos los datos que tenemos
capacidad = int(input("Peso total que el camión puede llevar en kg: "))
n = int(input("Número total de vacas a la venta: "))
caracteristicas_vacas = []

#Petición de datos de cada vaca y almacenamiento en un array de colecciones tipo diccionario
for count in range(n):
    peso = int(input(f"Peso en kg de la vaca {count+1} : "))
    produccion = int(input(f"Producción en l/día de la vaca {count+1} : "))
    caracteristicas_vacas.append(dict(key = count+1, key_peso = peso, key_produccion = produccion))

    # Convierto el diccionario en dataframe
datos = pd.DataFrame(caracteristicas_vacas)
# Ordeno por rentabilidad.
datos['rentabilidad']= datos['key_produccion']/datos['key_peso']
datos = datos.sort_values(by=['rentabilidad'], ascending=False)

# convierto en listas
vaca = datos['key'].tolist()
peso = datos['key_peso'].tolist()
produccion = datos['key_produccion'].tolist()

# vemos el peso de las vacas mas productivas hasta llegar a peso del camión
i = 0
s = 0
new_list = []
while i < len(peso) and s + peso[i] < capacidad:
    new_list.append(peso[i])
    s += peso[i]
    i += 1
    
    
def camion_ingenuo(produccion, peso, capacidad, n):
    if n == -1 or capacidad == 0:
        return 0
    if peso[n] <= capacidad:
        no_insert = camion_ingenuo(produccion, peso, capacidad, n-1)
        insert = produccion[n] + camion_ingenuo(produccion, peso, capacidad - peso[n], n-1)
        max_sack = max(no_insert, insert)
        return max_sack 
    else:
        return camion_ingenuo(produccion, peso, capacidad, n-1)

result = (camion_ingenuo(produccion, peso, capacidad, n-1))    
    

print("La combinacion de vacas que entra en el camión y que produce la mayor cantidad de leche es: ")


print("vaca número: ", vaca[0:len(new_list)])
print("Peso de las vacas seleccionadas: ", new_list)
print("Produccion total: ", result)
