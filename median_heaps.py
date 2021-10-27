# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)). 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:

# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:

# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:

# Input: nums1 = [2], nums2 = []
# Output: 2.00000
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

from typing import List
import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mid = (len(nums1) + len(nums2)) // 2

        merged_array = []
        for item in nums1:
            merged_array.append(item)
        for item in nums2:
            merged_array.append(item)

        left_arr = merged_array[:mid]
        right_arr = merged_array[mid:]

        heapq.heapify(right_arr)
        heapq._heapify_max(left_arr)

        right_element = heapq.heappop(right_arr)
        left_element = heapq.heappop(left_arr)

        if len(right_arr) == 0:
            return left_element
        elif len(left_arr) == 0:
            return right_element
        return (right_element + left_element) / 2
        
solution = Solution()
nums1 = [1, 3]
nums2 = [2]
print(solution.findMedianSortedArrays(nums1, nums2))
nums1 = [1, 3]
nums2 = [2, 4]
print(solution.findMedianSortedArrays(nums1, nums2))