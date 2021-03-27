"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread, currentThread
import time


class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time
        self.name = currentThread().getName()
        


    def run(self):
        for cart in self.carts:
            cart_id = self.marketplace.new_cart()

            for operation in cart:
                op_count = 0
                op_type = operation["type"]
                op_prod = operation["product"]
                op_qnt = operation["quantity"]
                
                while op_count < op_qnt:
                    if op_type == "add":
                        if self.marketplace.add_to_cart(cart_id, op_prod):
                            op_count += 1
                        else:
                            time.sleep(self.retry_wait_time)
                    else:
                        self.marketplace.remove_from_cart(cart_id, op_prod)
                        op_count += 1
            prod_list = self.marketplace.place_order(cart_id)
            for prod in prod_list:
                print(self.name + "bought" + prod)