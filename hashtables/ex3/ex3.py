def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {} # create a hash table to store key: number in arr, value: the number of times it occures in the all the arrays
    result = [] # create a list to save the numbers that appear in all the arrays

    for array in arrays: # loop through the list of arrays
        for num in array: # loop through each arr 
            if num not in hash_table: # check if the numer exists as a key in the hash table
                hash_table[num] = 1 # if it does not, add a key with the number and set the value to one
            else:
                hash_table[num] += 1 # if the hash table has a key that is equal to the num increase the value by one
                if hash_table[num] == len(arrays): # check if the hash table at the key of num has the value equal to the length of the initial array of arrays
                    result.append(num) #if it does means that the number is present in all the arrays and we can add it to the result array

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
