class Coffee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Coffee: {self.name}>"
    
    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if not hasattr(self, '_name'):
            if (type(new_name) == str) and (3 <= len(new_name)):
                self._name = new_name
            else:
                raise Exception("Coffee name must be a string with at least 3 characters.")
        else:
            raise Exception("Cannot rename coffee")

    name = property(get_name, set_name)

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        unique_customer_list = []
        for order in self.orders():
            if order.customer not in unique_customer_list:
                unique_customer_list.append(order.customer)
        return unique_customer_list

    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        total_price = 0
        for order in self.orders():
            total_price += order.price
        if total_price == 0:
            return 0
        else:
            return round(total_price / self.num_orders(), 2)
        

class Customer:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"<Customer: {self.name}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if (type(new_name) == str) and (1 <= len(new_name) <= 15):
            self._name = new_name
        else:
            raise Exception("Name must be a string between 1 and 15 characters long.")

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        unique_coffee_list = []
        for order in self.orders():
            if order.coffee not in unique_coffee_list:
                unique_coffee_list.append(order.coffee)
        return unique_coffee_list
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    def __repr__(self):
        return f"<Order of {self.coffee.name} for {self.customer.name}>"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if not hasattr(self, '_price'):
            if type(new_price) == float and (1.0 <= new_price <= 10.0):
                self._price = new_price
            else:
                raise Exception("Price must be a float between 1.0 and 10.0, inclusive.")
        else:
            raise Exception("Cannot change price.")
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else:
            raise Exception("Order must include a Customer instance.")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            raise Exception("Order must include a Coffee instance.")