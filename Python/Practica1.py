'''
from operator import truediv


miVariable = 3
print(miVariable)
miVariable = "Hola a todos los alumnos de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable) 
x = 10
y = 2
z = x + y
print(z)
print(id(x)) #Aca tenemos el id de memoria donde se guarda x- Estamos usando 2 variables. print+id
#Las literales se escriben x624-La memoria borra y guarda y puede cambiar el id de la literal

#a = 10
a:str = "Hola alumnos"#Se puede poner que es string, es una referencia- todas las variables son dinamicas
print(type(a)) #Esto sirve para mostrar el tipo de variable que es
a = True #ACa nos dice que es un tipo de dato booleano
#Tipos int, float, string, bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))
#Manejo de cadenas(String)
miGrupoFavorito = "The Letter Black"+" "+"The Best Rock Band"
caracteristicas = "The best rock band"
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)#Esto seria una concatenacion

numero1 = "7"
numero2 = "8"
print(numero1+numero2)#aca no se sumaron los valores sino que se hizo una concatenacion.No se puede sumar un string +string
print(int(numero1) +int(numero2))#Al ponerle un int nos suma las variables. Int es de tipo entero

#Tipos de datos Booleanos (bool)No permite saber si es VOF
miBooleano = True
print(miBooleano) 
miBooleano = 1 > 2

if miBooleano:
   print("El resultado es verdadero")
else :
   print("el resultado es falso")

#Procesar la entrada del usuario
#Funcion INPUT
Resultado = input("Digite un numero: ")#La funcion input regresa un dato del tipo string
print(Resultado)

#Conversion de la entrada de datos
numero1 = int(input("escribe el primer numero: "))#No olvidar ponerle el int antes del input porque sino no suma sino concatena
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: , resultado")'''
'''
operandoA=8
operandoB=5
suma=operandoA+operandoB
#print("Resultao de la suma; ",suma)
print(f'El resultado es :{suma}')#A esto se le llama interpolacion. Seria incluir la variable dentro de una cadena-Este metodo sirve para cuando necesitamos suma varias lines

resta = operandoA - operandoB
print(f"El resultado de la resta es:{resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operandoA/operandoB
print(f"El resultado de la division es:{division}")
division=operandoA// operandoB
print(f"El resultado de la division (int)es:{division}")#Este tipo de division nos permite ver el resultado entero
modulo = operandoA % operandoB
print(f"El resultado de la division o residuo(modulo)es:{modulo}")#Seria el residuo de la division 8/5
exponente = operandoA ** operandoB
print(f"El resultado del exponentees:{exponente}")'''
'''
#Ejercicio Rectangulo
from tkinter import ANCHOR


alto = int(input("Proporciona el alto del rectangulo: "))
ancho = int(input("Propociona el ancho del rectangulo:"))
area=alto*ancho
perimetro=(alto+ancho)*2
print("Area:",area)
print("Perimetro: ",perimetro)'''
'''
miVariable3 = 10
print(miVariable3)#Le estamos asignando un valor a la variable

#Operadores de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)
miVariable3+=1
print(miVariable3)

#miVariable3=miVariable3-2
miVariable3-=2
print(miVariable3)

#miVariable3=miVariable3*2
miVariable3*=3
print(miVariable3)

#miVariable3=miVariable3/2
miVariable3/=2
print(miVariable3)'''
'''
#Operadores de Comparacion
d=4
b=2
resultado= d==b #Comprobamos si son iguales
print(resultado)

#Operador diferente
resultado=d!=b
print(resultado)

#Operador menor que 
resultado = d < b
print(resultado)

#Operador mayor que 
resultado = d <= b
print(resultado)'''

#Operadores Logicos
from ast import Not


a=False
b=True
resultado=a and b
print(resultado)

#Operador OR
resultado=a or b
print(resultado)

#Operador NOT
resultado= not a #Es unario. Solo necesita de un operador para trabajar
print(resultado)

