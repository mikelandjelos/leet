class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_note_letters = {}

        for letter in ransomNote:
            if letter not in ransom_note_letters:
                ransom_note_letters[letter] = 1
                continue

            ransom_note_letters[letter] += 1

        for letter in magazine:
            if letter not in ransom_note_letters:
                continue

            ransom_note_letters[letter] -= 1
            if ransom_note_letters[letter] == 0:
                del ransom_note_letters[letter]

        return len(ransom_note_letters) == 0
