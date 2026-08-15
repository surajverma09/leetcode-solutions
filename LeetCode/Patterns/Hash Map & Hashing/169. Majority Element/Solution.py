class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = len(nums)/2
        i = 0
        dist = {}

        while len(nums)>i:
            if nums[i] in dist:
                dist[nums[i]] += 1
            else:
                dist[nums[i]] = 1
            i += 1
        
        for ch, count in dist.items():
            if count > major:
                return ch