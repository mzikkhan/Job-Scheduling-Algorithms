import plotly.graph_objects as go
import timeit
import random

# To generate random value for input


def generate_random_values():
    value = random.randint(1, 20)
    return value


# Greedy Algorithm to calculate profit


def job_schedulig_greedy(jobs):
    # Store deadlines in an array and find max deadline
    deadline = [0]*len(jobs.keys())
    i = 0
    for job in jobs:
        deadline[i] = jobs[job][1]
        i += 1

    # Initialize size of our schedule to max value of deadline
    size = max(deadline)
    schedule = [0]*size
    max_profit = 0

    # Sort jobs in order of decreasing profit
    jobs = dict(sorted(jobs.items(), key=lambda x: x[1], reverse=True))

    # Iterate over each job
    for job in jobs:
        # Check if schedule is full
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


if __name__ == "__main__":
    input_sizes = []
    execution_times = []

    # Declaring input range
    input_range = range(1, 1000)

    # Create input array of jobs
    for size in input_range:
        jobs = {f'j{i+1}': [generate_random_values(), generate_random_values()]
                for i in range(size)}

        # Start timer
        start_time = timeit.default_timer()
        # Run greedy algorithm
        max_profit = job_schedulig_greedy(jobs)
        # End timer
        end_time = timeit.default_timer()
        # Calculate execution time
        execution_time = end_time - start_time

        input_sizes.append(size)
        execution_times.append(execution_time)

    # Plot our graphs
    fig = go.Figure(data=go.Scatter(
        x=input_sizes, y=execution_times, mode='lines'))
    fig.update_layout(title='Job Scheduling - Greedy Algorithm',
                      xaxis_title='Input Size', yaxis_title='Execution Time (s)')
    fig.show()
