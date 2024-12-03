from typing import List
from collections import deque


def bfsOfGraph(adj: List[List[int]]) -> List[int]:
    noOfVertices = len(adj)

    visitedArr = [0]*noOfVertices

    queue = deque()
    queue.append(0)  # Reason for directly appending 0 is given below
    visitedArr[0] = 1

    bfs = []
    while queue:

        vertex = queue.popleft()

        bfs.append(vertex)

        for neighbour in adj[vertex]:
            if not visitedArr[neighbour]:
                visitedArr[neighbour] = 1
                queue.append(neighbour)

    return bfs


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


print(bfsOfGraph(adj))


""" 
Step-by-Step Explanation

    Input Variables:
        V: Number of vertices in the graph.
        adj: Adjacency list representation of the graph. Each adj[i] contains the list of vertices connected to vertex i.

    Visited List:
        vis = [0] * V: A list of size V initialized to 0 (False). This tracks whether a node has been visited.
        vis[0] = 1: The starting node (0) is marked as visited.

    Queue Initialization:
        q = deque(): A queue is used to store nodes to be visited (FIFO).
        q.append(0): Add the starting node (0) to the queue.

    BFS Process:
        The algorithm iterates as long as the queue is not empty (while q:).
        node = q.popleft(): The first element in the queue is removed and processed.
        bfs.append(node): The current node is added to the BFS result list.

    Traversing Neighbors:
        For every node, its neighbors (from the adjacency list) are iterated.
        If a neighbor has not been visited (if not vis[neighbor]:):
            Mark the neighbor as visited (vis[neighbor] = 1).
            Add the neighbor to the queue (q.append(neighbor)).

    Returning Result:
        After the queue is empty, the BFS traversal list (bfs) is returned.

Dry Run
Input:

V = 5
adj = [
    [1, 2],    # Node 0 is connected to 1, 2
    [0, 3, 4], # Node 1 is connected to 0, 3, 4
    [0],       # Node 2 is connected to 0
    [1],       # Node 3 is connected to 1
    [1]        # Node 4 is connected to 1
]

Execution:

    Initialization:
        vis = [1, 0, 0, 0, 0]
        q = deque([0])
        bfs = []

    First Iteration (q = [0]):
        node = q.popleft() = 0
        bfs = [0]
        Neighbors of 0: [1, 2]
            Visit 1: vis = [1, 1, 0, 0, 0], q = [1]
            Visit 2: vis = [1, 1, 1, 0, 0], q = [1, 2]

    Second Iteration (q = [1, 2]):
        node = q.popleft() = 1
        bfs = [0, 1]
        Neighbors of 1: [0, 3, 4]
            0 is already visited.
            Visit 3: vis = [1, 1, 1, 1, 0], q = [2, 3]
            Visit 4: vis = [1, 1, 1, 1, 1], q = [2, 3, 4]

    Third Iteration (q = [2, 3, 4]):
        node = q.popleft() = 2
        bfs = [0, 1, 2]
        Neighbors of 2: [0]
            0 is already visited.

    Fourth Iteration (q = [3, 4]):
        node = q.popleft() = 3
        bfs = [0, 1, 2, 3]
        Neighbors of 3: [1]
            1 is already visited.

    Fifth Iteration (q = [4]):
        node = q.popleft() = 4
        bfs = [0, 1, 2, 3, 4]
        Neighbors of 4: [1]
            1 is already visited.

    Queue Empty:
        q = []
        BFS traversal completed.

Output:

[0, 1, 2, 3, 4]
Time Complexity:

    O(V + E):
        Each vertex is visited once (O(V)).
        Each edge is processed once (O(E)).

Space Complexity:

    O(V + E):
        Adjacency list requires O(V + E) space.
        Visited list requires O(V).
        Queue size is at most O(V).


"""

""" 
The reason we directly append 0 and assume the start vertex is 0 in this BFS implementation is due to the problem constraints and assumptions made in many graph-related questions or examples. Here's why:

    Default Starting Node in BFS Examples:
    BFS traversal typically starts from a specific node. In this case, 0 is chosen as the starting vertex because:
        Many competitive programming problems or examples specify that the graph is 0-indexed, and the traversal should begin from node 0.
        This simplifies the code and ensures consistent behavior when there is no explicit input for the starting vertex.

    Adjacency List Assumption:
    The adjacency list is generally constructed for all vertices in the range [0, V-1]. Hence, 0 is assumed to be a valid vertex.
"""
