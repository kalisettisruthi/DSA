class Solution(object):
    def runningSum(self, nums):
        n = len(nums)
        runningSum = []
        sum = 0
        for i in range(0,n):
            sum = sum + nums[i]
            runningSum.append(sum)
        return runningSum