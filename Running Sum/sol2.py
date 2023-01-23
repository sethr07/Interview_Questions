# O(n)

def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        temp = 0

        for i in range(len(nums)):
            temp += nums[i]
            res.append(temp)

