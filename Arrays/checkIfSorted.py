

inp_arr = list(map(int, input().split()))
ans = True
for i in range(1, len(inp_arr)-1):
    if inp_arr[i] <= inp_arr[i+1] and inp_arr[i-1] <= inp_arr[i]:
        continue
    elif inp_arr[i] >= inp_arr[i+1] and inp_arr[i-1] >= inp_arr[i]:
        continue
    else:
        ans = False
        break

print(ans)
