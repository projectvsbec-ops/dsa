class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer boundaries
        MIN_INT = -2147483648
        MAX_INT = 2147483647
        
        res = 0
        # Work with the absolute value to make modulo/division easier
        # but keep track of the sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            # Check for overflow before updating res
            # (res * 10 + pop) > MAX_INT
            if res > (MAX_INT - pop) // 10:
                return 0
            
            res = (res * 10) + pop
            
        return res * sign
