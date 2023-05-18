import plotly.graph_objects as go
import timeit
import random


def generate_random_values():
    value = random.randint(1, 20)
    return value


def measure_execution_time(jobs):
    deadline = [0]*len(jobs.keys())
    i = 0
    for job in jobs:
        deadline[i] = jobs[job][1]
        i += 1

    size = max(deadline)
    schedule = [0]*size
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


input_sizes = []
execution_times = []

input_range = range(1, 1000)

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
fig.update_layout(title='Job Scheduling - Greedy Algorithm',
                  xaxis_title='Input Size', yaxis_title='Execution Time (s)')
fig.show()
