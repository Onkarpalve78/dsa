# Q] Find longest subarray with give sum k
# Read a list of integers from input
nums = list(map(int, input().split()))
# Read the target sum 'k' from input
k = int(input())


def longestSubArray(nums, k):
    preSum = {}
    # Dictionary to store the prefix sums and their corresponding indices
    max_len = 0
    # Variable to store the maximum length of subarray found
    current_sum = 0
    # Variable to store the current running sum

    # Iterate over the array using enumerate to get both index and value
    for i, num in enumerate(nums):
        current_sum += num
        # Add the current number to the running sum

        # Check if the current running sum is equal to target sum 'k'
        if current_sum == k:
            max_len = max(max_len, i+1)
            # Update max_len to the current index + 1

        # Calculate the remaining sum needed to reach 'k'
        remaining = current_sum - k

        # If the remaining sum is already in preSum, update max_len
        if remaining in preSum:
            max_len = max(max_len, i - preSum[remaining])

        # If current_sum is not already in preSum, add it with its index
        if current_sum not in preSum:
            preSum[current_sum] = i

    # Print the prefix sum dictionary for debugging purposes
    print(preSum)
    # Return the maximum length of the subarray found
    return max_len


# Test the function with the input numbers and target sum 'k'
print(longestSubArray(nums, k))
# Explaination:
# Suppose nums = [1, 2, 3, 2, 5] and k = 5.

# At i = 3 (value = 2), current_sum = 8.
# remaining = current_sum - k = 8 - 5 = 3.
# If preSum[3] = 1 (prefix sum 3 was seen at index 1), then:
# The subarray [3, 2] (from index 2 to 3) has a sum of 5.
# Its length is i - preSum[remaining] = 3 - 1 = 2.
# This logic ensures that the algorithm efficiently finds the longest subarray with the given sum k.4. Updating max_len:

# max_len keeps track of the maximum length of any subarray found so far that sums to k.
# If the current subarray (of length i - preSum[remaining]) is longer than max_len, it updates max_len.


def longestSubArrayMyCode(nums: list[int], k: int) -> int:
    presum = {}
    max_len = 0
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        presum[current_sum] = i

    for key, value in presum.items():
        if key == k:
            curr = nums[:value+1]
            max_len = max(max_len, len(curr))

        if key > k:
            remaining = key-k
            if remaining in presum:
                ans = presum[remaining]
                curr = nums[ans:value+1]
                max_len = max(max_len, len(curr))

    return max_len


print(longestSubArrayMyCode(nums, k))
