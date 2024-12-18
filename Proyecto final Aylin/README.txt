=======================================================
                   Sistema Kiosco Montoto
=======================================================

Descripción:
Este es un sistema para la gestión de inventarios de un kiosco. Permite al usuario realizar operaciones sobre un inventario de productos, como agregar, actualizar, eliminar y buscar productos, y consultar reportes sobre productos con bajo stock.

Instrucciones:

1. Al ejecutar el programa, se presentará un menú principal:
   1) Agregar producto
   2) Mostrar lista de productos
   3) Eliminar Producto
   4) Actualizar un Producto
   5) Buscar un producto por id
   6) Alerta de Stock Bajo
   7) Salir

2. Cada opción realiza una acción específica en el inventario:
   - Opción 1: Permite agregar un nuevo producto al inventario. El usuario debe ingresar el nombre, precio, stock, categoría y marca del producto.
   - Opción 2: Muestra todos los productos registrados en el inventario, con sus detalles.
   - Opción 3: Elimina un producto existente del inventario, solicitando al usuario el ID del producto a eliminar.
   - Opción 4: Permite actualizar los detalles de un producto. El usuario debe ingresar el ID del producto a actualizar y luego los nuevos detalles.
   - Opción 5: Permite buscar un producto por su ID y muestra sus detalles.
   - Opción 6: Genera un reporte de productos con stock menor o igual al límite ingresado por el usuario.
   - Opción 7: Sale del programa.

Funciones:

1. limpiar_consola()
   - Limpia la consola para una mejor visualización entre acciones.

2. mostrar_mensaje(mensaje)
   - Muestra un mensaje al usuario y espera a que presione Enter para continuar.

3. chequeo_datos_producto(precio, stock)
   - Verifica que el precio y el stock de un producto sean mayores a cero. Si no lo son, muestra un mensaje de error.

4. registrar_producto(datos_producto)
   - Registra un nuevo producto en el inventario.

5. mostrar_productos()
   - Muestra todos los productos registrados en el inventario.

6. actualizar_producto(key_producto)
   - Permite actualizar los detalles de un producto (nombre, precio, stock, categoría, marca).

7. buscar_producto(index)
   - Busca un producto por su ID y muestra sus detalles.

8. eliminar_producto(index)
   - Elimina un producto del inventario dado su ID.

9. reporte_bajo_stock(limite)
   - Muestra los productos cuyo stock es menor o igual al límite ingresado.

=======================================================
- Los productos en el inventario se identifican por un ID único, que se asigna automáticamente al registrar un producto.
- El programa está diseñado para ser ejecutado desde la consola. La entrada del usuario se maneja mediante opciones numéricas.
- Las operaciones de agregar, eliminar y actualizar productos requieren que el usuario ingrese el ID de un producto.

=======================================================
Autora: Aylin Ramirez