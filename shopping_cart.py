from product import Product

class ShoppingCart:
    def __init__(self):
        self.products = []

    def cart_content(self):
        print(self.add_cart)
    
    def add_product(self, product):
        self.products.append(product)
        # product_cat = input('What type of product are you looking for?: ')
        # Product.product_type = product_cat
        # product_add = input('What is the name of what you are buying?: ')
        # Product.product_name = product_add
        # product_price = input('How much are you willing to pay?: ')
        # Product.product_price = product_price
        # cust_response = input('would you like to get anything else?: ')
        # if cust_response == 'yes':
        #     ShoppingCart.add_product(self)
        # else:
        #     print('Ok, we can check you out now')

    def cart_total(self):
        cart_total = 0
        for product in self.products:
            cart_total += product.product_price
        print(f'Your total today will be ${cart_total}')  

    def cart_contents(self):
        cart_contents = Product.product_name
        print('You have ' + cart_contents +' in your cart right now')  
    
    def remove_all_prodcuts(self):
        leaving = input('Would you like to empty your cart?: ')
        if leaving == 'yes':
            print('I am sorry we were not able to help you today')
            ShoppingCart.add_cart == ''
        else:
            ShoppingCart.add_product()



