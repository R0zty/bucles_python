    # Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
En este ejercicio se lo provee de una lista de temperaturas,
esa lista de temperaturas corresponde a los valores de temperaturas
tomados durante una temporada del año en Buenos Aires.
Usted deberá analizar dicha lista para deducir
en que temporada del año se realizó el muestreo de temperatura.
La variable con la lista de temperaturas se llama "temp_dataloger"
definida al comienzo del archivo

Debe recorrer la lista "temp_dataloger" y obtener los siguientes
resultados

1 - Obtener la máxima temperatura
2 - Obtener la mínima temperatura
3 - Obtener el promedio de las temperaturas

Los resultados se deberán almacenar en las variables
que ya hemos preparado para usted al comienzo del ejercicio

NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
el máximo y el mínimo utilizando los mismos métodos vistos
durante la clase (ejemplos_clase/ejemplo_5.py)
'''

print("Mi primer pasito en data analytics")
# Empezar aquí la resolución del ejercicio

temperatura_max = None      # Aquí debe ir almacenando la temp máxima
temperatura_min = None      # Aquí debe ir almacenando la temp mínima
temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

# Colocar el bucle aqui......

for valor in temp_dataloger:
    temperatura_len += 1
    print(valor)

if (temperatura_max is None) or (valor > temperatura_max):
    temperatura_max = valor 

    if (temperatura_min is None) or (valor < temperatura_min):
        temperatura_min = valor 
        temperatura_sumatoria += valor

        print(temperatura_max, 'temperatura maxima')
        print(temperatura_min, 'temperatura minima')

       
# Al finalizar el bucle compare si el valor que usted calculó para
# temperatura_max y temperatura_min coincide con el que podría calcular
# usando la función "max" y la función "min" de python
# función "max" --> https://www.w3schools.com/python/ref_func_max.asp
# función "min" --> https://www.w3schools.com/python/ref_func_min.asp

print('maxima', max(temp_dataloger))
print('minima', min(temp_dataloger))


# Al finalizar el bucle debe calcular el promedio como:
# temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

temperatura_promedio = temperatura_sumatoria / temperatura_len
print('promedio', temperatura_promedio)

# Corroboren los resultados de temperatura_sumatoria
# usando la función "sum"
# función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

sumatoria_funcion = sum(temp_dataloger)
print('sumatoria de temperaturas es:', sumatoria_funcion,)

'''
Una vez que tengamos nuestros valores correctamente calculados debemos
determinar en que epoca del año nos encontramos en Buenos Aires utilizando
la estadística de años anteriores. Basados en el siguiente link realizamos
las siguientes aproximaciones:

verano -->      min = 19, max = 28
otoño -->       min = 11, max = 20
invierno -->    min = 8, max = 14
primavera -->   min = 10, max = 24

Referencia:
https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
'''

# En base a los rangos de temperatura de cada estación,
# ¿En qué época del año nos encontramos?
# Imprima el resultado en pantalla
# Debe utilizar temperatura_max y temperatura_min para definirlo


temperaturas_verano = [19, 28]
temperaturas_otoño = [11, 20]
temperaturas_invierno = [8, 14]
temperatura_primavera = [10, 24]

if temperatura_min > min(temperaturas_verano) and temperatura_max < max(temperaturas_verano):
    print('Estamos en Verano')

elif temperatura_min > min(temperaturas_otoño) and temperatura_max < max(temperaturas_otoño):
    print('Estamos en Otoño')

elif temperatura_min > min(temperaturas_invierno) and temperatura_max < max(temperaturas_invierno):
    print('Estamos en Invierno')
    
elif temperatura_min > min(temperaturas_primavera) and temperatura_max < max(temperaturas_primavera):
    print('Estamos en Primavera')