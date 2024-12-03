# https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
# https://www.youtube.com/watch?v=Qzf1a--rhp8

from typing import List


def dfs(vertex, adj, visitedArr, dfs_arr):

    visitedArr[vertex] = 1
    dfs_arr.append(vertex)
    for neighbour in adj[vertex]:
        if not visitedArr[neighbour]:
            dfs(neighbour, adj, visitedArr, dfs_arr)


def dfsOfGraph(adj):

    numberOfVertices = len(adj)

    visitedArr = [0]*numberOfVertices

    dfs_arr = []
    start = 0

    dfs(start, adj, visitedArr, dfs_arr)

    return dfs_arr


adj = [
    [1, 2],    # Node 0 is connected to 1, 2
    [0, 3, 4],  # Node 1 is connected to 0, 3, 4
    [0],       # Node 2 is connected to 0
    [1],       # Node 3 is connected to 1
    [1]        # Node 4 is connected to 1
]

# Graph representation:
# 0 - 1 - 3
# |   |
# 2   4

print(dfsOfGraph(adj))


""" 
Explanation and Step-by-Step Dry Run
Problem Statement:

Perform a DFS traversal on a graph represented by an adjacency list, starting from node 0. The goal is to return the list of nodes visited in DFS order.
Key Functions and Flow

    dfs(node, adj, vis, ls):
        Recursive function to explore the graph.
        Marks the current node as visited.
        Adds the node to the result list.
        Recursively visits all its unvisited neighbors.

    dfsOfGraph(V, adj):
        Initializes the visited array (vis) with all 0s (indicating no nodes are visited).
        Calls the dfs function starting from node 0.
        Returns the list ls containing the DFS traversal.

Dry Run Example
Graph Representation (Adjacency List):

Consider the following graph with V = 5 nodes and the adjacency list:

0 -> [1, 2]
1 -> [0, 3]
2 -> [0]
3 -> [1, 4]
4 -> [3]

Input:

V = 5
adj = [[1, 2], [0, 3], [0], [1, 4], [3]]

Initial Setup:

    vis = [0, 0, 0, 0, 0] (No nodes visited yet)
    ls = [] (Traversal list is empty)
    Starting node: 0

Execution Steps:

    Call dfs(0, adj, vis, ls):
        Mark 0 as visited: vis = [1, 0, 0, 0, 0].
        Add 0 to ls: ls = [0].
        Traverse neighbors of 0: [1, 2].

    Visit Neighbor 1:
        Call dfs(1, adj, vis, ls):
            Mark 1 as visited: vis = [1, 1, 0, 0, 0].
            Add 1 to ls: ls = [0, 1].
            Traverse neighbors of 1: [0, 3].
            Skip 0 (already visited).
        Visit 3.

    Visit Neighbor 3:
        Call dfs(3, adj, vis, ls):
            Mark 3 as visited: vis = [1, 1, 0, 1, 0].
            Add 3 to ls: ls = [0, 1, 3].
            Traverse neighbors of 3: [1, 4].
            Skip 1 (already visited).
        Visit 4.

    Visit Neighbor 4:
        Call dfs(4, adj, vis, ls):
            Mark 4 as visited: vis = [1, 1, 0, 1, 1].
            Add 4 to ls: ls = [0, 1, 3, 4].
            Traverse neighbors of 4: [3].
            Skip 3 (already visited).
        Return to 3, then 1, then 0.

    Visit Neighbor 2:
        Call dfs(2, adj, vis, ls):
            Mark 2 as visited: vis = [1, 1, 1, 1, 1].
            Add 2 to ls: ls = [0, 1, 3, 4, 2].
            Traverse neighbors of 2: [0].
            Skip 0 (already visited).
        Return to 0.

Final Traversal List:

ls = [0, 1, 3, 4, 2]
Complexity

    Time Complexity:
        Each node is visited exactly once.
        Each edge is traversed exactly once.
        O(V + E), where V is the number of vertices and E is the number of edges.

    Space Complexity:
        Visited array (vis): O(V).
        Recursion stack (in worst-case): O(V) for a connected graph.
        Total: O(V).


"""
