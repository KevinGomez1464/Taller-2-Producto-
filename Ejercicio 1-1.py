def hola_mundo():
    print("¡Hola, mundo!")

def suma_de_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    suma = num1 + num2
    print(f"La suma de {num1} y {num2} es igual a {suma}")

def calcular_edad():
    año_actual = 2024
    año_nacimiento = int(input("Ingrese su año de nacimiento: "))
    edad = año_actual - año_nacimiento
    print(f"Tienes {edad} años.")

def calcular_imc():
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = peso / (altura ** 2)
    print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")

def hallar_numero_impar():
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        numero += 1
    print(f"El siguiente número impar es: {numero}")

def area_cuadrado():
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    area = lado ** 2
    print(f"El área del cuadrado es: {area:.2f} unidades cuadradas")

def area_triangulo():
    base = float(input("Ingrese la longitud de la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = 0.5 * base * altura
    print(f"El área del triángulo es: {area:.2f} unidades cuadradas")

def validar_mayor_menor_edad():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")


while True:
    print("\nMenú de ejercicios:")
    print("1. Hola mundo")
    print("2. Suma de números")
    print("3. Calcular la edad")
    print("4. IMC")
    print("5. Hallar el siguiente número impar")
    print("6. Hallar el área de un cuadrado")
    print("7. Hallar el área de un triángulo")
    print("8. Validar si es mayor o menor de edad")
    print("9. Validar aumento de salario")
    print("10. Pago de horas extras")
    opcion = int(input("Seleccione un ejercicio (1-10): "))

    if opcion == 1:
        hola_mundo()
    elif opcion == 2:
        suma_de_numeros()
    elif opcion == 3:
        calcular_edad()
    elif opcion == 4:
        calcular_imc()
    elif opcion == 5:
        hallar_numero_impar()
    elif opcion == 6:
        area_cuadrado()
    elif opcion == 7:
        area_triangulo()
    elif opcion == 8:
        validar_mayor_menor_edad()
    else:
        print("Opción inválida. Intente nuevamente.")
