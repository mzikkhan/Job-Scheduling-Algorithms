import matplotlib.pyplot as plt
import random
import timeit

# To generate random value for input


def generate_random_values():
    value = random.randint(1, 20)
    return value


def job_scheduling_dp(jobs):
    """
    Solves the job scheduling problem using dynamic programming.

    Args:
        jobs: A dictionary of jobs, where the key is the job ID and the value is a tuple of (start time, end time, profit).

    Returns:
        The maximum profit that can be obtained by scheduling the jobs.
    """

    # Convert the dictionary of jobs to a list of tuples
    jobs_list = list(jobs.items())

    # Sort the jobs in increasing order of end times
    sorted_jobs = sorted(jobs_list, key=lambda x: x[1][1])

    # Create a table to store the maximum profit that can be obtained by scheduling
    # the first i jobs, where i is the index of the job in the sorted list.
    dp = [0] * len(sorted_jobs)

    # Initialize the table.
    dp[0] = sorted_jobs[0][1][2]

    # Fill in the table.
    for i in range(1, len(sorted_jobs)):
        current_job = sorted_jobs[i]
        prev_job_index = find_previous_job_index(sorted_jobs, i)
        include_profit = current_job[1][2] + dp[prev_job_index]
        dp[i] = max(include_profit, dp[i - 1])

    # Return the maximum profit that can be obtained by scheduling all of the jobs.
    return dp[-1]


def find_previous_job_index(sorted_jobs, current_job_index):
    """
    Finds the index of the latest job that is compatible with the current job.

    Args:
        sorted_jobs: The list of jobs sorted in increasing order of end times.
        current_job_index: The index of the current job.

    Returns:
        The index of the previous job that is compatible with the current job.
    """
    for i in range(current_job_index - 1, -1, -1):
        if sorted_jobs[i][1][1] <= sorted_jobs[current_job_index][1][0]:
            return i
    return -1


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
        # Run dynamic programming algorithm
        result = job_scheduling_dp(jobs)
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
        # Run dynamic programming algorithm
        result = job_scheduling_dp(jobs)
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
        # Run dynamic programming algorithm
        result = job_scheduling_dp(jobs)
        # End timer
        end_time = timeit.default_timer()
        # Calculate execution time
        execution_time = end_time - start_time
        average_case_times.append(execution_time)
        i += 1
    return input_sizes, average_case_times


# Main Function
if __name__ == "__main__":

    # Declaring input range
    input_range = range(1, 15)

    # Create input array of jobs
    jobs_best_list = []
    jobs_worst_list = []
    jobs_average_list = []
    for size in input_range:
        jobs = {f'j{i+1}': (generate_random_values(), generate_random_values(), generate_random_values())
                for i in range(size)}
        # For best case, sort the jobs in order of decreasing profit
        jobs_best = dict(
            sorted(jobs.items(), key=lambda x: x[1][2], reverse=True))
        jobs_best_list.append(jobs_best)
        # For worst case, sort the jobs in order of increasing profit
        jobs_worst = dict(
            sorted(jobs.items(), key=lambda x: x[1][2]))
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
    plt.title('Job Scheduling - Dynamic Programming')
    plt.legend()
    plt.show()
