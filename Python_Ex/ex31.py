def show_cart(cart):
    if isinstance(cart, list) and len(cart) > 0:
        print("Shopping Cart Items:")
        for item in cart:
            print(item)
    else:
        print("Invalid cart")

cart = [100, 250, 75]

show_cart(cart)