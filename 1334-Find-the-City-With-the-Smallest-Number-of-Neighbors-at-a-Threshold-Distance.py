from collections import defaultdict
import heapq
from typing import List

# TODO: resolve it again
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)

        for v1, v2, w in edges:
            adj[v1].append((v2, w))
            adj[v2].append((v1, w))
        
        def dijkstra(start):
            heap = [(0, start)]
            visited = set()

            while heap:
                dist, node = heapq.heappop(heap)

                if node in visited:
                    continue

                visited.add(node)

                for neighbor, weight in adj[node]:
                    new_dist = dist + weight
                    if new_dist <= distanceThreshold:
                        heapq.heappush(heap, (new_dist, neighbor))
            return len(visited) - 1
        

        min_cities = n
        min_city = -1

        for i in range(n):
            cities = dijkstra(i)
            if cities <= min_cities:
                min_cities = cities
                min_city = i
        
        return min_city