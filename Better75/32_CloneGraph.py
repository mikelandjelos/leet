class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        old_new = {}

        def dfs(node):
            if not node or node in old_new:
                return node

            new_node = Node(val=node.val)
            old_new[node] = new_node

            for old_neighbor in node.neighbors:
                new_neighbor = old_new.get(old_neighbor)
                if new_neighbor is None:
                    new_neighbor = dfs(old_neighbor)

                new_node.neighbors.append(new_neighbor)

            return old_new[node]

        return dfs(node)
