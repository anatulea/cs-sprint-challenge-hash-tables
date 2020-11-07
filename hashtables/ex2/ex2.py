#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {} # Create a hash table to store key: source, value: destination
    route = [None]* length # initiate an list to store the itinerary

    for fly in tickets: # loop over the tickets list
        hash_table[fly.source] = fly.destination # create a key-value  pair for each item in the list
    next_fly = hash_table['NONE'] # Save the first flight as the next flight variable

    for curr_fly in range(0,length): # Add the flights in proper order in the route list
        route[curr_fly]= next_fly # set the first element in the rout list to be the first flight
        next_fly = hash_table[next_fly] # set the next flight to be equal to the destination at the hash_table with the next_flight key

    return route
