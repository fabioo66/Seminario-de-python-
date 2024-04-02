def add_product(inventory, name, amount):
    for elem in inventory:
        if elem == name:
            print("El producto ya se encuentra en el inventario")
            return inventory    
        
    inventory[name] = amount
    print(f"Producto {name} agregado")
    return inventory

def show_products(inventory):
    print("----------------------")
    if inventory:
        print("Lista de productos")
        for elem in inventory:
            print(f"Nombre de producto: {elem} -> cantidad: {inventory[elem]}")

def remove_product(inventory, name):
    for elem in inventory:
        if elem == name:
            del inventory[name]
            
            print("Se elimino el producto correctamente")
            return inventory
    print("No se encontro ninguna coincidencia")
    return inventory

