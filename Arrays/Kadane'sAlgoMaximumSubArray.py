# LC 53 https://leetcode.com/problems/maximum-subarray/description/

# nums = list(map(int, input().split()))
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# region brute
#This code works but has a TC of O(N^3) and hence time limit exceeds on LC.
# def maximumSubArray(arr: list[int]) -> int:

#     maximmum = arr[0]
#     n = len(arr)
#     for i in range(n):
#         for j in range(i, n):
#             summation = sum(arr[i:j+1])
#             if summation > maximmum:

#                 maximmum = summation

#     return maximmum


# print(maximumSubArray(nums))

# region Kadane's Algo optimal
def maximumSubArray(arr: list[int]) -> int:
    current_sum=0
    maximum_sum=arr[0]
    
    for num in arr:
        
        current_sum+=num
            
        if current_sum>maximum_sum:
            maximum_sum=current_sum
            
        if current_sum<=0:
            current_sum=0
            
            
       
        
    return maximum_sum

print(maximumSubArray(nums))
            


