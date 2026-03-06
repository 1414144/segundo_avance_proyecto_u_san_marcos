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


menu()