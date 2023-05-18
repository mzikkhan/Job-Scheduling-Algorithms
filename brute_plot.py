import plotly.graph_objects as go
import timeit
import random
import itertools


def generate_random_values():
    value = random.randint(1, 20)
    return value


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
    return max_profit


def measure_execution_time(jobs):
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


input_sizes = []
execution_times = []

input_range = range(1, 100)

for size in input_range:
    jobs = {f'j{i+1}': [generate_random_values(), generate_random_values()]
            for i in range(size)}

    start_time = timeit.default_timer()
    max_profit = measure_execution_time(jobs)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time

    input_sizes.append(size)
    execution_times.append(execution_time)

fig = go.Figure(data=go.Scatter(
    x=input_sizes, y=execution_times, mode='lines'))
fig.update_layout(title='Job Scheduling - Brute Force Algorithm',
                  xaxis_title='Input Size', yaxis_title='Execution Time (s)')
fig.show()
