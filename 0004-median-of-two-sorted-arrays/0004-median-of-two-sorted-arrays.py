class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        total = m + n
        mid = total // 2
        i = j = 0
        merged = []
        while len(merged) <= mid:
            if i < m and (j >= n or nums1[i] < nums2[j]):
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        if total % 2 == 1:
            return merged[mid]
        else:
            return (merged[mid - 1] + merged[mid]) / 2.0