class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height)-1

        while left < right:
            width = right - left
            if height[left] <= height[right]:
                hight = height[left]
            else:
                hight = height[right]

            maxi_water = width * hight
            if max_water < maxi_water:
                max_water = maxi_water
            
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
        
        return max_water
