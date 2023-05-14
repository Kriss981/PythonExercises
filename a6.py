"""
Data Structures and Algorithms for CL 3, Assignment 6
See <https://https://dsacl3-2022.github.io/a6/> for detailed instructions.
Author:      Pun Ching Nei, Giulio Posfortunati
Honor Code:  I pledge that this program represents my work.
I received help from: no one in designing and debugging my program.
"""
from collections import defaultdict

import numpy as np


# Helper method to get incoming nodes
def get_parents(graph, node):
    return np.where(graph[:, node] == True)[0]


# Helper method to get outgoing nodes
def get_children(graph, parent):
    return np.where(graph[parent] == True)[0]


def find_cycle(graph):
    """
    Return the first cycle found by a depth-first traversal of the graph. When it is possible to visit more than one
    node, visit them in order.

    Returns a sorted list of nodes that participate in the first cycle found.

    Parameters
    ----------
    graph    An adjacency matrix where node 0 is a special root node (it never has any incoming edges).

    """
    newDict = defaultdict(list)
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j]:
                addEdge(newDict, i, j)

    numOfPoint = len(graph)
    visited = [0] * numOfPoint
    par = [-1] * numOfPoint
    cycles = []

    for i in range(numOfPoint):
        if visited[i] == 0:
            DFS(newDict, i, -1, visited, par, cycles)
    if len(cycles) > 0:
        # print(str(cycles[0]))
        return cycles[0]
    else:
        return []


def addEdge(graph, u, v):
    graph[u].append(v)


def DFS(graph, u, p, visited: list, par: list, cycles):
    if visited[u] == 2:
        return

    if visited[u] == 1:
        vList = []
        current = p
        vList.append(current)
        # when current is not starting point
        while current != u:
            current = par[current]
            vList.append(current)
        vList.reverse()
        cycles.append(vList)
        return

    #par mean path that how you go
    par[u] = p
    #visited means as a whole, means each point
    visited[u] = 1
    for vertex in list(graph[u]):
        if vertex == par[u]:
            visited[u] = 2
            # continue
        DFS(graph, vertex, u, visited, par, cycles)
    visited[u] = 2


def break_cycle(graph):
    """
    Void function. Calls the function find_cycle and breaks the cycle found by deleting the edge going from the lowest
    node in the cycle (n) to its lowest child also in the cycle (m) so that matrix[n][m] = False.

    Additionally, m should be attached to the root (node 0), so that matrix[0][m] = True.

    For example, if the cycle is [1, 3, 4, 5] and the children of 1 are [2, 3, 4], matrix[1][3] will be set to False and
    matrix[0][m] will be set to True.

    Parameters
    ____
     graph    An adjacency matrix where node 0 is a special root node (it never has any incoming edges).
    """
    cycle = find_cycle(graph)
    if not cycle:
        print('Graph is not cyclic')
        return
    else:
        # get the lowest node in the cycle
        lowest_node = min(cycle)

        # looking for the children of the node and then the lowest among them through iteration
        children = get_children(graph, lowest_node)
        # lowest_child = None
        for child in children:
            # if child in the cycle
            if child in cycle:
                # Break the edge, matrix[lowest_node][lowest_child] = False
                graph[lowest_node][child] = False

                # build a connection between the child and the root (node 0)
                graph[0][child] = True
                break
        return graph


def spanning_tree(graph):
    """
    Get rid of all the cycles in the graph and return a spanning tree in the form of an adjacency matrix. That is, no
    node can have more than one parent.

    When a node has two or more parents, delete all incoming edges except the one coming from the parent with the
    lowest value.

    For example, the following are all the incoming edges of node 2: [3, 2], [6, 2], [4, 2]. The tree should only
    contain the edge [3, 2]. As a result, matrix[3][2] = True but  matrix[6][2] = matrix[4][2] = False.

    Parameters
    ____
    graph    An adjacency matrix where node 0 is a special root node (it never has any incoming edges).
    """

    if not find_cycle(graph):
        # iterate each row
        for column in range(len(graph)):
            # iterate each column
            flag = False
            for row in range(len(graph)):
                # find the lowest node that is true
                if graph[row][column] and flag is False:
                    flag = True
                # make the others as false
                else:
                    graph[row][column] = False
    else:
        # make sure the graph has no cycle
        break_cycle(graph)
        spanning_tree(graph)
    return graph


class DiGraph:

    def __init__(self, edge_list):
        """
        Initialize an adjacency matrix with the edges specified by the edge list

        Parameters
        ____
        edge_list: a list of lists of two elements that represent directed edges, where the rightmost element
        """
        self.nodes = {item for lst in edge_list for item in lst}

        # Set matrix with corresponding nodes
        self.matrix = np.full((len(self.nodes), len(self.nodes)), False)

        for node1, node2 in edge_list:
            self.add_edges(node1, {}, {node2})

    def add_edges(self, node, in_neigh, out_neigh):
        """
        Adds incoming and outgoing edges to a node

        Parameters
        ____
        node: The node to which we add edges
        in_neigh: set of nodes that are incoming neighbors of the given node
        out_neigh: set of nodes that are outgoing neighbors of the given node
        """
        if node not in self.nodes:
            print(node, "is not in the matrix. Cannot add incoming or outgoing edges")
            return

        # Add neighbours going into node
        for n in in_neigh:
            if n not in self.nodes:
                print(n, "is not in the matrix. Cannot add incoming or outgoing edges")
                continue

            # set matrix cell to True
            self.matrix[n][node] = True

        # Add neighbours going out of node
        for n in out_neigh:
            if n not in self.nodes:
                print(n, "is not in the matrix. Cannot add incoming or outgoing edges")
                continue

            # set matrix cell to True
            self.matrix[node][n] = True


if __name__ == "__main__":
    pass