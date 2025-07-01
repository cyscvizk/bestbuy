from products import Product
from store import Store

def start(store: Store):
    while True:
        print("\n=== Welcome to the Store ===")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose an option (1-4): ")

        if choice == "1":
            print("\n--- Products Available ---")
            for idx, product in enumerate(store.get_all_products(), start=1):
                print(f"{idx}. {product.show()}")

        elif choice == "2":
            print("\nTotal quantity in store:", store.get_total_quantity())

        elif choice == "3":
            active_products = store.get_all_products()
            print("\n--- Make an Order ---")
            for idx, product in enumerate(active_products, start=1):
                print(f"{idx}. {product.show()}")

            shopping_list = []

            while True:
                prod_choice = input("\nEnter product number to buy (or 'done' to finish): ").strip()
                if prod_choice.lower() == "done":
                    break
                if not prod_choice.isdigit() or not (1 <= int(prod_choice) <= len(active_products)):
                    print("Invalid choice, try again.")
                    continue

                quantity = input("Enter quantity to buy: ").strip()
                if not quantity.isdigit() or int(quantity) <= 0:
                    print("Invalid quantity, try again.")
                    continue

                product = active_products[int(prod_choice) - 1]
                shopping_list.append((product, int(quantity)))

            try:
                total_price = store.order(shopping_list)
                print(f"\n✅ Order successful! Total price: ${total_price:.2f}")
            except Exception as e:
                print(f"\n❌ Error placing order: {e}")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose from 1 to 4.")

# Setup initial inventory and launch UI
if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)

    start(best_buy)
