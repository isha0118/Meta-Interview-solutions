class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validatePalindrome(s, i, j):
            while i < j:
                if s[i] is not s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        i, j = 0, len(s)-1
        while i < j:
            if s[i] is not s[j]:
                return validatePalindrome(s, i+1, j) or validatePalindrome(s, i, j-1)
            i += 1
            j -= 1
        return True


