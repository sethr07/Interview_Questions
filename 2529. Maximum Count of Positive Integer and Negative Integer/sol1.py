class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = neg = 0

        for i in range(len(nums)):

            if nums[i] > 0:
                pos += 1
            elif nums[i] < 0:
                neg += 1
        
        if neg is None:
            return pos
        if pos is None:
            return neg
        
        return max(pos, neg)
