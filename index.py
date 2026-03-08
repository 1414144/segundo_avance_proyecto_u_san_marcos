# librerias
from datetime import datetime

# variables
inventario = []
total_perdidas = 0

#funciones
# funciones
def agregar_producto():
    global total_perdidas

    print("\n--- Agregar Producto ---")

    nombre = input("Nombre: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    fecha_texto = input("Fecha vencimiento (DD/MM/AAAA): ")

    fecha_vencimiento = datetime.strptime(fecha_texto, "%d/%m/%Y")
    fecha_hoy = datetime.now()

    estado = "DISPONIBLE"

    if fecha_vencimiento < fecha_hoy:
        estado = "VENCIDO"
        perdida = cantidad * precio
        total_perdidas = total_perdidas + perdida

    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio,
        "fecha": fecha_vencimiento,
        "estado": estado
    }

    inventario.append(producto)

print("Producto guardado")
    print()

def mostrar_perdidas():
    print("\nTotal de perdidas:", total_perdidas)
    print()


def consultar_producto():
    if len(inventario) == 0:
        print("\nNo hay productos.")
        print()
        return

    print("\nLista de productos:")

    contador = 1
    for producto in inventario:
        print(contador, "-", producto["nombre"])
        contador = contador + 1

    numero = int(input("Numero del producto: "))

    if numero > 0 and numero <= len(inventario):
        producto = inventario[numero - 1]

        print("\nDatos del producto:")
        print("Nombre:", producto["nombre"])
        print("Cantidad:", producto["cantidad"])
        print("Precio:", producto["precio"])
        print("Fecha:", producto["fecha"].strftime("%d/%m/%Y"))
        print("Estado:", producto["estado"])
        print()
    else:
        print("Numero incorrecto")
        print()


def borrar_producto():
    global total_perdidas

    if len(inventario) == 0:
        print("\nNo hay productos para borrar.")
        print()
        return

    print("\nProductos registrados:")

    contador = 1
    for producto in inventario:
        print(contador, "-", producto["nombre"])
        contador = contador + 1

    numero = int(input("Numero del producto a borrar: "))

    if numero > 0 and numero <= len(inventario):
        producto = inventario[numero - 1]

        if producto["estado"] == "VENCIDO":
            perdida = producto["cantidad"] * producto["precio"]
            total_perdidas = total_perdidas - perdida

        inventario.pop(numero - 1)

        print("Producto eliminado.")
        print()
    else:
        print("Numero incorrecto")
        print()


def menu():
    opcion = 0

    while opcion != 5:
        print("===== INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Mostrar perdidas")
        print("3. Consultar producto")
        print("4. Borrar producto")
        print("5. Salir")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            mostrar_perdidas()
        elif opcion == 3:
            consultar_producto()
        elif opcion == 4:
            borrar_producto()
        elif opcion == 5:
            print("Saliendo...")
        else:
            print("Opcion invalida")
            print()
def borrar_producto():
    global total_perdidas

    if len(inventario) == 0:
        print("\nNo hay productos para borrar.")
        print()
        return

    print("\nProductos registrados:")

    contador = 1
    for producto in inventario:
        print(contador, "-", producto["nombre"])
        contador = contador + 1

    numero = int(input("Numero del producto a borrar: "))

    if numero > 0 and numero <= len(inventario):
        producto = inventario[numero - 1]

        if producto["estado"] == "VENCIDO":
            perdida = producto["cantidad"] * producto["precio"]
            total_perdidas = total_perdidas - perdida

        inventario.pop(numero - 1)

        print("Producto eliminado.")
        print()
    else:
        print("Numero incorrecto")
        print()

menu()
