#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

# if there aren't at least two weights return None
    if length < 2:
        return None
    
    for weight in range(length):
        hash_table_insert(ht, weights[weight], weight)
    
    for weight in range(length):
        first = weights[weight]
        second = limit - first
        node = hash_table_retrieve(ht, second)
        if node is not None:
            #checking larger value to place it first as a tuple
            if node > weight:
                returnResult = (node, weight)
            elif node < weight:
                returnResult = (weight, node)

    print("here is the return", returnResult)
    return returnResult
def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
