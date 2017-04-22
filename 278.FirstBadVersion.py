# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            if isBadVersion(1):
                return 1
            else:
                return 0
        start = 1
        medium = n/2
        end = n
        while start != end:
            if isBadVersion(medium):
                end = medium
                medium = (medium+start)/2
            else:
                start = medium+1
                medium = (end+start)/2
        return medium