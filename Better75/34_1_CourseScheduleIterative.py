class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses <= 1 or not prerequisites:
            return True

        adj_list = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)

        # 0 = unvisited, 1 = visiting, 2 = fully visited
        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:  # Cycle detected.
                return False
            if visited[course] == 2:  # Fully visited node - not a cycle.
                return True

            # Visiting current node.
            visited[course] = 1

            # Visit all adjacent nodes.
            for neighbor in adj_list[course]:
                if not dfs(neighbor):
                    return False

            # Fully visited.
            visited[course] = 2
            return True

        # Step 4: Check each course for cycles.
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
