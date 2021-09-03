# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while True:
            mid = left + (right - left) // 2

            if not isBadVersion(mid):
                left = mid + 1
            else:
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    right = mid - 1

