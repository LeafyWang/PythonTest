class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_e = {}
        longest = 0
        start   = 0
        size = len(s)
        for i in range(size):
            c = s[i]
            if(c in dict_e and dict_e[c]>=start):
                longest = max(longest,i-start)
                start = dict_e[c] + 1
            dict_e[c] = i
        return max(longest,size-start)      
