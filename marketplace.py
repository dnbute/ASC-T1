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
        self.consumer_cart_lock = threading.Lock() # lock used for creating a new cart for consumers
        self.add_cart_locks = [] # locks used for dealing with producer lists

        self.producer_queues = [] # a list queues for the producers
        self.consumer_carts = [] # a list of carts for the consumers

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        We have to use a lock as to be sure that if two
        threads call this method they dont get the same id.
        """

        with self.producer_reg_lock:
            self.next_producer_id += 1
            self.producer_queues.append([]) # new empty list for the producer
            self.add_cart_locks.append(threading.Lock()) # new lock for the producer

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
        return False

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id

        We have to use a lock as to be sure that if two
        threads call this method they dont get the same id.
        """
        with self.consumer_cart_lock:
            self.next_cart_id += 1
            self.consumer_carts.append([]) # new empty list for the cart

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

        for i, prod_queue in enumerate(self.producer_queues):
            if product not in prod_queue:
                pass
            else:
                # we use a lock when we found the product since
                # we dont want two threads trying to remove an
                # item at the same time
                with self.add_cart_locks[i]:
                    prod_queue.remove(product)
                    # Pair is used for knowing to which producer to return the item
                    # in case the consumer decides to remove it from the cart
                    prod_producer_pair = (product, i)
                    self.consumer_carts[cart_id].append(prod_producer_pair)
                    return True
        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        i = -1 # index of the producer to whom to return the product

        for prod, producer in self.consumer_carts[cart_id]:
            if prod == product:
                i = producer
                break
        prod_producer_pair = (product, i)
        self.consumer_carts[cart_id].remove(prod_producer_pair)
        # We use the same lock as the add_to_cart since both methods
        # operate on the producer lists and we dont want two
        # threads adding an item at the same time
        with self.add_cart_locks[i]:
            self.producer_queues[i].append(product)



    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        return self.consumer_carts[cart_id]
