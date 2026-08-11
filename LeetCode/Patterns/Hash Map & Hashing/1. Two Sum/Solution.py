class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        i = 0

        while len(nums)>i:
            need = target - nums[i]
            if need in dictionary:
                return [dictionary[need],i]
            else:
                dictionary[nums[i]] = i
            i += 1
            