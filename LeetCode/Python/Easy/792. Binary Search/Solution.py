class Solution:
    def binary_search(self, nums, low, high, target):
        if low > high:
            return -1
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(nums, mid+1, high, target)
        else:
            return self.binary_search(nums, low, mid-1, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums,0, len(nums)-1, target)