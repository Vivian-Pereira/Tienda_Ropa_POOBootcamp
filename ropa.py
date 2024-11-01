
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre 
        self._precio = precio

    def obtener_precio(self):
        return self._precio

    def __str__(self):
        return f"{self._nombre} - Gs {self._precio}"


class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def __str__(self):
        return f"Camisa: {super().__str__()}, Talla: {self._talla}"


class Pantalon(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def __str__(self):
        return f"Pantalón: {super().__str__()}, Talla: {self._talla}"


class Zapato(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def __str__(self):
        return f"Zapato: {super().__str__()}, Talla: {self._talla}"


class Vestido(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def __str__(self):
        return f"Vestido: {super().__str__()}, Talla: {self._talla}"


class Enterizo(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def __str__(self):
        return f"Enterizo: {super().__str__()}, Talla: {self._talla}"


class Categoria:
    def __init__(self, nombre):
        self._nombre = nombre
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def listar_productos(self):
        print(f"Productos en la categoría {self._nombre}:")
        for idx, producto in enumerate(self._productos, start=1):
            print(f"{idx}. {producto}")


class Carrito:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = sum(producto.obtener_precio() for producto in self._productos)
        return total

    def mostrar_resumen(self):
        print("Resumen de la compra:")
        for producto in self._productos:
            print(producto)
        print(f"Total a pagar: Gs {self.calcular_total()}")


class Tienda:
    def __init__(self):
        self._categorias = []

    def agregar_categoria(self, categoria):
        self._categorias.append(categoria)

    def mostrar_inventario(self):
        for categoria in self._categorias:
            categoria.listar_productos()

    def procesar_compra(self, carrito):
        carrito.mostrar_resumen()


if __name__ == "__main__":
    tienda = Tienda()

    categoria_camisas = Categoria("Camisas")
    categoria_pantalones = Categoria("Pantalones")
    categoria_zapatos = Categoria("Zapatos")
    categoria_vestidos = Categoria("Vestidos")
    categoria_enterizos = Categoria("Enterizos")
    
    categoria_camisas.agregar_producto(Camisa("Camisa Lila", 250000, "M"))
    categoria_camisas.agregar_producto(Camisa("Camisa Azul", 300000, "L"))
    categoria_pantalones.agregar_producto(Pantalon("Pantalón Negro", 150000, "32"))
    categoria_pantalones.agregar_producto(Pantalon("Pantalón Lila", 100000, "34"))
    categoria_zapatos.agregar_producto(Zapato("Zapato Deportivo", 400000, "42"))
    categoria_zapatos.agregar_producto(Zapato("Zapato Formal", 300000, "40"))
    categoria_vestidos.agregar_producto(Vestido("Vestido de Verano", 110000, "S"))
    categoria_vestidos.agregar_producto(Vestido("Vestido de Noche", 200000, "M"))
    categoria_enterizos.agregar_producto(Enterizo("Enterizo Corto", 50000, "L"))
    categoria_enterizos.agregar_producto(Enterizo("Enterizo Largo", 65000, "M"))
    tienda.agregar_categoria(categoria_camisas)
    tienda.agregar_categoria(categoria_pantalones)
    tienda.agregar_categoria(categoria_zapatos)
    tienda.agregar_categoria(categoria_vestidos)
    tienda.agregar_categoria(categoria_enterizos)
    tienda.mostrar_inventario()
    carrito = Carrito()
    carrito.agregar_producto(categoria_camisas._productos[0])
    carrito.agregar_producto(categoria_zapatos._productos[1])  
    tienda.procesar_compra(carrito)
