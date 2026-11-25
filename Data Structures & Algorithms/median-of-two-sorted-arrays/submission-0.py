class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A = nums2
            B = nums1
        total = len(nums1) + len(nums2)
        half = total // 2

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2
            a_l = A[i] if i >= 0 else float('-inf')
            b_l = B[j] if j >= 0 else float('-inf')
            a_r = A[i + 1] if i + 1 < len(A) else float('inf')
            b_r = B[j + 1] if j + 1 < len(B) else float('inf')

            if a_l <= b_r and b_l <= a_r:
                if total % 2:
                    return min(a_r, b_r)
                return (max(a_l, b_l) + min(a_r, b_r)) / 2
            elif a_l > b_r:
                r = i - 1
            else:
                l = i + 1
