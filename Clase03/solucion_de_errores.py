# solucion_de_errores.py
# Ejercicios de errores en el código
#%%
# Ejercicio 3.5. Función tiene_a()
"""
	El error era de tipo semántico ya que de la manera en que estaba el código
	en un principio, sólo se evalua si la 'a' se encuentra en la primera letra de la
	expresión y además solo evalua si es una 'a' minuscula.

	Para corregirlo elimine el bloque 'else', para que si no encuentra la 'a' en esa
	posicion continue iterando sin retornar nada y la busque en el siguiente caracter.
	
	Además, en el momento de comparar con 'a' en el if, convierto expresion[i] a minuscula
	para evaluar si la expresión tiene 'a' o 'A'.
	
	A continuación va el código corregido...
"""
def tiene_a(expresion):
	n = len(expresion)
	i = 0
	while i<n:
		if expresion[i].lower() == 'a':
			return True
		i += 1
	print()

#%%
# Ejercicio 3.6. Función tiene_a(), nuevamente
"""
	El código tenia errores de tipo sintáctico ya que faltaban los ':' tanto para definir la
	función, como para el bloque 'while' y para el 'if'.
	
	Tambien tenía un error sintáctico en el if ya que se estaba usando el '=' para asignar el
	valor de la variable en vez del '==' para comparar ambos valores.
	
	Por último tenia un NameError ya que se estaba devolviendo Falso en vez de la palabra
	reservada 'False' que representa el valor booleano.
	
	A continuación va el el código corregido...
"""
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        i += 1
    return False

#%%
# Ejercicio 3.7. Función tiene_uno()
"""
	El código tenia un TypeError ya que no es posible comparar un 'int' como es 1984 con
	un caracter como '1' y además una variable de tipo 'int' no posee el metodo len().
	
	Para solucionar eso convierto la variable 'expresion' a un string casteandola con la
	funcion 'str()'.
	
	A continuación va el el código corregido...
"""
def tiene_uno(expresion):
	expresion = str(expresion)
	n = len(expresion)
	i = 0
	tiene = False
	while (i<n) and not tiene:
		if expresion[i] == '1':
			tiene = True
		i += 1
	return tiene
	
#%%
# Ejercicio 3.8. Función suma()
"""
	El código tiene un error semantico ya que el resultado no es el esperado.
	
	Esto ocurre porque la función no retorna el resultado de la suma, y cuando no se
	especifica ningún 'return' la función por defecto retorna 'None'
	
	Para solucionarlo agregué return c en la ultima línea de la función.

	A continuación va el el código corregido...
"""
...
def suma(a,b):
	c = a + b
	return c
	
#%%
# Ejercicio 3.9. Función leer_camion()
"""
	El código tiene un error de tipo semántico ya que no arroja ningún error pero el
	resultado no es el esperado.
	
	El problema está en que estamos creando un diccionario llamado registro por fuera del
	bucle for, entonces cada vez que modificamos el valor del diccionario y lo agregamos
	a la lista camion, estamos apuntando siempre al mismo espacio en memoria y por eso
	vemos siempre el mismo valor repetido.
	
	Para solucionar esto tenemos que crear el diccionario dentro del bucle for, entonces en
	cada nueva iteracción se creará un nuevo diccionario los cuales apuntan a diferentes
	espacios en la memoria y por ende veremos los diferentes valores cargados en la lista.
	
	A continuación va el el código corregido...
"""
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]

    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

