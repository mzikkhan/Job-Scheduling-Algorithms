# Jobs - profit, deadline
jobs = {'j1': [10, 1], 'j2': [5, 3], 'j3': [
    20, 2], 'j4': [1, 3], 'j5': [15, 2]}

# Create array deadline and store each job's deadline in this array
deadline = [0]*len(jobs.keys())
i = 0
for job in jobs:
    deadline[i] = jobs[job][1]
    i += 1

# Store max value of deadline and assign size of schedule to this
size = max(deadline)
schedule = [0]*size
max_profit = 0

# Sort the jobs in descending order of profit
jobs = dict(sorted(jobs.items(), key=lambda x: x[1], reverse=True))

# If deadline spot in schedule empty, assign job there orelse keep going back to place job
for job in jobs:
    if size != 0:
        if schedule[jobs[job][1] - 1] == 0:
            schedule[jobs[job][1] - 1] = job
            max_profit += jobs[job][0]
            size -= 1
        else:
            length = jobs[job][1] - 2
            while length != -1:
                if schedule[length] == 0:
                    schedule[length] = job
                    max_profit += jobs[job][0]
                    size -= 1
                    break
                length -= 1

print("Best Schedule:", schedule)
print("Max Profit:", max_profit)
