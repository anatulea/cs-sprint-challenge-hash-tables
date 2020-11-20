def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {} # create a hash table 
    for idx in range(0, length):
        hash_table[weights[idx]] = idx # store the weight and index of  each weight from the list
    
    for index, weight in enumerate(weights): # for each item and index of item in the weights list
        second_item_weight = limit - weight # calculate the necessary weight that would sum to be the needed limit

        if second_item_weight in hash_table: # check the table for the needed contra weight 
            item_idx = hash_table[second_item_weight] # knowing the weight retrive the index of that weight
            
            if index > item_idx: # check which index of the two weights is bigger
                return(index, item_idx) # return both indeces with the bigger one first and smollest second 
            else:
                return(item_idx, index)
    return None # retun none if no two weights add up to the limit weight
