class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        array = [0]
        length = len(s)
        start, end = 0, 1
        while end < length + 1:
            now = s[start:end]
            if len(now) == len(set(now)):
                array.append(len(now))
                end += 1
            else:
                start += 1
        return max(array)
