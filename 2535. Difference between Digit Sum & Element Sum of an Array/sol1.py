# Time -> 2 mins

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        ele = dig = 0

        ele = sum(nums)

        for n in nums:
            if len(str(n)) == 1:
                dig += n
            else:
                tmp = str(n)
                for ch in tmp:
                    dig += int(ch)
        
        return abs(ele-dig)
