from shopping_cart import ShoppingCart



class Customer:
    def __init__(self, cust_name):
        self.cust_name =  cust_name
        self.cust_cart = ShoppingCart()
    
    def customer_name(self):
        cust_name = input('How are you doing today, may I ask your name?: ')
        Customer.cust_name = cust_name


    def new_product(self, product):
        self.cust_cart.add_product(product)

