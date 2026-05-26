# 344. Reverse String
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.


# Explanation: The left side of this line s[:] means clearing the "s" then filling it with 
# the reversed values. While the right side s[::-1] means reading the list backwards and returns
# a new temporary list.


class Solution(object):
    def reverseString(self, s):
        s[:] = s[::-1]