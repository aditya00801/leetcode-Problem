class Solution:
    def countMajoritySubarrays(self, nums, target):
        # Get the size of the array
        n = len(nums)

        # Stores the final answer
        ans = 0

        # Choose the starting index of every subarray
        for i in range(n):

            # Number of times target appears in the current subarray
            count = 0

            # Extend the subarray from i to j
            for j in range(i, n):

                # Update target count if current element is target
                if nums[j] == target:
                    count += 1

                # Current subarray length
                length = j - i + 1

                # Majority condition:
                # target_count > half of subarray length
                if count > length // 2:
                    ans += 1

        # Return total valid subarrays
        return ans