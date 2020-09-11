"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
        # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("that vertex does not exist!")
        # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
        # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # we must start at a node and traverse through
        # we will do it with a queue implementation 
        # we just want to print the values of each vertex in a breadth-first order
        # meaning ripples, each layer we want to print
        to_visit = Queue()

        # create a set to hold visited nodes
        # we can loop through a set and then do something with the values but nothing 
        # can be accessed to use
        visited = set()

        # Initialize: add the starting node to the queue
        to_visit.enqueue(starting_vertex)

        while to_visit.size() > 0:
            
            dqd = to_visit.dequeue()

            # if dqd not visited
            if dqd not in visited:
                # visit the node (print it)
                # print(dqd, 'the dequeue"d item')

                visited.add(dqd)
                print(dqd)
                for n in self.vertices[dqd]:
                    to_visit.enqueue(n)
        # print(visited)
        # new_list = list(visited)
        # print(new_list)
        # return new_list
        # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        to_visit = Stack()

        # create a set to hold visited nodes
        visited = set()

        # Initialize: add the starting_vertex to the stack
        to_visit.push(starting_vertex)

        # while queue not empty:
        while to_visit.size() > 0:
            # dequeue first entry
            v = to_visit.pop()

            # if not visited:
            if v not in visited:
                # visit the node (print it out)
                print(v)


                # add it to the visited set
                visited.add(v)

                # enqueue all it's neigbors
                for n in self.get_neighbors(v):
                    to_visit.push(n)


    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # if starting vertex 
        # return visited, dft_recursive(starting_vertex)
        # the next vertex end up being 
        if starting_vertex not in visited:
            print(starting_vertex)

            visited.add(starting_vertex)

            for n in self.get_neighbors(starting_vertex):
                self.dft_recursive(n, visited)


        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        to_visit = Queue()

        # create a set to hold visited nodes
        # we can loop through a set and then do something with the values but nothing 
        # can be accessed to use
        visited = set()

        # Initialize: add the starting node to the queue
        to_visit.enqueue([starting_vertex])

        while to_visit.size() > 0:
            
            path = to_visit.dequeue()
            visiting_node = path[-1]

            # if dqd not visited
            if visiting_node not in visited:
                # visit the node (print it)
                # print(dqd, 'the dequeue"d item')

                visited.add(visiting_node)
                if visiting_node == destination_vertex:
                    return path

                for n in self.vertices[visiting_node]:
                    to_visit.enqueue(path + [n])



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        to_visit = Stack()

        # create a set to hold visited nodes
        visited = set()

        # Initialize: add the starting_vertex to the stack
        to_visit.push([starting_vertex])

        while to_visit.size() > 0:

            # dequeue first item
            path = to_visit.pop()
            visiting_node = path[-1]

            if visiting_node not in visited:

                visited.add(visiting_node)
                if visiting_node == destination_vertex:
                    return path

                for n in self.vertices[visiting_node]:
                    to_visit.push(path + [n])



    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if path is None:

            path = [starting_vertex]

        visiting_node = path[-1]

        if visiting_node not in visited:
            visited.add(visiting_node)


            if visiting_node == destination_vertex:

                return path

            for n in self.get_neighbors(visiting_node):
                # we want to visit each new path given by the neighbors
                # otherwise we end up increasing our normal path and checking through those
                # when we want to check specific depths of neighobrs
                new_path = path + [n]
                # path = [1,2]
                # visiting_node = 2
                # path = [1,2,3]
                # path = [1,2,3,5]

                # path = [1,2,4]
                # path = [1,2,4]
                # visiting_node = 4
                # visited set = {1,2,4}
                # 4 != 6
                # now we loop through neighbors
                # new_path = [1,2,4] + [6] transforms path
                # path = [1,2,4,6]
                # visiting_node = 6

                # visited = {1,2,4,6}
                # is visiting node == dest.index 
                # return [1,2,4,6]
                next_search = self.dfs_recursive(starting_vertex,destination_vertex,visited,new_path)

                # if there are neighbors, let's execute our recursive function
                if next_search:
                    return next_search

        




if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    # print(graph.get_neighbors(4))

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    # graph.dft_recursive(1, 'the set')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6),'bfs path')

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6), 'dfs path')
    print(graph.dfs_recursive(1, 6),'dfs recursive')
