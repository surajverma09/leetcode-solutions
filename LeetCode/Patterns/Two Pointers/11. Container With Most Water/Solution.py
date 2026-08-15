class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height)-1

        while left < right:
            width = right - left

            hight = min(height[left], height[right])     

            maxi_water = width * hight
            
            max_water = max(maxi_water, max_water)
            
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
            
        
        return max_water
