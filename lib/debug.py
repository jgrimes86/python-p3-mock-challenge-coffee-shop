#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee


cust1 = Customer("Stephen")
cust2 = Customer("Amy")

cof1 = Coffee("Latte")
cof2 = Coffee("Espresso")

ord1 = Order(cust1, cof1, 5.25)
ord2 = Order(cust2, cof1, 5.20)
ord3 = Order(cust1, cof2, 4.75)
ord4 = Order(cust1, cof1, 5.25)

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    ipdb.set_trace()
