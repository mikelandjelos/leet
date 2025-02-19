from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1: int) -> int:
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]  # Path compression.
                res = par[res]

            return res

        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] = rank[p2]
            else:
                par[p1] = p2
                rank[p2] = rank[p1]

            return True

        result = n
        for n1, n2 in edges:
            result -= 1 if union(n1, n2) else 0

        return result
