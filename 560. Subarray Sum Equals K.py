# 0560. Subarray Sum Equals K
# Difficulty: Medium 
# Link: https://leetcode.com/problems/subarray-sum-equals-k/description/
# Approach: Hash Map
# Time: O(n) | Space: O(n)
# solved by brute force and optimal solution

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            sum = 0

            for j in range(i, n):
                sum += nums[j]

                if sum == k:
                    count += 1

        return count


#optimal solution


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        prefix_sum = 0

        # Store prefix sum frequencies
        hashmap = {0: 1}

        for num in nums:

            # Calculate current prefix sum
            prefix_sum += num

            # Check whether previous prefix exists
            target = prefix_sum - k

            if target in hashmap:
                count += hashmap[target]

            # Store/update current prefix sum
            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

        return count