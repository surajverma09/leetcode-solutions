class Solution:
    def isPowerOfThree( self, n: int) -> bool:
        if n == 3**1 or n == 3**2 or n == 3**3 or n == 3**4 or n == 3**5 or n == 3**6 or n ==  3**7 or n == 3**8 or n == 3**9 or n == 3**10 or n == 3**11 or n == 3**12 or n == 3**13 or n == 3**14 or n == 3**15 or n == 3**16 or n == 3**17 or n == 3**18 or n == 3**19 or n == 1:
            return True
        elif n == 0:
            return False
        elif n < 0:
            return False
        else:
            return False
        