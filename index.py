from datetime import datetime

# variables
inventario = []
total_perdidas = 0

# funciones
def agregar_producto():
    global total_perdidas

    print("\n--- Agregar Producto ---")
    try:
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
            total_perdidas += perdida

        producto = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio,
            "fecha": fecha_vencimiento,
            "estado": estado
        }

        inventario.append(producto)
        print("Producto guardado\n")
    except ValueError:
        print("Error: entrada inválida. Intente de nuevo.\n")


def mostrar_perdidas():
    print("\nTotal de pérdidas:", total_perdidas, "\n")


def consultar_producto():
    if len(inventario) == 0:
        print("\nNo hay productos.\n")
        return

    print("\nLista de productos:")
    for i, producto in enumerate(inventario, start=1):
        print(i, "-", producto["nombre"])
    
    try:
        numero = int(input("Número del producto: "))
        if 1 <= numero <= len(inventario):
            producto = inventario[numero - 1]
            print("\nDatos del producto:")
            print("Nombre:", producto["nombre"])
            print("Cantidad:", producto["cantidad"])
            print("Precio:", producto["precio"])
            print("Fecha:", producto["fecha"].strftime("%d/%m/%Y"))
            print("Estado:", producto["estado"], "\n")
        else:
            print("Número incorrecto\n")
    except ValueError:
        print("Entrada inválida, debe ser un número.\n")


def borrar_producto():
    if len(inventario) == 0:
        print("\nNo hay productos para borrar.\n")
        return

    print("\nProductos registrados:")
    for i, producto in enumerate(inventario, start=1):
        print(i, "-", producto["nombre"])
    
    try:
        numero = int(input("Número del producto a borrar: "))
        if 1 <= numero <= len(inventario):
            inventario.pop(numero - 1)
            print("Producto eliminado.\n")
        else:
            print("Número incorrecto\n")
    except ValueError:
        print("Entrada inválida, debe ser un número.\n")


def menu():
    opcion = 0

    while opcion != 5:
        print("===== INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Mostrar pérdidas")
        print("3. Consultar producto")
        print("4. Borrar producto")
        print("5. Salir")

        try:
            opcion = int(input("Opción: "))
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
                print("Opción inválida\n")
        except ValueError:
            print("Entrada inválida, debe ser un número.\n")


# ejecutar menú
menu()
