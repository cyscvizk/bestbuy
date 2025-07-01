from typing import List, Tuple
from products import Product

class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

# store.py (continued)

if __name__ == "__main__":
    from products import Product

    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    # Get and print active products
    products = best_buy.get_all_products()
    for p in products:
        print(p.show())

    # Total quantity in store
    print("Total quantity in store:", best_buy.get_total_quantity())  # Should print 850

    # Place an order
    try:
        total_cost = best_buy.order([
            (products[0], 1),  # 1 MacBook Air M2
            (products[1], 2)   # 2 Bose Earbuds
        ])
        print(f"Order cost: {total_cost} dollars.")  # Should print the total cost
    except Exception as e:
        print("Error placing order:", e)
