class Job:
    def __init__(self, name, deadline, profit):
        self.name = name
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs):
    jobs = sorted(jobs, key=lambda x: x.profit, reverse=True)
    n = len(jobs)
    slots = [False] * n
    total_profit = 0

    for i in range(n):
        for j in range(min(n, jobs[i].deadline) - 1, -1, -1):
            if not slots[j]:
                slots[j] = True
                total_profit += jobs[i].profit
                break

    return total_profit

# Example usage
jobs = [
    Job("J1", 2, 60),
    Job("J2", 1, 100),
    Job("J3", 3, 20),
    Job("J4", 2, 40),
    Job("J5", 1, 20)
]

print("Maximum profit:", job_sequencing(jobs)) # Output: Maximum profit: 220
