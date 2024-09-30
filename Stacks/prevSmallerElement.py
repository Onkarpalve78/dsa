

def prevSmaller(A: list[int]):
    nums_len = len(A)
    pse = [-1]*nums_len
    st = []

    for i in range(nums_len):

        while st and st[-1] >= A[i]:
            st.pop()

        if st:
            pse[i] = st[-1]

        st.append(A[i])

    return pse


print(prevSmaller([4, 5, 2, 10, 8]))
