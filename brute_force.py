# Import modules
import itertools

# Jobs input
jobs = {'j1': [10, 1], 'j2': [5, 3], 'j3': [
    20, 2], 'j4': [1, 3], 'j5': [15, 2]}

# Calculates max profit for a given schedule


def calculate_profit(schedule, l):
    size = l
    max_profit = 0
    current_time = []
    best_schedule = [0]*size

    for job in schedule:
        profit, deadline = jobs[job]
        # Check if deadline has already been checked
        # If not, add it to schedule and collect profit
        if deadline not in current_time:
            max_profit += profit
            best_schedule[deadline-1] = job
            current_time.append(deadline)
        # If yes, keep going back in the schedule to fit the job and collect profit
        else:
            deadline2 = deadline - 1
            while deadline2 != 0:
                if deadline2 in current_time:
                    deadline2 -= 1
                else:
                    max_profit += profit
                    best_schedule[deadline2-1] = job
                    current_time.append(deadline2)
                    break
    return max_profit, best_schedule


# Create array deadline and store each job's deadline in this array
deadline = [0]*len(jobs.keys())
i = 0
for job in jobs:
    deadline[i] = jobs[job][1]
    i += 1

# Store max value of deadline and assign size of schedule to this
size = max(deadline)

# Generate all permutations of the job names
job_names = list(jobs.keys())
permutations = list(itertools.permutations(job_names, size))
max_profit = 0
best_schedule = []

# Iterate over all permutations and calculate the profit for each schedule
for permutation in permutations:
    profit, schedule = calculate_profit(permutation, size)
    # If profit is greater than max_profit, store it as max_profit and save the corresponding schedule
    if profit > max_profit:
        max_profit = profit
        best_schedule = schedule

print("Best Schedule:", best_schedule)
print("Max Profit:", max_profit)
