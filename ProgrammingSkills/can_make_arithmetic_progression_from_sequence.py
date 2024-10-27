class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        n = len(arr)

        if n <= 2:
            return True

        a = min(arr)
        Sn = sum(arr)
        d = 2 * (Sn - a) / (n * (n - 1))

        print(a)
        print(n)
        print(Sn)
        print(d)

        if d == 0:
            return True

        return n * (n - 1) / 2 == sum(map(lambda num: (num - a) / d, arr))
