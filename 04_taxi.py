distancia = float(input("Cual fue la distancia recorridda de tu viaje en km?: "))
while distancia<=0 :
    distancia = float(input("no se aceptan distancias negativas o iguales a 0: "))
tiempo = int(input("A que hora del dia comenzo tu viaje?: "))
tarifa = 1
while tiempo<0 or tiempo>23:
    tiempo = int(input("El dia solo tiene horas entre el 0 y el 23, ingresa de nuevo: "))
if distancia>10 :
    tarifa = 2
    if 6<=tiempo<=19:
        total = tarifa + (distancia*0.5)
        print("Horario:    diurno")
        print(f"Distanciaa:    {distancia}")
        print(f"total a pagar:    {total}")
    elif 20<=tiempo<=23 or 0<=tiempo<=5:
        total= tarifa + (distancia*0.65)
        print("Horario:    nocturno")
        print(f"Distanciaa:    {distancia}")
        print(f"total a pagar:    {total}")
else:
    tarifa = 1
    if 6<=tiempo<=19:
        total = tarifa + (distancia*0.5)
        print("Horario:    diurno")
        print(f"Distanciaa:    {distancia}")
        print(f"total a pagar:    {total}")
    elif 20<=tiempo<=23 or 0<=tiempo<=5:
        total= tarifa + (distancia*0.65)
        print("Horario:    nocturno")
        print(f"Distanciaa:    {distancia}")
        print(f"total a pagar:    {total}")
