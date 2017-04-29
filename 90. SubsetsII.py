class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        nums.sort()
        res =[[]]
        for i in range(length):
            index = 0
            up_max = len(res)
            while index != up_max:
                temp = res[index][:]
                temp.append(nums[i])
                if temp in res:
                    index = index + 1
                    continue
                res.append(temp)
                index = index+1
        return res