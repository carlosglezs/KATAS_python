#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados

def frecuencias(cadena):
    """
    Esta función toma una cadena de texto como entrada y devuelve un diccionario con las frecuencias 
    de aparición de cada carácter en la cadena. Los espacios son ignorados y las letras se cuentan 
    sin distinguir entre mayúsculas y minúsculas.

    Parámetros:
    cadena (str): La cadena de texto en la que se contarán las frecuencias de los caracteres.

    Retorna:
    dict: Un diccionario con los caracteres como claves y sus frecuencias como valores.
    """
    diccionario = {} #creamos diccionario vacío
    for elemento in cadena: #iteramos cada elemnto del string
        if elemento != " ": #nos quedamos con los que no son espacio
            elemento = elemento.lower() #pasamos todos a minus
            if elemento in diccionario: #los buscamos en el diccionario
                diccionario[elemento] += 1 #si ya habia sido encontrado +1 
            else:
                diccionario[elemento] = 1 #si es la primera vez =1
    return diccionario

# Ejemplo de uso:
cadena = "hola hola como estamos"
frecuencias(cadena)

#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()


lista = [12, 32, 12, 43, 54, 65, 34]

def duplicador(lista):
    """
    Esta función toma una lista de números enteros y devuelve una nueva lista donde cada elemento
    es el doble del valor correspondiente en la lista original.

    Parámetros:
    lista (list): Una lista de números enteros.

    Retorna:
    list: Una lista con los elementos de la lista original multiplicados por 2.
    """
    return list(map(lambda x: x * 2, lista)) #generamos una lista y aplicamos x*2 a traves de una lambda y usamos map para referirnos a la lista con los números

# Ejemplo de uso:
duplicador(lista)

#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def encontrar(lista, objetivo):
    """
    Esta función toma una lista de palabras y una palabra objetivo. Devuelve una lista con todas 
    las palabras de la lista que están contenidas dentro de la palabra objetivo.

    Parámetros:
    lista (list): Una lista de palabras a ser evaluadas.
    objetivo (str): Una palabra que se busca dentro de las palabras en la lista.

    Retorna:
    list: Una lista con las palabras de la lista que contienen la palabra objetivo.
    """
    return [palabra for palabra in lista if palabra in objetivo] #iteramos las palabras en la lista y nos quedamos con las palabras que sean iguales al objetivo

# Ejemplo de uso:
lista = ["platano", "melon", "pera", "platano", "kiwi"]
objetivo = "platano"

encontrar(lista, objetivo)

#4.Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función 
map()

lista_1 = [12, 21, 23, 43, 567]
lista_2 = [1, 54, 12, 7, 43]

def diferenciador(lista_1, lista_2):
    """
    Esta función toma dos listas de números y devuelve una nueva lista en la que cada elemento
    es el resultado de restar el valor correspondiente de la segunda lista del valor de la primera lista.

    Parámetros:
    lista_1 (list): Una lista de números.
    lista_2 (list): Una lista de números que se restarán de la lista_1.

    Retorna:
    list: Una lista con los resultados de las restas de los elementos de lista_2 de los elementos de lista_1.
    """
    return list(map(lambda x, y: x - y, lista_1, lista_2)) #generamos un lista que reste el primer elemento menos el segundo usando lambda y refiriendonos a la primera lista y  a la segunda mediante map()

# Ejemplo de uso:
diferenciador(lista_1, lista_2)

#5.   Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado

def evaluador(lista, nota_aprobado = 5):
    """
    Esta función recibe una lista de notas y una nota de aprobado. Calcula la media de las notas 
    y devuelve un tupla con la media y el estado (aprobado o suspenso) dependiendo de si la media 
    es mayor o igual que la nota de aprobado.

    Parámetros:
    lista (list): Una lista de números que representan las notas.
    nota_aprobado (int o float, opcional): La nota mínima para aprobar, por defecto es 5.

    Retorna:
    tuple: Una tupla con dos elementos: la media de las notas y el estado ("aprobado" o "suspenso").
    """
    media = sum(lista) / len(lista) #calculamos la media
    if media >= nota_aprobado:
        estado = "aprobado" #si supera o iguala 5 está aprobado 
    else: 
        estado = "suspenso" #si no suspenso
    return (media, estado)

# Ejemplo de uso:
lista = [4, 6, 8, 3, 8, 10]
evaluador(lista, 5)

#6. Escribe una función que calcule el factorial de un número de manera recursiva.

def numero_a_factorizar(n):
    """
    Esta función calcula el factorial de un número entero positivo n de forma recursiva.
    Si el número es negativo, devuelve un mensaje indicando que no se puede calcular el factorial.
    Si el número es 0 o 1, devuelve 1, ya que el factorial de ambos es 1 por definición.

    Parámetros:
    n (int): Un número entero para el cual se calculará el factorial.

    Retorna:
    int: El factorial de n, o un mensaje en caso de ser negativo.
    """
    if n < 0:
        return "no se factoriza numeros negativos"
    elif n == 0 or n == 1:
        return 1  # El factorial de 0 y 1 es 1
    else:    
        return n * numero_a_factorizar(n - 1)  # Llamada recursiva para calcular el factorial

# Ejemplo de uso:
numero_a_factorizar(13)

#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def cadena(lista):
    """
    Esta función toma una lista de tuplas y convierte cada tupla en una cadena de texto.
    Cada tupla se convierte en un string en formato de tupla (por ejemplo, ('a', 'b', 'c') se convierte en '(a, b, c)').

    Parámetros:
    lista (list): Una lista de tuplas que se convertirán en cadenas de texto.

    Retorna:
    list: Una lista con las tuplas convertidas a cadenas de texto.
    """
    return list(map(lambda x: str(x), lista)) #hacemos una lista donde convertimos cada tupla de la lista a string

# Ejemplo de uso:
lista = [("hola"),("como"),("estas")] 
cadena(lista)  


#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no

def division():
    """
    Esta función solicita dos números al usuario, los divide y muestra el resultado.
    Maneja los siguientes casos de error:
    - Si se ingresan valores no numéricos, se muestra un mensaje de error.
    - Si se intenta dividir entre cero, se muestra un mensaje de error.
    
    La función utiliza un bloque try-except para manejar excepciones, y en caso de éxito, 
    muestra el resultado de la división.

    No toma parámetros y no retorna ningún valor; solo muestra el resultado o un mensaje de error.
    """
    try:
        primer_numero = float(input("Ingresa el primer número: "))
        segundo_numero = float(input("Ingresa el segundo número: "))
        resultado = primer_numero / segundo_numero
    except ValueError:
        print("Error: por favor ingresa valores numéricos")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        print(f"La división fue exitosa. El resultado es: {resultado}")     

# Ejemplo de uso:
division()

#9.  Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def filtrar_mascotas(lista_mascotas):
    """
    Esta función recibe una lista de mascotas y filtra las que están prohibidas según una lista predeterminada.
    Las mascotas prohibidas son: "Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo" y "Oso".
    
    Parámetros:
    lista_mascotas (list): Una lista de nombres de mascotas que se van a evaluar.

    Retorna:
    list: Una lista con las mascotas que no están en la lista de mascotas prohibidas.
    """
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]  # Lista de mascotas prohibidas en España

    def no_prohibida(mascota):
        """
        Función interna que verifica si una mascota no está en la lista de mascotas prohibidas.
        
        Parámetros:
        mascota (str): El nombre de la mascota que se evaluará.

        Retorna:
        bool: True si la mascota no está prohibida, False en caso contrario.
        """
        return mascota not in mascotas_prohibidas  # Retorna True si la mascota no está prohibida

    mascotas_permitidas = filter(no_prohibida, lista_mascotas) # Filtra las mascotas permitidas usando la función no_prohibida

    return list(mascotas_permitidas) # Convertimos el resultado a lista y lo devolvemos

# Ejemplo de uso:
lista_mascotas = ["Elefante", "Gato", "Tigre", "Hamster", "Serpiente Pitón"]
resultado = filtrar_mascotas(lista_mascotas)
print(resultado)

#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente

def calcular_promedio(lista_numeros):
    """
    Esta función recibe una lista de números y calcula su promedio (media).
    Si la lista está vacía, devuelve un mensaje indicando que se deben añadir números a la lista.

    Parámetros:
    lista_numeros (list): Una lista de números (enteros o flotantes) para los cuales se calculará el promedio.

    Retorna:
    float o str: El promedio de los números si la lista no está vacía, o un mensaje de error si la lista está vacía.
    """
    try:
        return sum(lista_numeros) / len(lista_numeros) # Calcula el promedio dividiendo la suma de los números entre la cantidad de elementos
    except ZeroDivisionError:
        return "Añade número a la lista" # En caso de que la lista esté vacía y no se pueda dividir entre 0

# Ejemplo de uso:
lista_numeros = [6, 4,45,78,42]
calcular_promedio(lista_numeros)

#11.  Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente.

try:
    """
    Este bloque de código solicita al usuario que ingrese su edad y verifica si la edad ingresada
    es un valor numérico válido y si está dentro del rango permitido (0-120 años).

    Si la edad es válida (es decir, es un número dentro del rango de 0 a 120), imprime "La edad es valida".
    Si la edad está fuera de este rango, imprime "el valor esta fuera de rango".
    Si se ingresa un valor no numérico, se captura la excepción ValueError y se imprime "Ingresa un numero".
    """
    age = float(input("Ingresa tu edad: "))  # Solicita al usuario que ingrese su edad
    if 0 <= age <= 120:  # Verifica si la edad está en el rango válido
        print("La edad es valida")
    else:
        print("el valor esta fuera de rango")  # Si la edad está fuera del rango, imprime el mensaje
except ValueError:  # Captura el error si el usuario ingresa algo que no se puede convertir a número
    print("Ingresa un numero")  # Si ocurre un ValueError, informa al usuario

#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras(frase):
    """
    Esta función toma una frase como entrada, la divide en palabras y calcula la longitud de cada una.
    Retorna una lista con la longitud de cada palabra en la frase.

    Parámetros:
    frase (str): Una cadena de texto que contiene una frase compuesta por varias palabras.

    Retorna:
    list: Una lista de enteros donde cada elemento es la longitud de una palabra en la frase.
    """
    palabras = frase.split()  # Divide la frase en palabras usando el espacio como delimitador
    longitudes = list(map(len, palabras))  # Calcula la longitud de cada palabra
    return longitudes  # Retorna una lista con las longitudes de las palabras

# Ejemplo de uso:
frase = "mañana hace sol"
print(longitud_palabras(frase))

#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def transformador(conjunto):
    """
    Esta función toma un conjunto de caracteres y realiza dos transformaciones:
    1. Elimina los caracteres que no son letras (es decir, elimina números y símbolos).
    2. Para cada letra única, crea una tupla con la letra en mayúscula y minúscula.

    Parámetros:
    conjunto (set): Un conjunto de caracteres que puede contener letras, números y símbolos.

    Retorna:
    list: Una lista de tuplas, donde cada tupla contiene una letra en mayúscula y en minúscula.
    """
    conjunto_unico = set(filter(str.isalpha, conjunto))  # Elimina los caracteres no alfabéticos
    resultado = list(map(lambda letra: (letra.upper(), letra.lower()), conjunto_unico))  # Crea una lista de tuplas con mayúsculas y minúsculas

    return resultado

# Ejemplo de uso:
conjunto = {'a', 'b', 'A', 'c', 'C', '1', '@'}
transformador(conjunto)

#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def filtrador(lista):
    """
    Esta función recibe una lista de frutas y filtra aquellas que comienzan con la letra 'p'.
    
    Parámetros:
    lista (list): Una lista de nombres de frutas.
    
    Retorna:
    list: Una lista filtrada con las frutas que comienzan con la letra 'p'.
    """
    return [fruta for fruta in lista if fruta[0].lower() == 'p']  # Filtra las frutas que empiezan con 'p'

lista = ["platano", "papaya", "melocotón", "sandía", "pera"]

filtrador(lista)

#15. Crea una función lambda que  sume 3 a cada número de una lista dada.

# Lista de números
lista = [87953, 287, 289375]

def sumador_3(lista):
    """
    Esta función recibe una lista de números y suma 3 a cada elemento de la lista.
    
    Parámetros:
    lista (list): Una lista de números (enteros o flotantes) a los cuales se les sumará 3.
    
    Retorna:
    list: Una lista con los elementos originales de la lista, pero con 3 sumado a cada uno.
    """
    return list(map(lambda asumar: asumar + 3, lista))  # Suma 3 a cada elemento de la lista

sumador_3_resultado = sumador_3(lista) # Usamos la función sumador_3 para agregar 3 a cada número en la lista

print(sumador_3_resultado)

#16.  Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def funcion(texto, numero):
    """
    Esta función recibe un texto y un número. Divide el texto en palabras y filtra aquellas palabras
    cuya longitud sea mayor que el número proporcionado. Retorna una lista de las palabras filtradas.

    Parámetros:
    texto (str): Una cadena de texto que se dividirá en palabras.
    numero (int): Un número que se utilizará como umbral para filtrar las palabras. 
                  Solo se incluirán las palabras cuya longitud sea mayor que este número.

    Retorna:
    list: Una lista con las palabras filtradas, es decir, aquellas cuya longitud es mayor que 'numero'.
    """
    palabras = texto.split()  # Divide el texto en palabras utilizando espacios como delimitadores
    palabras_filtradas = filter(lambda palabra: len(palabra) > numero, palabras)  # Filtra las palabras cuya longitud es mayor que 'numero'
    return list(palabras_filtradas)  # Convierte el resultado de 'filter' en una lista y la retorna

# Ejemplo de uso:
texto = "El esternocleidomastoideo está dañado"
numero = 4
resultado = funcion(texto, numero)

print(resultado)

#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, 5,7,2 corresponde al número quinientos setenta y dos 572. Usa la función reduce()

from functools import reduce

def unidor_numeros(num_1, num_2):
    """
    Esta función recibe dos números y los concatena como cadenas de texto.

    Parámetros:
    num_1 (int): El primer número que será convertido a cadena.
    num_2 (int): El segundo número que será convertido a cadena.

    Retorna:
    str: La concatenación de los dos números convertidos a cadenas.
    """
    return str(num_1) + str(num_2)  # Convierte los números a cadenas y los concatena

lista_digitos = [2, 3, 6, 78]

resultado_reduce = reduce(unidor_numeros, lista_digitos) # Usamos reduce para concatenar todos los números de la lista

# Mostramos el resultado
print(f"El número concatenado es: {resultado_reduce}")

#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

info_estudiantes = [
    {"nombre": "Carlos", "edad": 20, "calificacion": 85},
    {"nombre": "Ana", "edad": 22, "calificacion": 92},
    {"nombre": "Luis", "edad": 19, "calificacion": 88},
    {"nombre": "María", "edad": 21, "calificacion": 95},
    {"nombre": "Sofía", "edad": 23, "calificacion": 78},
]

def filtrador(estudiante):
    """
    Esta función recibe un diccionario de un estudiante y verifica si su calificación es mayor o igual a 90.
    
    Parámetros:
    estudiante (dict): Un diccionario que contiene la información del estudiante (nombre, edad, calificación).
    
    Retorna:
    bool: Retorna True si la calificación es mayor o igual a 90, de lo contrario False.
    """
    return estudiante["calificacion"] >= 90  # Verifica si la calificación es mayor o igual a 90

estudiantes_calificacion_alta = list(filter(filtrador, info_estudiantes)) # Filtramos los estudiantes con calificación alta (mayor o igual a 90)

for estudiante in estudiantes_calificacion_alta: # Imprimimos los estudiantes con calificación alta
    print(estudiante)

#19. Crea una función lambda que filtre los números impares de una lista dada.

lista = [8273, 8974, 873, 874, 23, 77, 43, 55, 42]
impares = list(filter(lambda x: x % 2 != 0, lista)) # Usamos filter y lambda para obtener solo los números impares de la lista

print(impares)

#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

lista_mix = ["hola", 12, 464, "regalo", "flor"]

lista_int = lambda x: type(x) == int # Usando lambda con type() para filtrar solo los enteros

resultado = list(filter(lista_int, lista_mix))
print(resultado)

#21. Crea una función que calcule el cubo de un número dado mediante una función lambda

numero =17  
al_cubo = lambda x: x**3
al_cubo(numero)

#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() 

from functools import reduce

def multiplicador(num1, num2):
    """
    Esta función recibe dos números y devuelve su producto.
    
    Parámetros:
    num1 (int o float): El primer número a multiplicar.
    num2 (int o float): El segundo número a multiplicar.
    
    Retorna:
    int o float: El producto de num1 y num2.
    """
    return num1 * num2  # Devuelve el producto de los dos números

lista_numeros = [12, 43, 2, 3, 5]

resultado = reduce(multiplicador, lista_numeros) # Usamos reduce para multiplicar todos los números de la lista de forma acumulativa

# Imprimimos el resultado
print(resultado)

#23. Concatena una lista de palabras.Usa la función reduce() 

from functools import reduce

def unidor(pal1, pal2):
    """
    Esta función recibe dos cadenas de texto y las concatena con un espacio entre ellas.
    
    Parámetros:
    pal1 (str): La primera palabra o cadena de texto.
    pal2 (str): La segunda palabra o cadena de texto.
    
    Retorna:
    str: La concatenación de pal1 y pal2 con un espacio en el medio.
    """
    return pal1 + " " + pal2  # Concatenamos las dos palabras con un espacio entre ellas

lista_palabras = ["hola", "que", "tal", "estas"]

# Usamos reduce para concatenar todas las palabras en la lista
resultado = reduce(unidor, lista_palabras)

# Imprimimos el resultado
print(resultado)

#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() 

from functools import reduce

# Lista de números
lista_numeros = [1000000, 50000, 700, 12]

# Función para restar dos números
def diferenciador(num1, num2):
    """
    Esta función toma dos números y retorna su diferencia (num1 - num2).
    
    Parámetros:
    num1 (int o float): El primer número de la resta.
    num2 (int o float): El segundo número de la resta.
    
    Retorna:
    int o float: La diferencia entre num1 y num2.
    """
    return num1 - num2  # Resta num2 a num1

resultado = reduce(diferenciador, lista_numeros) # Usamos reduce para aplicar la función diferenciador de manera acumulativa

# Imprimimos el resultado
print(resultado)

#25. Crea una función que cuente el número de caracteres en una cadena de texto dada

cadena_de_texto = "esto es una cadena de texto"

contador = lambda x: len(x) # Función lambda que cuenta la longitud de una cadena

# Imprime la longitud de la cadena de texto
print(contador(cadena_de_texto))


#26. Crea una función lambda que calcule el resto de la división entre dos números dados

num1= 18
num2= 5
calculador_resto = lambda num1, num2: num1 % num2 # Función lambda que calcula el resto de la división de num1 por num2
print(calculador_resto(num1,num2))

#27. Crea una función que calcule el promedio de una lista de números.

lista_numeros = [2,5,7,3,5,2,5]
promedio = sum(lista_numeros)/len(lista_numeros) #Función que haya el promedio
print(promedio)

#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    """
    Busca y devuelve el primer elemento duplicado en una lista dada.
    Si no hay duplicados, devuelve None.

    :param lista: List - La lista donde buscar duplicados.
    :return: El primer elemento duplicado o None si no hay duplicados.
    """
    elementos_vistos = set()  # Crear un conjunto para almacenar elementos ya vistos
    for elemento in lista:  # Recorrer cada elemento de la lista
        if elemento in elementos_vistos:  # Si el elemento ya está en el conjunto
            return elemento  # Devolver el primer duplicado encontrado
        elementos_vistos.add(elemento)  # Si no está en el conjunto, añadirlo
    return None  # Si no se encuentra duplicado, devolver None

# Ejemplo de uso
mi_lista = [1, 2, "camión", 4, 5, 3, "camión", 7]
resultado = primer_duplicado(mi_lista)
print(f"El primer duplicado es: {resultado}")

#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro

variable = 666778899
def mask_variable(variable):
    """
    Convierte una variable en una cadena de texto y enmascara todos los caracteres 
    con el carácter '#', excepto los últimos cuatro.

    :param variable: La variable a convertir y enmascarar
    :return: Una cadena de texto enmascarada
    """
    variable_str = str(variable) # Convertir la variable a cadena
    
    masked = '#' * max(0, len(variable_str) - 4) + variable_str[-4:]  # Enmascarar todos los caracteres excepto los últimos cuatro
    
    return masked

resultado = mask_variable(variable)
print(resultado)  

#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    """
    Determina si dos palabras son anagramas.

    :param palabra1: Primera palabra (cadena de texto).
    :param palabra2: Segunda palabra (cadena de texto).
    :return: True si son anagramas, False de lo contrario.
    """
    palabra1 = ''.join(palabra1.lower().split()) # Eliminar espacios y convertir a minúsculas
    palabra2 = ''.join(palabra2.lower().split())


    return sorted(palabra1) == sorted(palabra2) # Verificar si tienen las mismas letras con la misma frecuencia

# Ejemplo de uso
print(son_anagramas("nacionalista", "altisonancia")) 

#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción

def buscador():
    """
    Esta función solicita al usuario una lista de nombres separados por comas, y luego solicita un nombre
    para buscar en esa lista. Si el nombre se encuentra en la lista, imprime "Fue encontrado", de lo contrario,
    lanza una excepción ValueError con un mensaje indicando que el nombre no está en la lista.

    No retorna ningún valor, pero imprime el resultado o el error correspondiente.
    """
    try:
        lista = input("Ingrese una lista de nombres separados por comas: ").split(",")  # Solicitar al usuario que ingrese una lista de nombres separados por comas
        
        lista = [nombre.strip() for nombre in lista] # Quitar espacios adicionales alrededor de los nombres
        
        nombre = input("Ingrese el nombre que desea buscar: ").strip() # Solicitar el nombre a buscar
        
        if nombre in lista: # Verificar si el nombre está en la lista
            print("Fue encontrado")
        else:    
            raise ValueError(f"El nombre '{nombre}' no está en la lista.") # Si el nombre no está, lanzar una excepción con un mensaje personalizado
    
    except ValueError as error:   
        print(error)    # Capturar y mostrar el mensaje de error
    
# Llamar a la función para ejecutarla
buscador()

#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscador(nombre_completo, lista_empleados):
    """
    Busca el puesto de un empleado en una lista de empleados.

    Args:
        nombre_completo (str): Nombre completo del empleado a buscar.
        lista_empleados (list): Lista de diccionarios, cada uno representando un empleado con 'nombre' y 'puesto'.

    Returns:
        str: El puesto del empleado si está en la lista, o un mensaje indicando que no trabaja aquí.
    """
    for empleado in lista_empleados: #iteramos la lista
        if empleado.get('nombre') == nombre_completo: #comparamos el nombre en la lista
            return empleado.get('puesto') #devuelve el puesto si está en la lista
    return f"La persona '{nombre_completo}' no trabaja aquí."
lista_empleados = [
    {"nombre": "Juan Pérez", "puesto": "Gerente"},
    {"nombre": "Ana Gómez", "puesto": "Desarrolladora"},
    {"nombre": "Luis Martínez", "puesto": "Analista"}
]

nombre_buscar = "Juan Pérez"
comprobacion = buscador(nombre_buscar,lista_empleados)
print(comprobacion)

#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumador = lambda lista_1, lista_2: list(map(lambda x, y: x + y, lista_1, lista_2)) # Función lambda para sumar los elementos de dos listas

lista_1 = [12, 16, 23, 32]
lista_2 = [44, 12, 21, 3]

# Llamada a la función y mostrar el resultado
print(sumador(lista_1, lista_2))

#34. Crea la clase 
"""Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
crecer_tronco , 
nueva_rama , 
crecer_ramas , 
quitar_rama e 
info_arbol . El objetivo es implementar estos métodos para 
manipular la estructura del árbol.
 Código a seguir:
 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
 2. Implementar el método 
crecer_tronco para aumentar la longitud del tronco en una unidad.
 3. Implementar el método 
nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
 4. Implementar el método 
crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
 5. Implementar el método 
quitar_rama para eliminar una rama en una posición específica.
 6. Implementar el método 
info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las 
mismas.
 Caso de uso:
 1. Crear un árbol.
 2. Hacer crecer el tronco del árbol una unidad.
 3. Añadir una nueva rama al árbol.
 4. Hacer crecer todas las ramas del árbol una unidad.
 5. Añadir dos nuevas ramas al árbol.
 6. Retirar la rama situada en la posición 2.
 7. Obtener información sobre el árbol."""

class Arbol:
    
    def __init__(self):
        self.longitud = 1  # La longitud inicial del tronco
        self.ramas = []  # Lista para almacenar las ramas

    def crecer_tronco(self):
        """Hace crecer el tronco una unidad."""
        self.longitud += 1

    def nueva_rama(self):
        """Añade una nueva rama al árbol, inicializando su longitud en 1."""
        self.ramas.append(1)

    def crecer_ramas(self):
        """Hace crecer todas las ramas del árbol una unidad."""
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, indice):
        """Elimina una rama especificada por el índice de la lista de ramas."""
        if 0 <= indice < len(self.ramas):
            self.ramas.pop(indice)
        else:
            print("Índice de rama no válido")

    def info_arbol(self):
        """Devuelve un diccionario con la información del árbol."""
        return {
            "longitud": self.longitud,
            "numero_ramas": len(self.ramas),
            "longitud_ramas": self.ramas,
        }

if __name__ == "__main__":
    arbol = Arbol()  # Crear un árbol
    arbol.crecer_tronco()  # Hacer crecer el tronco del árbol una unidad
    arbol.nueva_rama()  # Añadir una nueva rama al árbol
    arbol.crecer_ramas()  # Hacer crecer todas las ramas del árbol una unidad
    arbol.nueva_rama()  # Añadir dos nuevas ramas al árbol
    arbol.nueva_rama()
    arbol.quitar_rama(2)  # Retirar la rama situada en la posición 2 (índice 2)
    
    info = arbol.info_arbol()  # Obtener la información del árbol
    print("Información del árbol:")
    print(f"Longitud del tronco: {info['longitud']}")
    print(f"Número de ramas: {info['numero_ramas']}")
    print(f"Longitudes de las ramas: {info['longitud_ramas']}")


#36.Crea la clase 
"""UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta 
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y 
agregar dinero al saldo.
 Código a seguir:
  Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante 
 Implementar el método 
True y 
False .
 retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no 
poder hacerse.
  Implementar el método 
transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. 
Lanzará un error en caso de no poder hacerse.
  Implementar el método 
agregar_dinero para agregar dinero al saldo del usuario.
 Caso de uso:
 Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
 2
Agregar 20 unidades de saldo de "Bob".
 Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
  Retirar 50 unidades de saldo a "Alicia" """

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente): #Metodo para crear los usuarios con nombre, saldo y si tienen cuenta corriente
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):  #Metodo para retirar dinero con sus respectivos errores con respecto a quedarse en negativo
        try:
            if cantidad <= 0:
                raise ValueError("La cantidad a retirar debe ser mayor que cero.")
            if self.saldo < cantidad:
                raise ValueError(f"Saldo insuficiente. Saldo actual: {self.saldo}")
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad} unidades. Saldo restante: {self.saldo}")
        except ValueError as e:
            print(f"Error al retirar dinero: {e}")

    def transferir_dinero(self, otro_usuario, cantidad): #Metodo para transferir dinero con sus respectivos errores con respecto a quedarse en negativo
        try:
            if cantidad <= 0:
                raise ValueError("La cantidad a transferir debe ser mayor que cero.")
            if self.saldo < cantidad:
                raise ValueError(f"Saldo insuficiente para la transferencia. Saldo actual: {self.saldo}")
            self.saldo -= cantidad
            otro_usuario.agregar_dinero(cantidad)
            print(f"Se han transferido {cantidad} unidades a {otro_usuario.nombre}. Saldo restante: {self.saldo}")
        except ValueError as e:
            print(f"Error al transferir dinero: {e}")

    def agregar_dinero(self, cantidad): #Metodo para agregar dinero
        try:
            if cantidad <= 0:
                raise ValueError("La cantidad a agregar debe ser mayor que cero.")
            self.saldo += cantidad
            print(f"Se han agregado {cantidad} unidades. Saldo actual: {self.saldo}")
        except ValueError as e:
            print(f"Error al agregar dinero: {e}")


# Caso de uso
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# Agregar 20 unidades de saldo a Bob
bob.agregar_dinero(20)

# Hacer una transferencia de 80 unidades desde Bob a Alicia
bob.transferir_dinero(alicia, 80)

# Retirar 50 unidades de saldo a Alicia
alicia.retirar_dinero(50)

#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: reemplazar_palabras , procesar_texto .contar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función 
"""Código a seguir:
 Crear una función 
contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene 
que devolver un diccionario.
 Crear una función 
reemplazar_palabras para remplazar una 
que devolver el texto con el remplazo de palabras.
 Crear una función 
palabra_original del texto por una 
palabra_nueva . Tiene 
eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra 
eliminada.
 Crear la función 
procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un 
número de argumentos variable según la opción indicada.
 Caso de uso:
 Comprueba el funcionamiento completo de la función 
procesar_text"""

def contar_palabras(texto):
    """
    Cuenta el número de veces que aparece cada palabra en el texto.
    Devuelve un diccionario con las palabras como claves y su frecuencia como valores.
    """
    palabras = texto.split() #Dividimos el texto en sus palabras
    conteo = {}  #creamos ser vacío
    for palabra in palabras: #iteramos sobre cada palabra
        palabra = palabra.lower()  # Convertimos a minúsculas para evitar duplicados por mayúsculas/minúsculas
        if palabra in conteo: #buscamos las palabras en el set
            conteo[palabra] += 1 #si ya estaba +1
        else:
            conteo[palabra] = 1 #si no estaba =1
    return conteo


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Reemplaza todas las ocurrencias de palabra_original por palabra_nueva en el texto.
    Devuelve el texto con las palabras reemplazadas.
    """
    return texto.replace(palabra_original, palabra_nueva) #usamos funcion replace para cambiar las palabras


def eliminar_palabra(texto, palabra_a_eliminar):
    """
    Elimina todas las ocurrencias de palabra_a_eliminar del texto.
    Devuelve el texto con la palabra eliminada.
    """
    palabras = texto.split() #Dividimos el texto en sus palabras
    palabras_filtradas = [palabra for palabra in palabras if palabra != palabra_a_eliminar] #hacemos una lista de palabras con las palabras distintas a las palabras a elimiar
    return ' '.join(palabras_filtradas) #hacemos un string con todas las palabras_filtrdas con espacio entre ellas
    


def procesar_texto(texto, opcion, *args): #utilizamos args pues segun la función el número de argumetos es variables
    """
    Procesa el texto según la opción indicada.
    Las opciones disponibles son:
    - "contar": llama a contar_palabras y devuelve el conteo.
    - "reemplazar": requiere dos argumentos (palabra_original, palabra_nueva).
    - "eliminar": requiere un argumento (palabra_a_eliminar).
    """
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar" and len(args) == 2: #para esta opción hace falta además del reempazar 2 argumentos
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar" and len(args) == 1: #para esta opción hace falta además del eliminar 1 argumentos
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción no válida o argumentos insuficientes."


# Caso de uso
texto = "Hola mundo, hola universo. El mundo es grande y el universo es infinito."
print("Resultado de contar palabras:")
print(procesar_texto(texto, "contar"))

print("\nResultado de reemplazar palabras:")
print(procesar_texto(texto, "reemplazar", "mundo", "planeta"))

print("\nResultado de eliminar palabra:")
print(procesar_texto(texto, "eliminar", "universo"))


#38 Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def determinar_momento_del_dia(hora):
    """
    Determina si es de día, tarde o noche según la hora ingresada.
    Parámetros:
        hora (int): La hora en formato 24 horas.
    Retorno:
        str: Momento del día ("Día", "Tarde" o "Noche").
    """
    if 7 <= hora < 14:
        return "Es de día (mañana)."
    elif 14 <= hora < 20:
        return "Es de tarde."
    elif (20 <= hora <= 23) or (0 <= hora < 7):
        return "Es de noche."
    else:
        return "Hora no válida. Por favor, ingresa un valor entre 0 y 23."

try:
    hora = int(input("Ingresa la hora en formato 24 horas (0-23): ")) # Solicitar al usuario la hora
    resultado = determinar_momento_del_dia(hora)
    print(resultado)
except ValueError:
    print("Por favor, ingresa un número entero válido.")

#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
"""Las reglas de calificación son:
  0  69 insuficiente
  70  79 bien
  80  89 muy bien
  90  100 excelente"""

def calificador(nota):
    """
    Esta función clasifica una nota en diferentes categorías según su valor.
    
    Parámetros:
    nota (int o float): La nota del estudiante que se va a clasificar.
    
    Retorna:
    str: La categoría en la que se encuentra la nota.
    """
    if 90 <= nota <= 100:
        return "excelente"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 70 <= nota <= 79:
        return "bien"
    elif 0 <= nota <= 69:
        return "insuficiente"
    else:
        return "nota no valida"

#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" ,"circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math  # Importamos el módulo math para utilizar el valor de pi

def area(figura, datos):
    """
    Esta función calcula el área de diferentes figuras geométricas (rectángulo, círculo, triángulo).
    
    Parámetros:
    figura (str): El tipo de figura para la cual se va a calcular el área.
    datos (tuple): Los datos necesarios para calcular el área. Depende de la figura:
        - Para un rectángulo: (base, altura)
        - Para un círculo: (radio)
        - Para un triángulo: (base, altura)
    
    Retorna:
    float: El área calculada de la figura.
    
    Lanza:
    ValueError: Si se pasa un tipo de figura no válido.
    """
    
    if figura == "rectangulo":
        base, altura = datos  # Desempaquetamos los valores de base y altura
        return base * altura
    elif figura == "circulo":
        radio = datos  # Asumimos que 'datos' es una tupla con un solo valor (el radio)
        return math.pi * radio**2
    elif figura == "triangulo":
        base, altura = datos  # Desempaquetamos base y altura para el triángulo
        return base * altura / 2
    else:
        raise ValueError("Usa una figura válida (rectangulo, circulo, triangulo)") # Si la figura no es válida, lanzamos un error

# Ejemplo de uso:
print(area("triangulo", (2, 63)))  # Área de un triángulo con base 2 y altura 63

#41.   En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
"""1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor 
a cero). Por ejemplo, descuento de 15€. 
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu 
programa de Python"""

def programa_precio():
    """
    Esta función calcula el precio final de un producto considerando un posible descuento aplicado
    mediante un cupón. El usuario debe ingresar el precio original y, si tiene un cupón de descuento,
    debe ingresar el valor del descuento.
    
    Si el valor del cupón es válido (mayor a 0), se aplica el descuento. Si no, se muestra el precio
    original sin descuentos.
    
    Retorna:
    float: El precio final después de aplicar el descuento (si aplica).
    """
    try:
        precio_original = float(input("Introduce el precio original del producto: "))
        
        cupon_descuento = input()
        if cupon_descuento == "sí":
            try:
                descuento = float(input("Introduce el valor del descuento: "))
                if descuento > 0:
                    precio_final = precio_original - descuento
                    return precio_final
                else:
                    print ("El cupón debe ser superior a 0€")
            except ValueError:
                print ("por favor intrude un número en el descuento")
        elif cupon_descuento == "no":  
            precio_final = precio_original
            return precio_final
        else:
            print ("Debe seleccionar sí o no")   
    except ValueError:
        print ("por favor intrude un número en el precio original")         
programa_precio()
 
 
 
