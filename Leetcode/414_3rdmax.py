import math

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = -float('inf')
        
        for num in nums:
            # Skip duplicates of existing top 3 numbers
            if num in (first, second, third):
                continue
            
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num
                
        return third if third != -float('inf') else first