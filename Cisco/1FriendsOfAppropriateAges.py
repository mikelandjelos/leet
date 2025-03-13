from collections import Counter


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        age_groups = Counter(
            ages
        )  # O(n), but cardinality of `age_groups` map is max. 120, so space is O(1)
        num_requests = 0

        for age_X, num_X in age_groups.items():  # O(120) ~ O(1)
            for age_Y, num_Y in age_groups.items():  # O(120) ~ O(1)
                if age_Y > 0.5 * age_X + 7 and age_Y <= age_X:
                    num_requests += num_X * num_Y
                    if age_X == age_Y:
                        num_requests -= num_X

        return num_requests
