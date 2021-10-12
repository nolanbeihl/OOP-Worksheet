from product import Product



class ShoppingCart:
    def __init__(self, add_cart):
        add_cart += []
        self.add_cart = add_cart

    def cart_content(self):
        print(self.add_cart)
    
    def add_product(self):
        input('What would you like to add?: ') + ShoppingCart.add_cart
        print('Ok, you now have ' + self.add_cart + ' in your cart')

    def remove_all_prodcuts(remove_all):
        customer_leave = input('Would you like to empty your cart?: ')
        if customer_leave == 'yes':
            print('I am sorry we were not able to help you today')
            ShoppingCart.add_cart == ''
        else:
            ShoppingCart.add_product()



