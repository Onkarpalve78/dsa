# # LC 118 https://leetcode.com/problems/pascals-triangle/description/
# # Can't believe this code worked!!! although with worst complexity but this code worked and got submitted in first attempt! :')
# numRows = int(input("Enter length of triangle: "))
# count = 0
# pascal_arr = []
# while count != numRows:
#     sub_arr = []
#     if count == 0:
#         sub_arr.append(1)
#         pascal_arr.append(sub_arr)
#         count += 1
#         continue
#     # sub_arr.clear()
#     count += 1
#     flag = True
#     i, j = 0, 0
#     while flag:
#         arr_to_look_at = pascal_arr[-1]
#         if i == j:
#             sub_arr.append(1)
#             if len(sub_arr) == count:
#                 flag = False
#             if j < len(arr_to_look_at)-1:
#                 j += 1
#                 continue

#         if j > i:
#             sub_arr.append(arr_to_look_at[i]+arr_to_look_at[j])
#             if len(sub_arr) == count:
#                 flag = False
#             if j < len(arr_to_look_at)-1:
#                 j += 1
#             if i < len(arr_to_look_at)-1:
#                 i += 1
#             continue
#     i, j = 0, 0
#     pascal_arr.append(sub_arr)


# for item in pascal_arr:
#     print(item)


# NOTE: GPT's Approach, works so learn this!

# Get the number of rows in Pascal's Triangle
numRows = int(input("Enter length of triangle: "))
pascal_arr = []

# Generate each row of Pascal's Triangle
for count in range(numRows):
    sub_arr = []  # Temporary sub-array for the current row

    # First element of each row is always 1
    sub_arr.append(1)

    # For rows with more than 1 element, calculate the middle elements
    if count > 0:
        prev_row = pascal_arr[- 1]

        # Calculate the values in between the first and last element
        for i in range(1, count):  # when count is 1, loop doesnt run, cuz range(1,1)
            # has no in between range to iterate over, the amount of times range will run a loop depends on (right value)-(left value)
            sub_arr.append(prev_row[i - 1] + prev_row[i])
            print("prev row: ", prev_row[i-1], prev_row[i], count)

        # Last element of each row is always 1
        sub_arr.append(1)

    # Add the generated row to pascal_arr
    pascal_arr.append(sub_arr)

# Print Pascal's Triangle
for row in pascal_arr:
    print(row)
