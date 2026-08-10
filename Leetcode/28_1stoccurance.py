class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Approach 1: Using Python's built-in str.find()
        # Returns index of first occurrence, or -1 if not found.
        return haystack.find(needle)
        