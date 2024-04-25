from collections import defaultdict
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # Special case when there's only one node

        # Construct adjacency list
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Find leaf nodes
        leaves = [node for node in range(n) if len(adj_list[node]) == 1]

        # Trim leaves until there are 1 or 2 nodes left
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = adj_list[leaf].pop()  # Remove leaf from its neighbor's list
                adj_list[neighbor].remove(leaf)  # Remove neighbor from the leaf's list
                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        # The remaining nodes are roots of MHTs
        return leaves
        