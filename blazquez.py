print("Bienvenido al sistema de ordenamiento de 3 números distintos.")
num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))
num3 = float(input("Ingrese otro numero: "))
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"{num3}, {num2}, {num1}")
    elif num3 > num2:
        print(f"{num2}, {num3}, {num1}")
elif num2 > num1 and num2 > num3:
    if num1 > num3:
         print(f"{num3}, {num1}, {num2}")
    elif num3 > num1:
        print(f"{num1}, {num3}, {num2}")
elif num3 > num1 and num3 > num2:
    if num1 > num2:
         print(f"{num2}, {num1}, {num3}")
    elif num2 > num1:
        print(f"{num1}, {num2}, {num3}")
