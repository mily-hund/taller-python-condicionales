nota_1 = float(input("Ingresa tu calificacion de la primera nota: "))
if nota_1<0 or nota_1>100 :
    print("Esa calificacion no es valida")
    raise SystemExit

nota_2 = float(input("Ingresa tu calificacion de la segunda nota: "))
if nota_2<0 or nota_2>100 :
    print("Esa calificacion no es valida")
    raise SystemExit

nota_3 = float(input("Ingresa tu calificacion de la tercera nota: "))
if nota_3<0 or nota_3>100 :
    print("Esa calificacion no es valida")
    raise SystemExit

promedio = (nota_1+nota_2+nota_3)/3

if 90<=promedio<=100:
    print(f"Nota 1:         {nota_1}")
    print(f"Nota 2:         {nota_2}")
    print(f"Nota 3:         {nota_3}")
    print(f"Promedio:       {promedio}")
    print(f"Clasificacion:  Excelente")
elif 80<=promedio<90:
    print(f"Nota 1:         {nota_1}")
    print(f"Nota 2:         {nota_2}")
    print(f"Nota 3:         {nota_3}")
    print(f"Promedio:       {promedio}")
    print(f"Clasificacion:  Muy bueno")
elif 70<=promedio<80:
    print(f"Nota 1:         {nota_1}")
    print(f"Nota 2:         {nota_2}")
    print(f"Nota 3:         {nota_3}")
    print(f"Promedio:       {promedio}")
    print(f"Clasificacion:  Bueno")
elif 60<=promedio<70:
    print(f"Nota 1:         {nota_1}")
    print(f"Nota 2:         {nota_2}")
    print(f"Nota 3:         {nota_3}")
    print(f"Promedio:       {promedio}")
    print(f"Clasificacion:  Supletorio")
else:
    print(f"Nota 1:         {nota_1}")
    print(f"Nota 2:         {nota_2}")
    print(f"Nota 3:         {nota_3}")
    print(f"Promedio:       {promedio}")
    print(f"Clasificacion:  Reprobado")