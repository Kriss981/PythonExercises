#!/usr/bin/env python3
""" Data Structures and Algorithms for CL 3, Assignment 5
    See <https://https://dsacl3-2022.github.io/a5/> for detailed
    instructions.

    Author: Pun Ching Nei
    Honor Code:  I pledge that this program represents my work.
    I received help from: no one in designing and debugging my program.
"""
from collections import defaultdict

import numpy as np


class DiGraph:

    def __init__(self, edge_list):
        """
        Initialize an adjacency matrix without edges

        Parameters
        ____
        edge_list: a list of lists of two elements that represent directed edges, where the rightmost element
        """
        flat_nodes = {item for lst in edge_list for item in lst}
        # print(flat_nodes)
        # print(sorted(list(flat_nodes)))
        self.nodes = sorted(list(flat_nodes))
        self.nodes2idx = dict()
        self.idx2nodes = dict()
        self.color = {}
        self.visited = {}
        self.isCycle = False

        # Dictionaries for easy access
        for idx, node in enumerate(self.nodes):
            self.nodes2idx[node] = idx
            self.idx2nodes[idx] = node
        # print(self.nodes2idx)
        # print(self.idx2nodes)

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
        if node not in self.nodes2idx:
            print(node, "is not in the matrix. Cannot add incoming or outgoing edges")
            return
        # get index of the node
        node_idx = self.nodes2idx[node]

        # Add neighbours going into node
        for n in in_neigh:
            if n not in self.nodes2idx:
                print(n, "is not in the matrix. Cannot add incoming or outgoing edges")
                continue

            # get index of neighbor
            neigh_idx = self.nodes2idx[n]
            # set matrix cell to True
            self.matrix[neigh_idx][node_idx] = True

        # Add neighbours going out of node
        for n in out_neigh:
            if n not in self.nodes2idx:
                print(n, "is not in the matrix. Cannot add incoming or outgoing edges")
                continue
            # get index of neighbor
            neigh_idx = self.nodes2idx[n]
            # set matrix cell to True
            self.matrix[node_idx][neigh_idx] = True

    def add_node(self, node, in_neigh, out_neigh):
        """
        Exercise 5.1

        Add a node to the matrix with the associated incoming and outgoing neighbors. This is a void method.

        Parameters
        ____
        node: data of the node to be added
        in_neigh: data of the associated incoming nodes
        out_neigh: data of the associated outgoing nodes
        """
        temp = []
        self.nodes.append(node)
        if node not in self.nodes2idx:
            self.nodes2idx[node] = max(self.nodes2idx.values()) + 1

        for _ in in_neigh:
            temp.append([_, node])

        for _ in out_neigh:
            if [node, _] not in temp:
                temp.append([node, _])

        new_matrix = np.full((len(self.nodes), len(self.nodes)), False)
        for x in range((len(self.nodes) - 1)):
            for y in range((len(self.nodes) - 1)):
                if self.matrix[x][y] != new_matrix[x][y]:
                    new_matrix[x][y] = True
        self.matrix = new_matrix

        for x in temp:
            in_node = self.nodes2idx[x[0]]
            out_node = self.nodes2idx[x[1]]
            self.matrix[in_node][out_node] = True
        # print(self.matrix)

    def detect_cycle_dfs(self, start, visited=None):
        """
        Exercise 5.2

        Detect a cycle by using a depth-first traversal of the graph from start node.  When it is possible to visit more
        than one node, visit them in alphabetical order. You may assume all nodes have string names.

        It should return a tuple where the first element is a boolean (was a cycle found in this traversal) and the
        second one is the visited dictionary.

        Parameters
        ____
        start: first node to visit
        visited: a dictionary keeping track of visited nodes (keys) and where they were visited from.
        """
        # visited_ans = self.visited_dict(start)
        # cycle = self.have_cycle(start)
        # ans = (, visited_ans)
        # return ans
        return self.dfs(start)

    # def get_neighbour(self, start):
    #     neighbour = []
    #     for x in range(len(self.nodes)):
    #         if self.matrix[self.nodes2idx[start]][x]:
    #             neighbour.append(self.idx2nodes[x])
    #     # print(neighbour)
    #     return neighbour

    # def visited_dict(self, start, visited=None):
    #     if visited is None:
    #         visited = {start: None}
    #     for node in self.get_neighbour(start):
    #         if node not in visited:
    #             visited[node] = start
    #             self.visited_dict(node, visited)
    #     return visited

    def dfs(self, start=None):
        for u in self.nodes:
            self.color[u] = "WHITE"
            self.visited[u] = None
        if start is not None:
            self.dfs_visit(start)
        for u in self.nodes:
            if self.color[u] == "WHITE":
                self.dfs_visit(u)
        return self.isCycle, self.visited

    def dfs_visit(self, u):
        self.color[u] = "GRAY"
        index = self.nodes2idx[u]
        adj = [self.idx2nodes[i] for i,v in enumerate(self.matrix[index]) if v]
        adj.sort()
        for v in adj:
            if self.color[v] == "GRAY":
                self.isCycle = True
            elif self.color[v] == "WHITE":
                self.visited[v] = u
                self.dfs_visit(v)
        self.color[u] = "BLACK"

    # def def_value(self):
    #     return []

    # def all_path_dict(self):
    #     connection = []
    #     connect_dict = defaultdict(self.def_value)
    #     # connect_dict = {}
    #     for x in range((len(self.nodes))):
    #         for y in range((len(self.nodes))):
    #             if self.matrix[x][y]:
    #                 connection.append([self.idx2nodes[x], self.idx2nodes[y]])
    #
    #     # print(connection)
    #     for x in range(len(connection)):
    #         key = connection[x][0]
    #         if connect_dict.get(key) is None:
    #             connect_dict[key] = connection[x][1]
    #         else:
    #             temp = []
    #             temp.extend(connect_dict[key])
    #             temp.extend(connection[x][1])
    #             connect_dict[key] = temp
    #     return connect_dict
        # print(connect_dict)

    # def have_cycle(self, x, visited, parent):
    #
    #     visited[x] = "In"
    #
    #     for y in self.all_path_dict()[x]:
    #         if visited[y] is not None and visited[y] == "N":
    #             cycle = self.have_cycle(y, visited, parent)
    #             if cycle:
    #                 return True
    #         elif visited[y] == "Y":
    #             print("cycle found", x, y)
    #             return True
    #     visited[x] = "Y"
    #     return False

    # def have_cycle(self, x, visited=[], cycle=[]):
    #     # print(self.all_path_dict()[x])
    #     final = False
    #     if x not in visited:
    #         visited.append(x)
    #     for _ in self.all_path_dict()[x]:
    #         # print(y)
    #         if _ not in visited:
    #             visited.append(_)
    #             cycle.append("False")
    #             self.have_cycle(_, visited,cycle)
    #         else:
    #             cycle.append("True")
    #
    #     # print(cycle)
    #     if "True" in cycle:
    #         visited = []
    #         cycle = []
    #         final = True
    #
    #     else:
    #         visited.pop()
    #         final = False
    #
    #     return final


    def contains_cycle(self):
        """
        Exercise 5.3

        Returns True if there is a cycle in the graph matrix. You may make use of the function in exercise 5.2.
        """
        return self.dfs()[0]
        # ans = []
        # for x in self.nodes:
        #     temp = self.have_cycle(x)
        #     ans.append(temp)
        #
        # if True not in ans:
        #     return False
        # else:
        #     return True
        # print(ans)



# You can use this space for trying and testing your code
if __name__ == '__main__':
    graph = DiGraph([['a', 'c'], ['a', 'd'], ['c', 'b'], ['d', 'b'], ['d', 'c']])
    # graph = DiGraph([['b', 'c'], ['c', 'b'], ['c', 'a'], ['c', 'd'], ['a', 'a'], ['a', 'b'], ['a', 'c'], ['a', 'd'],
    #                  ['d', 'b'], ['d', 'c']])
    # graph = DiGraph([['a', 'b'], ['b', 'a'], ['b', 'c'], ['c', 'a'], ['c', 'b'], ['c', 'c']])
    # graph = DiGraph([['a', 'a']])
    # graph.detect_cycle_dfs('a')
    # print(graph.dfs_visit('a'))
    graph.detect_cycle_dfs('a')
    # graph.get_neighbour('a')
    # graph.visited_dict('a')
    # print(graph.visited_dict('a'))
    # print(graph.contains_cycle())
