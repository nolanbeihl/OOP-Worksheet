# from alarm_clock import AlarmClock

# current_time = AlarmClock(input("What time would you like to set the clock to?: "),input("What time would you like to set the alarm for?: "))

# print(current_time.time)

# current_time.change_time()
# current_time.set_alarm()

from product import Product
from customer import Customer
                       
customer_object = Customer("Nolan")

tent = Product("Camping", "Tent", 300)
fishing_pole = Product("Camping", "Fishing Pole", 80)
sleeping_bag = Product("Camping", "Sleeping Bag", 30)

customer_object.new_product(tent)
customer_object.new_product(fishing_pole)
customer_object.new_product(sleeping_bag)
print(customer_object.cust_cart.products)
customer_object.cust_cart.cart_total()






# customer_object.customer_name()
# print('Good Afternoon ' + customer_object.cust_name)

# customer_object.add_product('shopping')
# customer_object.cart_total('products in cart')
# customer_object.cart_total('total')

