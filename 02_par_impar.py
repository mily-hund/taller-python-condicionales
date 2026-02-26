numero = int(input("Puedes decirme un numero?: "))
if numero%2 == 0:
    print("Es un numero par")
else:
    print("Es un numero impar")

edad = int(input("Ahora puede decirme tu edad?: "))
if edad<0:
    print("No existen edades negativas")
else:
    if edad>=18:
        print("Eres mayor de edad") 
    else:
        print("Eres menor de edad")
