class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y Setters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, id, nombre, cantidad, precio):
        # Verificar si el ID ya existe
        if any(producto.get_id() == id for producto in self.productos):
            print("Error: El ID ya existe. No se puede añadir el producto.")
            return
        nuevo_producto = Producto(id, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print("Producto añadido exitosamente.")

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                print("Producto eliminado exitosamente.")
                return
        print("Error: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: No se encontró un producto con ese ID.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        if resultados:
            print("\n--- Productos encontrados ---")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            print("\n--- Inventario ---")
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")


def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id = input("Ingresa el ID del producto: ").strip()
            nombre = input("Ingresa el nombre del producto: ").strip()
            try:
                cantidad = int(input("Ingresa la cantidad: ").strip())
                precio = float(input("Ingresa el precio: ").strip())
            except ValueError:
                print("Error: La cantidad y el precio deben ser valores numéricos.")
                continue
            inventario.añadir_producto(id, nombre, cantidad, precio)

        elif opcion == '2':
            id = input("Ingresa el ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("Ingresa el ID del producto a actualizar: ").strip()
            nueva_cantidad = input("Ingresa la nueva cantidad (dejar en blanco si no deseas actualizarla): ").strip()
            nuevo_precio = input("Ingresa el nuevo precio (dejar en blanco si no deseas actualizarlo): ").strip()

            # Convertir entradas si no están vacías
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None

            inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio)

        elif opcion == '4':
            nombre = input("Ingresa el nombre del producto a buscar: ").strip()
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
