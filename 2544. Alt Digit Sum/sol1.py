# Time -> 3 min 57 s

class Solution:
    def alternateDigitSum(self, n: int) -> int:

        num = str(n)
        s = 0

        for idx, digit in enumerate(num):
            if idx%2 != 0:
                s += -int(digit)
            else:
                s += int(digit)
        
        return s
