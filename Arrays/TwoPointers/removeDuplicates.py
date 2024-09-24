

inp_arr = list(map(int, input().split()))

uni_dict = set(inp_arr)  # SC O(N) extra space used  and TC O(NLog(N))
print("Dict before==>", uni_dict)
inp_arr = list(uni_dict)
print(len(uni_dict))
print(inp_arr)


print("##--------------------------------------##")

# TC O(NLog(N)) and SC O(N)


def removeDuplicates(nums: list[int]) -> int:
    uni_dict = set(nums)
    nums.clear()
    nums = list(uni_dict)
    # This solution wasnt being accepted because the question asked to not create a new array but to modify the esisting one so when u assign the array with "=" you're still essentially creating a new array instead you should loop over the array and append values to it.
    nums.sort()
    return len(uni_dict)


print("Function==>", removeDuplicates([1, 1, 2]))


# region optimal
# TC O(N) and SC O(1)

def removeDuplicatesOptimal(nums: list[int]) -> int:
    i = nums[0]
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i+1


print(removeDuplicatesOptimal(
    [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]))
