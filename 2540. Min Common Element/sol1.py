# Time -> 3min 50 s

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        com = 0
        s1, s2 = set(nums1), set(nums2)

        z = s1.intersection(s2)
        print(z)
        if not z:
            return -1

        return min(z)
