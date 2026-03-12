print("bienvenido al programa de ventas")

nommbre_producto = input("ingrese el nombre del producto: ")
precio_producto = float(input("ingrese el precio del producto: "))    
while precio_producto < 0:
    print("el precio no puede ser negativo, por favor ingrese un precio valido")
    precio_producto = float(input("ingrese el precio del producto: "))  
cantidad_producto = int(input("ingrese la cantidad del producto: "))    
while cantidad_producto < 0:
    print("la cantidad no puede ser negativa, por favor ingrese una cantidad valida")
    cantidad_producto = int(input("ingrese la cantidad del producto: "))

total_venta = precio_producto * cantidad_producto
print(f"usted ha comprado: producto: {nommbre_producto}, precio: {precio_producto}, cantidad: {cantidad_producto}")
print(f"el total de la venta es: {total_venta}")


