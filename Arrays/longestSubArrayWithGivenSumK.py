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
