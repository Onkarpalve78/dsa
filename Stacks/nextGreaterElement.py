

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]


def nextGreaterElement(nums1, nums2) -> list[int]:
    nums2_len = len(nums2)
    # Length of nums2

    nge = [-1]*nums2_len
    # Initialize nge (next greater element) list with -1 for all elements. This list will store the next greater elements for nums2.

    st = []
    # Stack to keep track of the elements for which we need to find the next greater element

    nums2_index_map = {}
    # Dictionary to map each element of nums2 to its index

    ans = []
    # Resultant list to store the next greater elements for nums1

    for i in range(nums2_len-1, -1, -1):
        # Loop through nums2 from the end to the start

        while st and st[-1] < nums2[i]:
            st.pop()
            # Pop elements from stack while stack is not empty and top element is smaller than the current nums2 element

        if st:
            nge[i] = st[-1]
            # If stack is not empty after popping, the current top element of the stack is the next greater element for nums2[i]

        st.append(nums2[i])
        # Push the current element of nums2 onto the stack

    for i in range(nums2_len):
        nums2_index_map[nums2[i]] = i
        # Populate the dictionary with elements of nums2 and their corresponding indices

    for i, num in enumerate(nums1):
        # Loop through each element in nums1

        if num in nums2_index_map:
            ans.append(nge[nums2_index_map[num]])
            # Use the dictionary to find the index of num in nums2 and use that index to find the next greater element from the nge list. Append this next greater element to ans.

    return ans


print(nextGreaterElement(nums1, nums2))
