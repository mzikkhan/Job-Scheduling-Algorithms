jobs = { 'j1': [10, 1], 'j2': [5, 3], 'j3': [20, 2], 'j4': [1, 3], 'j5': [15, 2] }

deadline = [0]*len(jobs.keys())
i = 0
for job in jobs:
    deadline[i] = jobs[job][1]
    i+=1
print(deadline)

size = max(deadline)

schedule = [0]*size
max_profit = 0

jobs = dict(sorted(jobs.items(), key=lambda x:x[1], reverse=True))

for job in jobs:
    if size != 0:
        if schedule[jobs[job][1] - 1]==0:
            schedule[jobs[job][1] - 1] = job
            max_profit += jobs[job][0]
            size -= 1
        else:
            length = jobs[job][1] - 2
            while length != -1:
                if schedule[length]==0:
                    schedule[length] = job
                    max_profit += jobs[job][0]
                    size -= 1
                    break
                length -= 1

print(schedule)
print(max_profit)

