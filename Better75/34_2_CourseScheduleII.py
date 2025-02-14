class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque

        if numCourses <= 1 or not prerequisites:
            return list(range(numCourses))

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
                elif indegrees[neighbor] < 0:
                    return []

        return sequence if len(sequence) == numCourses else []
