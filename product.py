class Product:
    def __init__(self, product_type, product_name, product_price):
        product_type = []
        product_name = []
        product_price = []
        self.product_name = product_name
        self.product_type = product_type
        self.product_price = product_price
    
    def add_product(product_add):
        product_add = input('What is the name of what you are buying?: ')
        Product.product_name = product_add

    
