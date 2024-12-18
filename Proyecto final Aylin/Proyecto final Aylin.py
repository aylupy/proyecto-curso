import os

index_global = 3
inventario = {1: {"nombre": "Jugo Cepita de naranja", "stock": 10, "precio": 2500, "categoria": "Bebidas", "marca": "Cepita"},
              2: {"nombre": "Papas Lays", "stock": 15, "precio": 2300, "categoria": "Snacks", "marca": "Lays"},
              3: {"nombre": "Alfajor Rasta", "stock": 7, "precio": 1500, "categoria": "Golosinas", "marca": "Rasta"}}


def limpiar_consola():
    #Limpiar la consola para una mejor visualización.
    os.system("cls")


def mostrar_mensaje(mensaje):
    #Mostrar mensajes al usuario.
    print(mensaje)
    input("Presione Enter para continuar...")


def chequeo_datos_producto(precio, stock):
    #Chequea y valida los datos del producto ingresados por el usuario.
    if precio <= 0 or stock <= 0:
        mostrar_mensaje("Datos incorrectos, el precio y el stock deben ser mayores a cero.")
        return False
    return True


def registrar_producto(datos_producto):
    #Registrar un nuevo producto.
    global index_global
    index_global += 1
    inventario[index_global] = datos_producto
    limpiar_consola()
    mostrar_mensaje(f"Producto '{datos_producto['nombre']}' registrado exitosamente.")


def mostrar_productos():
    #Mostrar todos los productos registrados.
    limpiar_consola()
    print("<----- Lista de Productos ------>")
    print(f"INDEX|       Datos")
    for key, producto in inventario.items():
        print(f"{key}: {producto}")
    mostrar_mensaje("")
    input("")


def actualizar_producto(key_producto):
    #Actualizar los detalles de un producto.
    if key_producto in inventario:
        producto = inventario[key_producto]
        print(f"Seleccionaste el producto: {producto}")
        nombre = input("Ingrese el nuevo nombre: ")
        precio = int(input("Ingrese el nuevo precio: "))
        stock = int(input("Ingrese el nuevo stock: "))
        categoria = input("Ingrese la nueva categoria: ")
        marca = input("Ingrese la nueva marca: ")

        if chequeo_datos_producto(precio, stock):
            inventario[key_producto] = {
                "nombre": nombre, "precio": precio, "stock": stock, "categoría": categoria, "marca": marca}
            mostrar_mensaje(f"Producto '{nombre}' actualizado exitosamente.")
    else:
        mostrar_mensaje("Producto no encontrado.")


def buscar_producto(index):
    #Buscar y mostrar un producto por su id.
    if index in inventario:
        producto = inventario[index]
        print(f'''
                Datos del producto:
                
                Nombre: {producto["nombre"]}
                Precio: {producto["precio"]}
                Stock: {producto["stock"]}
                Categoria: {producto["categoria"]}
                Marca: {producto["marca"]}
                ''')
        input()
    else:
        mostrar_mensaje("Producto no encontrado.")


def eliminar_producto(index):
    #Eliminar un producto por su id.
    if index in inventario:
        producto = inventario.pop(index)
        mostrar_mensaje(f"Producto '{producto['nombre']}' eliminado exitosamente.")
    else:
        mostrar_mensaje("Producto no encontrado.")


def reporte_bajo_stock(limite):
    #Generar un reporte de productos con stock bajo.
    limpiar_consola()
    print(f"Productos con stock menor o igual a: {limite}")
    for producto in inventario.values():
        if producto["stock"] <= limite:
            print(producto)
    mostrar_mensaje("")
    input()


# Menú principal
opcion = ""

while opcion != "7":
    limpiar_consola()
    print("Bienvenido/a al sistema Kiosco Montoto")
    opcion = input(f'''Ingrese la opción: 
                            1) Agregar producto 
                            2) Mostrar lista de productos 
                            3) Eliminar Producto 
                            4) Actualizar un Producto
                            5) Buscar un producto por id
                            6) Alerta de Stock Bajo
                            7) Salir
                            Ingrese su opción: ''')

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio: "))
        stock = int(input("Ingrese el stock: "))
        categoria = input("Ingrese la categoría: ")
        marca = input("Ingrese la marca: ")

        if chequeo_datos_producto(precio, stock):
            datos_producto = {"nombre": nombre, "precio": precio, "stock": stock, "categoria": categoria, "marca": marca}
            registrar_producto(datos_producto)
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        mostrar_productos()
        ingreso_usuario = int(input("Ingrese el id del producto que desea eliminar: "))
        eliminar_producto(ingreso_usuario)
    elif opcion == "4":
        mostrar_productos()
        ingreso_usuario = int(input("Ingrese el id del producto que desea actualizar: "))
        actualizar_producto(ingreso_usuario)
    elif opcion == "5":
        ingreso_usuario = int(input("Ingrese el id del producto que desea buscar: "))
        buscar_producto(ingreso_usuario)
    elif opcion == "6":
        ingreso_usuario = int(input("Ingrese el límite de stock a consultar: "))
        reporte_bajo_stock(ingreso_usuario)
    elif opcion == "7":
        mostrar_mensaje("Vuelva pronto.")
    else:
        mostrar_mensaje("Opción no válida.")
