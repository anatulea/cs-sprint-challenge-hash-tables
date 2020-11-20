def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {} # create table to store key: absolute value of number and  value: the number
    result = [] # save the numbers that have coresponding negative numbers

    for num in a: # loop through each number in the list
        # get() method eturns the value for the given key, if present in the dictionary.
        #  If not, then it will return None 

        if hash_table.get(abs(num)) == None: # check if the absolute of the number is a key in the hash table
            hash_table[abs(num)] = num    # if it is not we add it 
        else: # if it is  we check if the absolute value and the value add up to be 0
            if (hash_table.get(abs(num)) + num) == 0:
                result.append(abs(num))# if they do means they are oposite so we add the absolute value of the number to the results list

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
