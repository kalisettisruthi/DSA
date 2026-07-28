class Solution(object):
    def getConcatenation(self, nums,n=None):
        if n is None :
            n = len(nums)
        ans = []
        #for loop
        for i in range(2) :
            ans.extend(nums)
        return ans