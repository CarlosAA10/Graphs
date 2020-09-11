
def earliest_ancestor(ancestors, starting_node):
    # if a node has no parents, it is the earliest ancestor
    # [(1,3),(2,3), (3,6)]

    # starting_node = 6
    # (3,6)
    # (5,6)
    # run on each of them if they do exist
    # this is for starting_node = 3
    # (1,3)
    # (2,3)
    # starting_node = 1
    # (10,1)
    # starting_node = 10
    # return ancestor = 10 # this should be what is returned
    # we have to find a way to keep track of ancestor list we have visited, and compare the longer one


    # starting_node = 2


    # after we discover each parent, we add that parent to the path
    # when we don't have a parent, return the path and then we can compare 
    # however, we would want to do this dynamically and 
    # this is for starting_node = 5
    # (4,5)
    # start_node = 4
    # we've reached no more parents, it's an ancestor



    # what this model misses is a way to gather paths, 
    # and then compare the paths to find an earliest ancestor
    # if we can find a way to generate paths 
    # we can effectively compare all arrays of paths [1,2,4] , [1,2,4,5]
    # we can loop through all of the paths
    # keep a variable as earliest ancestor
    # if the list we are on is longer than current
    # earliest ancestor path, we swap earliest ancestor path with current list 
    # we return earliest ancestor[-1]
    # [1,2,5] [1,2,6]


    # i think to have paths set for each number, 
    # we need to add to a dictionary, that we will create the paths for 
    # we will run a DFT that appends to 
    # before with bfs
    # once we reaches the level that had the destination vertex
    # we stopped
    # if we want to search the longest path
    # we would need to 

    # if all lists are the same length
    # we will check for last item in each list
    # so for current earliest ancestor, 
    # we will make it equal to the last element in the list of paths we are looping through
    # we will make this for the first one
    # as we loop through each path, if the last element of that path is less than 
    # our earliest ancestor variable, we swap values
    # otherwise keep traversing
    # once we have traversed, we return the earliest ancestor
    # and that's the answer 

    pass