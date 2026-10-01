class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1
        y = abs(x)
        int_min = -(2**31)
        int_max = (2**31)-1

        while y != 0:
            rem = y % 10
            rev = rev * 10 + rem
            y = y // 10
        
        ans = rev

        if x < 0:
            ans = ans * sign


        if int_min <= ans <= int_max:
            return ans
        else:
            return 0