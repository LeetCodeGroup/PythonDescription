class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        start = 0
        end = len(nums)-1
        if end == -1:
            return [-1,-1]
        res = self.checkRule(start,end)

        return res
        
        
    def checkRule(self,start,end):
        if start == end:
            if self.target == self.nums[start]:
                return [start,end]
            else:
                return [-1,-1]
        
        s1,m1=self.checkRule(start,(start+end)/2)
        m2,e2=self.checkRule((start+end)/2+1,end)
        
        if s1==-1:
            return [m2,e2]
        if m2==-1:
            return [s1,m1]
        return [s1,e2]
