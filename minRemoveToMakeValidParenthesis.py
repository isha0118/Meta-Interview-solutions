class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def twoPass(s, openB, closingB):
            count = 0
            partiallyValid = []
            for c in s:
                if c is openB:
                    count += 1
                elif c is closingB:
                    if count is 0:
                        continue
                    count -= 1
                partiallyValid.append(c)
            return "".join(partiallyValid)
        s = twoPass(s,'(',')')
        s = twoPass(s[::-1], ')', '(')
        return s[::-1]

        # O(n) for 2 pass, O(n) for partially_valid used to build solution
