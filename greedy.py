import matplotlib.pyplot as plt
import random
import timeit

# To generate random value for input


def generate_random_values():
    value = random.randint(1, 20)
    return value


def job_scheduling_greedy(jobs):
    # Store deadlines in an array and find max deadline
    deadline = [0] * len(jobs.keys())
    i = 0
    for job in jobs:
        deadline[i] = jobs[job][1]
        i += 1

    # Initialize size of our schedule to max value of deadline
    size = max(deadline)
    schedule = [0] * size
    max_profit = 0

    # Sort the jobs in decreasing order of profit
    jobs = dict(sorted(jobs.items(), key=lambda x: x[1], reverse=True))

    # Iterate over each job
    for job in jobs:
        # Check if schedule is empty
        if size != 0:
            # If deadline spot empty, assign job to that spot
            if schedule[jobs[job][1] - 1] == 0:
                schedule[jobs[job][1] - 1] = job
                max_profit += jobs[job][0]
                size -= 1
            # Otherwise, keep going back in schedule until you find empty spot
            else:
                length = jobs[job][1] - 2
                while length != -1:
                    if schedule[length] == 0:
                        schedule[length] = job
                        max_profit += jobs[job][0]
                        size -= 1
                        break
                    length -= 1

    return max_profit


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
        # Run greedy algorithm
        result = job_scheduling_greedy(jobs)
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
        # jobs = {f'j{i+1}': [generate_random_values(), generate_random_values()]
        #         for i in range(size)}
        jobs = jobs_worst_list[i]
        input_sizes.append(size)

        # Start timer
        start_time = timeit.default_timer()
        # Run greedy algorithm
        result = job_scheduling_greedy(jobs)
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
        # Run greedy algorithm
        result = job_scheduling_greedy(jobs)
        # End timer
        end_time = timeit.default_timer()
        # Calculate execution time
        execution_time = end_time - start_time
        average_case_times.append(execution_time)
        i += 1
    return input_sizes, average_case_times


if __name__ == "__main__":

    # Declaring input range
    input_range = range(1, 10000, 1000)

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
    plt.plot(input_sizes_worst, worst_case_times, label='Average Case')
    plt.plot(input_sizes_average, average_case_times, label='Worst Case')
    plt.xlabel('Input Size')
    plt.ylabel('Running Time')
    plt.title('Job Scheduling - Greedy')
    plt.legend()
    plt.show()
