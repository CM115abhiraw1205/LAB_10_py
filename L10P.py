# create an empty dictionary to store products and brands
shoppingCart = {}

# function to add a new product to the shopping cart


def add_product():
    itemNumberIWant = int(
        input("Enter the number of items to be added in the stationary shop: "))
    # check if input is valid
    if itemNumberIWant >= 5:
        print("Invalid input")
        return

    if len(shoppingCart) >= 5:
        print("Cart is full")

    # add items to cart
    for i in range(itemNumberIWant):
        # get input from user for product and brand
        product = input("Enter an item: ")
        brand = input("Enter the brand name: ")
        # add product and brand to the shopping cart
        shoppingCart[product] = brand

    # check if cart has less than 5 products
    if len(shoppingCart) == itemNumberIWant or len(shoppingCart) == 5:
        print("You added following items to the cart:")
        for items in shoppingCart.items():
            print(f"{product}:{shoppingCart[product]}")

# function to search for a product in the shopping cart


def search_product():
    # get input from user for product to search
    product = input("Enter the item to be searched: ")
    # check if product exists in the shopping cart
    if product in shoppingCart:
        print(f"{product} found in cart.")
        print(f"{product}:{shoppingCart[product]}")
    else:
        print("No product exists with this name.")

# function to delete a product from the shopping cart


def delete_product():
    # get input from user for product to delete
    product = input("Enter product name to delete: ")
    # check if product exists in the shopping cart
    if product in shoppingCart:
        # remove product from the shopping cart
        del shoppingCart[product]
        print(f"{product} deleted from cart.")
    else:
        print("No product exists with this name.")
    # check if cart is empty
    if not shoppingCart:
        print("Cart is empty, no item is found.")

# main function to display the menu and handle user input


def main():
    print("WELCOME TO THE AMANDO SHOPPING SITE")
    print("1. Add product to the cart.")
    print("2. Search the product.")
    print("3. Delete the product from the cart.")
    print("4. Quit.")
    print()
    while True:
        choice = input("Enter your choice : ")
        # handle user input based on menu choice
        if choice == "1":
            add_product()
        elif choice == "2":
            search_product()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            print("Thank you for shopping with us!")
            break
        else:
            print("Wrong Option Entered.")


# call the main function to run the program
if __name__ == "__main__":
    main()
