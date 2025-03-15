from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, path_len in times:  # O(E)
            graph[u].append((v, path_len))

        visited_vertices = set()
        priority_queue = [(0, k)]

        min_time = 0
        while priority_queue:
            path_len, vertex = heappop(priority_queue)  # O(logV)

            if vertex in visited_vertices:
                continue

            visited_vertices.add(vertex)
            min_time = max(min_time, path_len)

            for adjacent_vertex, edge_weight in graph[vertex]:
                if adjacent_vertex not in visited_vertices:
                    heappush(priority_queue, (path_len + edge_weight, adjacent_vertex))

        return min_time if len(visited_vertices) == n else -1
