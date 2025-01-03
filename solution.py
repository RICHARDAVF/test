#EJERCICIO 1:
# Se tienen los siguientes diccionarios:
# PROGRAMA PRINCIPAL
# Productos = {1:'Pantalones', 2:'Camisas', 2:'Corbatas',4:'Casacas'}
# Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
# Stock = {1:50, 2:45, 3:30, 4:15}

# Elaborar un programa que muestre los diccionarios, y programar las
# siguientes acciones:
#  [1] Agregar
#  [2] Eliminar
#  [3] Actualizar
#  [4] Salir
# ========================================
# Lista de Productos:
# ========================================
# 1 Pantalones 200.0 50
# 2 Camisas 120.0 45
# 3 Corbatas 50.0 30
# 4 Casacas 350.0 15
# ========================================
# [1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir
# Elija opción
try:
    from tabulate import tabulate #Libreria para imprimir en forma de tablas  para instalar "pip install tabulate "
except:
    pass
class Crud:
    def __init__(self):
        self.products:dict = {1:'Pantalones', 2:'Camisas', 3:'Corbatas',4:'Casacas'}
        self.prices:dict = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
        self.stock:dict =  {1:50, 2:45, 3:30, 4:15}

    def add(self):
        product_name:str = None
        product_price: float = None
        product_stock : int = None
        id = len(self.products)+1
        try:
            while True:
                print(" PROCESO DE AGREGAR ".center(100,'-'))

                try:
                    name:str = input("Ingrese nombre del producto: ")
                    if not name.isalpha():
                        raise ValueError("El nombre debe contener letras.")
                    if len(name)<2:
                        print("Nombre de la prenda demasiada corta.")
                        continue
                    product_name = name.capitalize()
                    break
                except Exception as e:
                    print(f"Error: {str(e)}")
            while True:
                try:
                    price:str = input("Ingrese el precio del producto: ")
                    if price.isalpha():
                        raise ValueError("Ingrese un precio válido.")

                    if float(price)<=0:
                        raise ValueError("El precio no puede ser negativo o cero")
                    product_price = round(float(price),3)
                    break
                except Exception as e:
                    print(f"Error: {str(e)}")
            while True:
                try:
                    stock:str = input("Ingrese stock del producto: ")
                    if stock.isalpha():
                        raise ValueError("Ingrese un stock válido.")
                    if int(stock)<=0:
                        raise ValueError("El stock no puede ser negatico o cero")
                    product_stock = int(stock)
                    break
                except Exception as e:
                    print(f"Error: {str(e)}")
            self.products[id] = product_name
            self.prices[id] = product_price
            self.stock[id] = product_stock
            print("Producto agragado exitosamente.\n")
        except Exception as e:
            raise ValueError(f"Ocurrio un error al intentar agregar un producto: {str(e)} ")
        self.read()
    def delete(self):
        try:
            while True:
                print(" PROCESO DE ELIMINACION ".center(100,'-'))
                self.read()
                try:
                    id:str = input("Ingrese el ID del producto: ")
                    if id.isalpha():
                        raise ValueError("El ID es un numero")
                    if int(id)<=0:
                        raise ValueError("El ID es un numeo posiivo")
                    if int(id) not in self.prices:
                        raise ValueError(f"Producto con ID:{id} no encontrado.\n")
                    confirm = input("¿Esta seguro(a) de eliminar este producto? (1:Sí,2:No)\nOpcion: ")
                    if confirm not in ["1","2"]:
                        print("Se cierra el proceso por seguridad...")
                        break
                    if confirm=="2":
                        print("Proceso cancelado...")
                        break
                    self.products.pop(int(id))
                    self.prices.pop(int(id))
                    self.stock.pop(int(id))
                    print(f"Producto con ID:{id} eliminado exitosamente.\n")
                    print("  NUEVO STOCK DE PRODUCTOS  ".center(100,'-'))
                    break
                except Exception as e:
                    print(str(f"Error: {str(e)}"))
        except Exception as e:
            raise ValueError(f"Ocurrio un erro al intentar eliminar un producto.")
        self.read()
    def update(self):
        product_id:int = None
        product_name : str = None
        product_price : str = None
        product_stock : str = None
        try:
            while True:
                print(" PROCESO DE EDICION ".center(100,'-'))

                self.read()
                try:
                    id = input("Ingrese el ID del producto a actualizar: ")
                    if id.isalpha():
                        raise ValueError("Error, el ID debe ser un numero")
                    if int(id)<=0:
                        raise ValueError("El ID no puede ser un numero negativo o cero")
                    if int(id) not in self.products:
                        raise ValueError(f"No existe un producto con ID:{id}.\n")
                    print(" PRODUCTO ".center(100,'-'))
                    product_id = int(id)
                    product_name = self.products[product_id]
                    product_price = self.prices[product_id]
                    product_stock = self.stock[product_id]
                    print(f"Nombre: {product_name}, Precio: {product_price}, Stock: {product_stock}")
                    break
                except Exception as e:
                    print(str(e))
            while True:
                try:
                    print(f"Nombre anterior: {product_name}")
                    name:str = input("Ingrese el nuevo nombre del producto (Enter para mantener.): ")
                    if name=="":
                        break
                    if not name.isalpha():
                        raise ValueError("El nombre debe contener letras.")
                    if len(name)<2:
                        print("Nombre de la prenda demasiada corta.")
                        continue
                    product_name = name.capitalize()
                    break
                except Exception as e:
                    print(f"Error: {str(e)}")
            while True:
                try:
                    print(f"Precio anterior: {product_price}")
                    price:str = input("Ingrese el nuevo precio del producto (Enter para mantener. ): ")
                    if price=="":
                        break
                    if price.isalpha():
                        raise ValueError("Ingrese un precio válido.")

                    if float(price)<=0:
                        raise ValueError("El precio no puede ser negativo o cero")
                    product_price = round(float(price),3)
                    break
                except Exception as e:
                    print(f"Error: {str(e)}")
            while True:
                try:
                    print(f"Stock anterior:{product_stock}")
                    stock:str = input("Ingrese nuevo stock del producto (Enter para mantener. ): ")
                    if stock=="":
                        break
                    if stock.isalpha():
                        raise ValueError("Ingrese un stock válido.")
                    if int(stock)<=0:
                        raise ValueError("El stock no puede ser negatico o cero")
                    product_stock = int(stock)
                    break
                except Exception as e:
                    print(f"Error: {str(e)}")
            self.products[product_id] = product_name
            self.prices[product_id] = product_price
            self.stock[product_id] = product_stock
            print(f"Producto con ID:{product_id} editado exitosamente.\n")
        except Exception as e:
            raise ValueError(f"Error: {str(e)}")
        self.read()
    def read(self):
        print("LISTADO DE PRODUCTOS".center(100,'-'))
        try:
            id:list[int] = ["ID"]+ list(self.prices.keys())
            prices:list[float] = ["PRECIOS S/"]+ list(self.prices.values())
            products:list[str] = ["PRODUCTOS"]+list(self.products.values())
            stock:list[int] = ["STOCK"]+list(self.stock.values())
            product = [[a,b,c,d] for a,b,c,d in zip(id,products,stock,prices)]
            print(tabulate(product,tablefmt="simple"))
        except :
            id = ["ID"] + list(self.prices.keys()) 
            prices = ["PRECIOS S/"] + list(self.prices.values()) 
            products = ["PRODUCTOS"] + list(self.products.values()) 
            stock = ["STOCK"] + list(self.stock.values()) 
            product = [[a, b, c, d] for a, b, c, d in zip(id, products, stock, prices)]
            print("="*100) 
            for row in product: 
                print(f"{row[0]: <5} {row[1]: <20} {row[2]:<5} {row[3]:<10} ")
            print("="*100) 
            
if __name__ == '__main__':
    instance = Crud()
    instance.read()
    while True:
        print("[1]:Agregar, [2]:Eliminar, [3]:Actualizar, [4]:Salir")
        try:
            option = int(input("Elija opción: "))
            if option==4:
                print("Procesos terminados...")
                break
            elif option == 1:
                instance.add()
            elif option == 2:
                instance.delete()
            elif option == 3:
                instance.update()
            else:
                raise ValueError("Opcion no reconocida, ingrese en un rango del 1 al 4")
        except Exception  as e:
            print(f"Error: {str(e)}")
