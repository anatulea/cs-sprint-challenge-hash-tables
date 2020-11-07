# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {} # create a table to store key: file name and value: entire path
    result = [] # list to store all the full paths that match that filename

    for path in files: # loop through each path from the files array
        file_name = path.split('/')[-1] # extract the file name from the whole path
        # print(file_name)  # foo
                            # bar
                            # baz

        if file_name not in hash_table: # check if file mame exists as key in the table
            # if not we create is as ke and give the value of the whole path 
            # place the path in an array in case the file is saved in different places
            hash_table[file_name]= [path] 
        else:
            hash_table[file_name].append(path)  # append tne other path to the path array

    # print(hash_table) # {'foo': ['/bin/ggg/foo', '/bin/foo'], 'bar': ['/bin/bar'], 'baz': ['/usr/bin/baz']}

    for query in queries: # loop through the querries list
        if query in hash_table: # check it the query is present as a key in the hash table
            results = hash_table[query]
            # print(results) # ['/bin/ggg/foo', '/bin/foo']
                             # ['/usr/bin/baz']
                             # []
            for path in results: # the results is an array so we need to loop through it and append each path to th eresult array
                result.append(path)
    return result


if __name__ == "__main__":
    files = [
        '/bin/ggg/foo',
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
