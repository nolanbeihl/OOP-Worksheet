class Product:
    def __init__(self, product_cat, product_name, product_price):
        self.product_name = product_name
        self.product_type = product_cat
        self.product_price = product_price
        # product_cat = []
        # product_name = []
        # product_price = [int(i) for i in product_price]

    # def add_product(product_add):
    #     product_cat = input('What type of product are you looking for?: ')
    #     Product.product_cat = product_cat
    #     product_add = input('What is the name of what you are buying?: ')
    #     Product.product_name = product_add
    #     product_price = input(int('How much are you willing to pay?: '))
    #     Product.product_price = product_price
    #     input('would you like to get anything else?: ')
    #     if input == 'yes':
    #         Product.add_product(product_add)
    #     else:
    #         print('Ok, we can check you out now')

    
