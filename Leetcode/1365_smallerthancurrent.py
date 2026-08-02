class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        rank = {}
        for index, num in enumerate(sorted_nums):
            if num not in rank:
                rank[num] = index
        return [rank[num] for num in nums]