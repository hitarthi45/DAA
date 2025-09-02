#Job Scheduling
def Job_scheduling(deadline, profit):
    n = len(profit)
    jobs = sorted(zip(deadline, profit), key=lambda x: x[1], reverse=True)
    max_deadline = max(deadline)
    slots = [-1] * max_deadline
    total_profit = 0
    for job in jobs:
        for j in range(job[0] - 1, -1, -1):
            if slots[j] == -1:
                slots[j] = job[1]
                total_profit += job[1]
                break
    return max_deadline,total_profit

deadline = [2, 1, 2, 1, 5]
profit = [100, 19, 27, 25, 15]
print("Maximum profit from job scheduling:", Job_scheduling(deadline, profit))
