"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""
import threading

class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """
    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        self.queue_size_per_producer = queue_size_per_producer
        self.next_producer_id = -1 
        self.next_cart_id = -1

        self.producer_reg_lock = threading.Lock() # lock used for registering new producers
        self.consumer_cart_lock = threading.Lock() # lock used for creating a new cart for a consumer

        self.producer_queues = [] # a list queues for the producers
        self.consumer_carts = [] # a list of carts for the consumers

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """

        with self.producer_reg_lock:
            self.next_producer_id += 1
            self.producer_queues.append([])

        return self.next_producer_id

        

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        queue_id = int(producer_id)
        if len(self.producer_queues[queue_id]) < self.queue_size_per_producer:
            self.producer_queues[queue_id].append(product)
            return True
        else:
            return False
        

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        with self.consumer_cart_lock:
            self.next_cart_id += 1
            self.consumer_carts.append([])

        return self.next_cart_id

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        return True

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        pass

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        return []
