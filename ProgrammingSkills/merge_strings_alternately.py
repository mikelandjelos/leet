class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        merged_word = []

        i = 0

        while i < len(word1):
            merged_word.append(word1[i])
            if i < len(word2):
                merged_word.append(word2[i])
            i += 1

        while i < len(word2):
            merged_word.append(word2[i])
            i += 1

        return "".join(merged_word)
