#librerias
from datetime import datetime


#funciones 
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


def mostrar_perdidas():
    print("\nTotal de perdidas:", total_perdidas)
    print()
# este esta incompleto conpletalo 
def consultar_producto():
    if len(inventario) == 0:
        print("\nNo hay productos.")
        print()
        return

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
#            mostrar_perdidas()
        elif opcion == 3:
            consultar_producto()
#        elif opcion == 4:
#            borrar_producto()
#        elif opcion == 5:
            print("Saliendo...")
        else:
            print("Opcion invalida")
            print()





menu()
