# O(n*2)
# Time -> 2 mins 34 s
def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
  

        for i in range(1, len(nums)):
            s = nums[i] + sum(nums[:i])
            res.append(s)
        
        return res
