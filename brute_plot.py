import matplotlib.pyplot as plt
import random
import timeit
import itertools

# To generate random value for input


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
    return max_profit, best_schedule


def job_scheduling_brute_force(jobs):
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
    return best_schedule, max_profit


def analyze_performance_best(jobs_best_list, input_range):

    input_sizes = []
    best_case_times = []

    # Create input array of jobs
    i = 0
    for size in input_range:
        jobs = jobs_best_list[i]

        input_sizes.append(size)

        # Start timer
        start_time = timeit.default_timer()
        # Run brute force algorithm
        result = job_scheduling_brute_force(jobs)
        # End timer
        end_time = timeit.default_timer()
        # Calculate execution time
        execution_time = end_time - start_time
        best_case_times.append(execution_time)
        i += 1
    return input_sizes, best_case_times


def analyze_performance_worst(jobs_worst_list, input_range):

    input_sizes = []
    worst_case_times = []

    # Create input array of jobs
    i = 0
    for size in input_range:
        jobs = jobs_worst_list[i]
        input_sizes.append(size)

        # Start timer
        start_time = timeit.default_timer()
        # Run brute force algorithm
        result = job_scheduling_brute_force(jobs)
        # End timer
        end_time = timeit.default_timer()
        # Calculate execution time
        execution_time = end_time - start_time
        worst_case_times.append(execution_time)
        i += 1
    return input_sizes, worst_case_times


def analyze_performance_average(jobs_average_list, input_range):

    input_sizes = []
    average_case_times = []

    # Create input array of jobs
    i = 0
    for size in input_range:
        jobs = jobs_average_list[i]

        input_sizes.append(size)

        # Start timer
        start_time = timeit.default_timer()
        # Run brute force algorithm
        result = job_scheduling_brute_force(jobs)
        # End timer
        end_time = timeit.default_timer()
        # Calculate execution time
        execution_time = end_time - start_time
        average_case_times.append(execution_time)
        i += 1
    return input_sizes, average_case_times


if __name__ == "__main__":

    # Declaring input range
    input_range = range(1, 100, 10)

    # Create input array of jobs
    jobs_best_list = []
    jobs_worst_list = []
    jobs_average_list = []
    for size in input_range:
        jobs = {f'j{i+1}': [generate_random_values(), generate_random_values()]
                for i in range(size)}
        # For best case, sort the jobs in order of decreasing profit
        jobs_best = dict(
            sorted(jobs.items(), key=lambda x: x[1], reverse=True))
        jobs_best_list.append(jobs_best)
        # For worst case, sort the jobs in order of increasing profit
        jobs_worst = dict(
            sorted(jobs.items(), key=lambda x: x[1]))
        jobs_worst_list.append(jobs_worst)
        # For average case, send random values
        jobs_average_list.append(jobs)

    # Plot Graph
    input_sizes_best, best_case_times = analyze_performance_best(
        jobs_best_list, input_range)
    input_sizes_worst, worst_case_times = analyze_performance_worst(
        jobs_worst_list, input_range)
    input_sizes_average, average_case_times = analyze_performance_average(
        jobs_average_list, input_range)
    plt.plot(input_sizes_best, best_case_times, label='Best Case')
    plt.plot(input_sizes_worst, worst_case_times, label='Worst Case')
    plt.plot(input_sizes_average, average_case_times, label='Average Case')
    plt.xlabel('Input Size')
    plt.ylabel('Running Time')
    plt.title('Job Scheduling - Brute Force')
    plt.legend()
    plt.show()
