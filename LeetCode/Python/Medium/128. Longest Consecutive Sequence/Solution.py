class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        if len(nums)==0:
            return 0
        longest = 1

        for i in seen:
            if (i-1) in seen:
                continue
            else:
                count = 1
                right = i
                while (right+1) in seen:
                    count += 1
                    right += 1
                if count > longest:
                    longest = count
        return longest