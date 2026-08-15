class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dist = {}
        alpha = True
        i = 0

        while len(nums)>i:
            if nums[i] in dist:
                return True
            else:
                dist[nums[i]] = 1
                alpha = False
            i += 1
    
        return False