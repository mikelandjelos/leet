class TimeMap(object):

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.store:
            return ""

        values = self.store[key]

        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) >> 1
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        if right >= 0:
            return values[right][1]
        return ""  # No valid timestamp found
