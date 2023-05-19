import plotly.graph_objects as go
import timeit
import random
import itertools

# To generate random value for input


def generate_random_values():
    value = random.randint(1, 20)
    return value

# Brute Force Algorithm to calculate profit


def calculate_profit(schedule, l):
    size = l
    max_profit = 0
    current_time = []
    best_schedule = [0]*size

    for job in schedule:
        profit, deadline = jobs[job]
        # Check if deadline spot is empty
        # If so, add it to schedule and collect profit
        if deadline not in current_time:
            max_profit += profit
            best_schedule[deadline-1] = job
            current_time.append(deadline)
        # If not, keep going back in the schedule to fit the job and collect profit
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

# To Measure Execution Time


def measure_execution_time(jobs):
    # Create array deadline and store each job's deadline in this array
    deadline = [0]*len(jobs.keys())
    i = 0
    for job in jobs:
        deadline[i] = jobs[job][1]
        i += 1

    # Store max value of deadline and assign size of schedule to this
    size = max(deadline)

    # Generate all permutations of the jobs
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


if __name__ == "__main__":
    input_sizes = []
    execution_times = []

    # Declaring input range
    input_range = range(1, 100)

    # Create input array of jobs
    for size in input_range:
        jobs = {f'j{i+1}': [generate_random_values(), generate_random_values()]
                for i in range(size)}

        # Start timer
        start_time = timeit.default_timer()
        # Run brute force algorithm
        max_profit = measure_execution_time(jobs)
        # End timer
        end_time = timeit.default_timer()
        # Calculate execution time
        execution_time = end_time - start_time

        input_sizes.append(size)
        execution_times.append(execution_time)

    # Plot our graph
    fig = go.Figure(data=go.Scatter(
        x=input_sizes, y=execution_times, mode='lines'))
    fig.update_layout(title='Job Scheduling - Brute Force Algorithm',
                      xaxis_title='Input Size', yaxis_title='Execution Time (s)')
    fig.show()
