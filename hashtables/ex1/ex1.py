#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    index = 0
    for i in weights:
        index +=1
        hash_table_insert(ht, i, index)

    for i in range(len(weights)):
        # checking hastable for the weights
        sum_of_weight = limit - weights[i]
        #this finds the answer
        max_weight = hash_table_retrieve(ht, sum_of_weight)
        if max_weight is not None:
            return (max_weight, i)
    # return None



    """
    YOUR CODE HERE
    """

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
