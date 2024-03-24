import shop

def main():
    inventory = {}
    inventory = shop.add_product(inventory, "Cindor", 3)
    inventory = shop.add_product(inventory, "Oreos", 2)

    inventory = shop.remove_product(inventory, "Cindor")
    inventory = shop.add_product(inventory, "Cindor", 5)
    inventory = shop.add_product(inventory, "Frutigran", 5)
    shop.show_products(inventory)

main()
