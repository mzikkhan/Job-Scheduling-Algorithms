import matplotlib.pyplot as plt
import random

# To generate random value for input


def generate_random_values():
    value = random.randint(1, 20)
    return value


def job_sequencing_performance(jobs):
    deadline = [0] * len(jobs.keys())
    i = 0
    for job in jobs:
        deadline[i] = jobs[job][1]
        i += 1

    size = max(deadline)

    schedule = [0] * size
    max_profit = 0

    jobs = dict(sorted(jobs.items(), key=lambda x: x[1], reverse=True))

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

    return max_profit


def analyze_performance():

    input_sizes = []
    best_case_times = []
    worst_case_times = []
    average_case_times = []

    # Declaring input range
    input_range = range(1, 1000)

    # Create input array of jobs
    for size in input_range:
        jobs = {f'j{i+1}': [generate_random_values(), generate_random_values()]
                for i in range(size)}

        input_sizes.append(size)

        best_case_time = float('inf')
        worst_case_time = float('-inf')
        average_case_time = 0

        result = job_sequencing_performance(jobs)
        best_case_time = min(best_case_time, result)
        worst_case_time = max(worst_case_time, result)
        average_case_time += result

        average_case_time /= size

        best_case_times.append(best_case_time)
        worst_case_times.append(worst_case_time)
        average_case_times.append(average_case_time)

    plt.plot(input_sizes, best_case_times, label='Best Case')
    plt.plot(input_sizes, worst_case_times, label='Worst Case')
    plt.plot(input_sizes, average_case_times, label='Average Case')

    plt.xlabel('Input Size')
    plt.ylabel('Running Time')

    plt.title('Job Scheduling - Greedy')

    plt.legend()
    plt.show()


if __name__ == "__main__":

    analyze_performance()
