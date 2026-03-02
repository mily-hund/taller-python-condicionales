numero = int(input("Puedes decirme un numero?: "))
if numero == 0:
    print("El numero es cero")
elif numero%2 == 0 :
    print("Es un numero par")
else:
    print("Es un numero impar")

edad = int(input("Ahora puede decirme tu edad?: "))
while edad <= 0:
    edad = int(input("La edad no puede ser menor o igual a cero, vuelve a intentarlo: "))
if edad<0:
    print("No existen edades negativas")
else:
    if edad>=18:
        print("Eres mayor de edad") 
    else:
        print("Eres menor de edad")
