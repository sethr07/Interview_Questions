   def pivotIndex(self, nums: List[int]) -> int:

        pre = sum(nums)
        l = 0

        for idx, s in enumerate(nums):
            if l == pre - l - s:
                return idx
            l += s
        
        return -1
