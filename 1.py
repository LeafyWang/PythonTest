class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        '''# brute force
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i]+nums[j]==target and i!=j):
                    return [i,j]'''
                
        # dictionary which only store one position for one value (but is useful)
        dictn = {}
        for i in range(len(nums)):
            if (target-nums[i] in dictn):
                if (i!=dictn[target-nums[i]]):
                    return [i,dictn[target-nums[i]]]
            else:
                dictn[nums[i]] = i
