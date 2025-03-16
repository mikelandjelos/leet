class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        stretchy = 0
        for word in words:
            i = j = 0
            while i < len(s) and j < len(word):
                if s[i] != word[j]:  # Mismatch
                    break

                # Count consecutive chars in `s`
                s_count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    s_count += 1

                # Count consecutive chars in `word`
                w_count = 1
                while j + 1 < len(word) and word[j] == word[j + 1]:
                    j += 1
                    w_count += 1

                # Check if word can be stretched
                if s_count < w_count or (s_count > w_count and s_count < 3):
                    break

                i += 1
                j += 1

            if len(s) == i and len(word) == j:
                stretchy += 1

        return stretchy
