from typing import Optional

# Definition for a Node.


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # edge case, no nodes
        if not node:
            return None

        # hashmap to map original with copy
        node_to_clone = {}

        def dfs(node):
            # base case - check if node already mapped
            # avoid cycle
            if node in node_to_clone:
                return node_to_clone[node]  # return the copy

            # copy node
            node_copy = Node(node.val)
            node_to_clone[node] = node_copy

            # check neighbors, make copy and add to array
            for neighbor in node.neighbors:
                neighbor_copy = dfs(neighbor)
                node_copy.neighbors.append(neighbor_copy)  # add the copy

            return node_copy  # return copy

        # call recursive function
        dfs(node)

        return node_to_clone[node]

# Complexity
# Time: O(V + E) - the amount of vertices and edges
# Space: O(V) - vertices or nodes in the graph
