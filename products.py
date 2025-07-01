class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name.strip():
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        if not self.active:
            raise Exception("Cannot buy an inactive product.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return quantity * self.price

if __name__ == "__main__":
    # Create a new product
    product = Product("MacBook Air M2", 1450.0, 100)
    print(product.show())  # Output: MacBook Air M2, Price: 1450.0, Quantity: 100

    # Buy 5 units
    total_price = product.buy(5)
    print(f"Total price for 5 units: {total_price}")  # Output: 7250.0
    print(product.show())  # Quantity should now be 95

    # Set quantity to 0
    product.set_quantity(0)
    print(f"Product active? {product.is_active()}")  # Output: False

    # Try to buy inactive product
    try:
        product.buy(1)
    except Exception as e:
        print(f"Error: {e}")
