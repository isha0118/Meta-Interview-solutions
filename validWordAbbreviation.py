class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] is '0':    #edge case
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
            elif word[i] != abbr[j]:
                return False
            else:
                i+=1
                j+=1
        return i is len(word) and j is len(abbr)

        # O(m) — length of abbreviation
        # Space: O(1)
                