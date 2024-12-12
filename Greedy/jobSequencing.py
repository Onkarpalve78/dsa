# https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1


def jobSequencing(jobs: list[list[int]]):
    jobs.sort(key=lambda x: x[2], reverse=True)
    maxDeadline = jobs[0][1]

    for i in range(1, len(jobs)):
        if jobs[i][1] > maxDeadline:
            maxDeadline = jobs[i][1]

    slots = [-1]*(maxDeadline+1)
    countJobsDone = 0
    contTotalProfit = 0

    for i in range(len(jobs)):
        # checking till the deadline if there are any slots free
        for j in range(jobs[i][1], 0, -1):
            if slots[j] == -1:
                slots[j] = i
                countJobsDone += 1
                contTotalProfit += jobs[i][2]
                break

    return countJobsDone, contTotalProfit


print(jobSequencing([(1, 4, 20), (2, 1, 1), (3, 1, 40), (4, 1, 30)]))
