class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import deque

        if numCourses <= 1 or not prerequisites:
            return True

        neighbor_list = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for course, prereq in prerequisites:
            neighbor_list[prereq].append(course)
            indegrees[course] += 1

        q = deque([i for i, indeg in enumerate(indegrees) if indeg == 0])
        sequence = []

        while q:
            course = q.popleft()
            sequence.append(course)

            for neighbor in neighbor_list[course]:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    q.append(neighbor)

        return len(sequence) == numCourses
