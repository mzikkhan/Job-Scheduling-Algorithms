# import matplotlib.pyplot as plt
# import random
# import timeit

# # To generate random value for input


# def generate_random_values():
#     value = random.randint(1, 20)
#     return value


# def job_scheduling_dynamic_programming(jobs):
#     # Store deadlines in an array and find max deadline
#     deadline = [0] * len(jobs.keys())
#     i = 0
#     for job in jobs:
#         deadline[i] = jobs[job][1]
#         i += 1

#     # Initialize size of our schedule to max value of deadline
#     size = max(deadline)
#     schedule = [0] * size
#     max_profit = 0

#     # Sort the jobs in decreasing order of profit
#     jobs = dict(sorted(jobs.items(), key=lambda x: x[1], reverse=True))

#     # Iterate over each job
#     for job in jobs:
#         # Check if schedule is full
#         if size != 0:
#             # If deadline spot empty, assign job to that spot
#             if schedule[jobs[job][1] - 1] == 0:
#                 schedule[jobs[job][1] - 1] = job
#                 max_profit += jobs[job][0]
#                 size -= 1
#             # Otherwise, keep going back in schedule until you find empty spot
#             else:
#                 length = jobs[job][1] - 2
#                 while length != -1:
#                     if schedule[length] == 0:
#                         schedule[length] = job
#                         max_profit += jobs[job][0]
#                         size -= 1
#                         break
#                     length -= 1

#     return max_profit


# def analyze_performance_best(jobs_best_list, input_range):

#     input_sizes = []
#     best_case_times = []

#     # Create input array of jobs
#     i = 0
#     for size in input_range:
#         jobs = jobs_best_list[i]

#         input_sizes.append(size)

#         # Start timer
#         start_time = timeit.default_timer()
#         # Run dynamic programming algorithm
#         result = job_scheduling_dynamic_programming(jobs)
#         # End timer
#         end_time = timeit.default_timer()
#         # Calculate execution time
#         execution_time = end_time - start_time
#         best_case_times.append(execution_time)
#         i += 1
#     return input_sizes, best_case_times


# def analyze_performance_worst(jobs_worst_list, input_range):

#     input_sizes = []
#     worst_case_times = []

#     # Create input array of jobs
#     i = 0
#     for size in input_range:
#         jobs = jobs_worst_list[i]
#         input_sizes.append(size)

#         # Start timer
#         start_time = timeit.default_timer()
#         # Run dynamic programming algorithm
#         result = job_scheduling_dynamic_programming(jobs)
#         # End timer
#         end_time = timeit.default_timer()
#         # Calculate execution time
#         execution_time = end_time - start_time
#         worst_case_times.append(execution_time)
#         i += 1
#     return input_sizes, worst_case_times


# def analyze_performance_average(jobs_average_list, input_range):

#     input_sizes = []
#     average_case_times = []

#     # Create input array of jobs
#     i = 0
#     for size in input_range:
#         jobs = jobs_average_list[i]

#         input_sizes.append(size)

#         # Start timer
#         start_time = timeit.default_timer()
#         # Run dynamic programming algorithm
#         result = job_scheduling_dynamic_programming(jobs)
#         # End timer
#         end_time = timeit.default_timer()
#         # Calculate execution time
#         execution_time = end_time - start_time
#         average_case_times.append(execution_time)
#         i += 1
#     return input_sizes, average_case_times


# if __name__ == "__main__":

#     # Declaring input range
#     input_range = range(1, 1000)

#     # Create input array of jobs
#     jobs_best_list = []
#     jobs_worst_list = []
#     jobs_average_list = []
#     for size in input_range:
#         jobs = {f'j{i+1}': [generate_random_values(), generate_random_values()]
#                 for i in range(size)}
#         # For best case, sort the jobs in order of decreasing profit
#         jobs_best = dict(
#             sorted(jobs.items(), key=lambda x: x[1], reverse=True))
#         jobs_best_list.append(jobs_best)
#         # For worst case, sort the jobs in order of increasing profit
#         jobs_worst = dict(
#             sorted(jobs.items(), key=lambda x: x[1]))
#         jobs_worst_list.append(jobs_worst)
#         # For average case, send random values
#         jobs_average_list.append(jobs)

#     # Plot Graph
#     input_sizes_best, best_case_times = analyze_performance_best(
#         jobs_best_list, input_range)
#     input_sizes_worst, worst_case_times = analyze_performance_worst(
#         jobs_worst_list, input_range)
#     input_sizes_average, average_case_times = analyze_performance_average(
#         jobs_average_list, input_range)
#     plt.plot(input_sizes_best, best_case_times, label='Best Case')
#     plt.plot(input_sizes_worst, worst_case_times, label='Worst Case')
#     plt.plot(input_sizes_average, average_case_times, label='Average Case')
#     plt.xlabel('Input Size')
#     plt.ylabel('Running Time')
#     plt.title('Job Scheduling - Dynamic Programming')
#     plt.legend()
#     plt.show()

import matplotlib.pyplot as plt
import random
import time

# list of jobs taken as input, where (job_id, deadline, profit)


def job_sequencing(jobs):
    # sorts the jobs in descending order of profit
    jobs.sort(key=lambda x: x[2], reverse=True)
    # max deadline among all jobs determined
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    # creates table to store max profit that can be obtained by considering a subset of jobs upto a certain deadline
    table = [[0] * (max_deadline + 1) for _ in range(len(jobs) + 1)]

    # iterates over the jobs and updates the tabe based on the dynamic programming algorithm
    for i in range(1, len(jobs) + 1):
        for j in range(1, max_deadline + 1):
            if jobs[i - 1][1] <= j:
                table[i][j] = max(table[i - 1][j], jobs[i - 1]
                                  [2] + table[i - 1][j - jobs[i - 1][1]])
            else:
                table[i][j] = table[i - 1][j]

    # tracks back through the table to determine optimal job sequence that maximizes profit
    sequence = []
    i, j = len(jobs), max_deadline
    while i > 0 and j > 0:
        if table[i][j] != table[i - 1][j]:
            sequence.append(jobs[i - 1])
            j -= jobs[i - 1][1]
        i -= 1
    sequence.reverse()

    max_profit = table[-1][-1]
    return max_profit, sequence

# takes number of jobs as input an generates list of random job with randowm deadlines and profit


def generate_jobs(num_jobs):
    jobs = []
    for i in range(1, num_jobs + 1):
        deadline = random.randint(1, num_jobs)
        profit = random.randint(1, 100)
        jobs.append((i, deadline, profit))
    return jobs

# # plots the execution time for the job sequencing for different cases
# # number of jobs taken as input
# def plot_job_sequencing(num_jobs):
#     # Generate jobs for different cases
#     best_case = generate_jobs(num_jobs)
#     worst_case = sorted(best_case, key=lambda x: x[2])
#     average_case = generate_jobs(num_jobs)

#     # Run job sequencing and measure execution time for each case
#     best_case_time = []
#     worst_case_time = []
#     average_case_time = []

#     for i in range(1, num_jobs + 1):
#         start_time = time.time()
#         job_sequencing(best_case[:i])
#         end_time = time.time()
#         best_case_time.append(end_time - start_time)

#         start_time = time.time()
#         job_sequencing(worst_case[:i])
#         end_time = time.time()
#         worst_case_time.append(end_time - start_time)

#         start_time = time.time()
#         job_sequencing(average_case[:i])
#         end_time = time.time()
#         average_case_time.append(end_time - start_time)

#     # Plot the results
#     x = list(range(1, num_jobs + 1))

#     plt.plot(x, best_case_time, label='Best Case')
#     plt.plot(x, worst_case_time, label='Worst Case')
#     plt.plot(x, average_case_time, label='Average Case')

#     plt.xlabel('Number of Jobs')
#     plt.ylabel('Execution Time (seconds)')
#     plt.title('Job Sequencing Execution Time')
#     plt.legend()
#     plt.show()


# # Specify the number of jobs for the plot
# num_jobs = 10

# # Plot the execution time for job sequencing
# plot_job_sequencing(num_jobs)

jobs = [(1, 6, 41), (2, 1, 60), (3, 5, 28), (4, 6, 31)]
print(job_sequencing(jobs))
