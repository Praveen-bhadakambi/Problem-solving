# 0026. Remove Duplicates from Sorted Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Approach: Two pointers (in-place)
# Time: O(n) | Space: O(1)

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # k is the position where the next unique value will be written
        k = 1

        for i in range(1, len(nums)):
            # The array is sorted, so a new value differs from the previous one
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k