#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # print(tickets.source , tickets.destination)
    for tickets in tickets:
        hash_table_insert(hashtable, tickets.source , tickets.destination)
        take_off = hash_table_retrieve(hash ,'NONE') #I dont know what to put for the key
        route[0] = take_off

    

    return route
