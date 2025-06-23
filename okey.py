x = 21
y = 18

division = x / y
print(division)

resta = x - y
print(resta)

suma = x+y
print(suma)

multiplicacion = x * y
print(multiplicacion)

modulo = x & y
print(modulo)

exponente = x ** y
print(exponente)

division_entera = x // y
print(division_entera)

a = True
b = False
resultado = a and b
print(resultado)

#ejercicios

#ejercicio 1
nombre = "fabian"
edad = 18
ciudad = "maracaibo"

print (f"hola soy ", nombre, "tengo" , edad, " y mi ciudad es", ciudad,)

#ejercicio 2
matematica = 15
lenguaje = 18
programacion = 20
calificacion =(  matematica + lenguaje + programacion) / 3
print(f"el promedio de las 3 materias es =", calificacion,)

#introducir desde consola 
nomb = input("introdusca su nombre ")
print(f"tu nombre es: ",nomb,)

edad1 = int(input("cual es tu edad? "))
print(f"tu edad es de:",edad1,)

#ejercicio 3

numb1 = int(input("ingrese el primer numero: "))
numb2 = int(input("ingrese el segundo numero: "))

division1 = numb1 / numb2
print(f"la division de su dos numero es:",division,)

resta = numb1 - numb2
print(f"la resta de su dos numero es:",resta,)

suma = numb1 + numb2
print(f"la suma de su dos numero es:",suma,)

multiplicacion = numb1 * numb2
print(f"la multiplicacion de su dos numero es:",multiplicacion,)

#ejercicio 4
numb3 = int(input("ingrese un numero: "))

modulo1 = numb3 % 2


#condicionales
calificacion1 = int(input("ingrese su calificacion: "))
 
if calificacion1 >= 90:
    print("obtuviste una A")
elif calificacion1 >= 80:
    print("obtuviste una B")
elif calificacion1 >= 70:
    print("obtuviste una C")
elif calificacion1 >= 60:
    print("obtuviste una F")
elif calificacion1 <= 59:
    print("obtuviste una F")
