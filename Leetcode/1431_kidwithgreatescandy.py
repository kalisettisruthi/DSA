class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        #maximum candies
        max_candy = max(candies)
        result = []
        for candy in candies :
            if candy + extraCandies >= max_candy :
                result.append(True)
            else :
                result.append(False)    
        return result     