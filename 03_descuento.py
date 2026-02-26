subtotal = float(input("Cual es el subtotal de tu cuenta?: "))


if subtotal<0:
    print("No existen subtotales negativos")
else: 
    cliente = input("El cliente es vip o regular?: ")
    if cliente == "vip":
        descuento = subtotal*0.15
        porcentaje = "15%"
    elif cliente == "regular" and subtotal>=100:
        descuento = subtotal*0.05
        porcentaje = "5%"
    elif cliente == "regular" and subtotal<100:
        descuento = 0
        porcentaje = "0%"
    print("Su cuenta final es: ")
    print(f"subotal:   {subtotal}")
    print(f"descuento aplicado:   {porcentaje}")
    print(f"total:   {subtotal-descuento} ")

