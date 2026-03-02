subtotal = float(input("Cual es el subtotal de tu cuenta?: "))
while subtotal<=0:
    subtotal = int(input("No existe una cuenta menor o igual a cero, vuelve a ingresar: "))

cliente = input("El cliente es vip o regular?: ")
while cliente != "vip" and cliente != "regular" :
    cliente = input("Solo se puede ingresar \"vip\" o \"regular\": ")
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

