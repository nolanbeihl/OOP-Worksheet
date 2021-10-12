# from alarm_clock import AlarmClock

# current_time = AlarmClock(input("What time would you like to set the clock to?: "),input("What time would you like to set the alarm for?: "))

# print(current_time.time)

# current_time.change_time()
# current_time.set_alarm()

from product import Product
from customer import Customer
from shopping_cart import ShoppingCart

cart = ShoppingCart
cust = Customer
product = Product

cust.customer_name('Hello')
print('Good Afternoon ' + Customer.cust_name)

cart.add_product('shopping')
cart.cart_total('products in cart')
cart.cart_total('total')

