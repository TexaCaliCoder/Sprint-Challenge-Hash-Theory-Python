#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for location in tickets:
        hash_table_insert(hashtable, location.source, location.destination)
        
    # the stupid capitalization of this work got me hung up for like 30 min.
    key = "NONE"
    for ticket in range(length):
        current = hash_table_retrieve(hashtable, key)
        route[ticket] = current
        key = current
    return route
