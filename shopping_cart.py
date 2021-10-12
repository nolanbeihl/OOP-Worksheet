from product import Product



class ShoppingCart:
    def __init__(self, shopping_cart_products):
        shopping_cart_products += Product.product_name
        self.add_cart = shopping_cart_products

    def cart_content(self):
        print(self.add_cart)
    
    def add_product(self):
        user_input=input('What would you like to add?: ')
        ShoppingCart.shopping_cart_products = user_input
        print('Ok, you now have ' + ShoppingCart.shopping_cart_products + ' in your cart')

    def remove_all_prodcuts(self):
        leaving = input('Would you like to empty your cart?: ')
        if leaving == 'yes':
            print('I am sorry we were not able to help you today')
            ShoppingCart.add_cart == ''
        else:
            ShoppingCart.add_product()



