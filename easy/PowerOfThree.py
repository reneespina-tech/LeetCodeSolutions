# 326. Power of Three
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

 

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33
# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).
 

# Constraints:

# -231 <= n <= 231 - 1

# Explanation on this code below:

        # temp = n // 3

        # if n // 3 == 3:
        #     return True
        # elif n == 0:
        #     n = 1
        #     return False
        # else:
        #     return False

# while my first code is correct in some cases,
# it only checks a fixed number of divisions and
# doesn't handle all powers of three (e.g. 81, 243...).
# it also used / (float division) instead of // (integer division),
# and was missing a return on the else branch.

# the fix was to use a while loop that keeps dividing n by 3
# as long as n > 1. inside the loop, we check if n % 3 != 0 —
# meaning n is not cleanly divisible by 3 — and immediately
# return False. otherwise we keep dividing.
# after the loop, we return n == 1, because if we divided
# cleanly all the way down, n will always end up as 1.

class Solution(object):
    def powerOfThree(self, s):

        while n > 1:
            if n % 3 != 0:
                return False
            n = n // 3
        
        return n == 1
            

