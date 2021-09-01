class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_kth(k, nums1, nums2):
            n1 = len(nums1)
            n2 = len(nums2)
            if n1 == 0:
                return nums2[k - 1]
            if n2 == 0:
                return nums1[k - 1]
            if k == 1:
                return min(nums1[0], nums2[0])

            index1 = min(k // 2 - 1, n1 - 1)
            index2 = min(k // 2 - 1, n2 - 1)
            pivot1 = nums1[index1]
            pivot2 = nums2[index2]
            if pivot1 < pivot2:
                k -= index1 + 1
                return find_kth(k, nums1[index1 + 1: n1], nums2)
            else:
                k -= index2 + 1
                return find_kth(k, nums1, nums2[index2 + 1: n2])

        m = len(nums1) + len(nums2)
        if m % 2 == 1:
            k = (m + 1) // 2
            return find_kth(k, nums1, nums2)
        else:
            k = m // 2
            return (find_kth(k, nums1, nums2) + find_kth(k + 1, nums1, nums2)) / 2