# from itertools import permutations

# def job_sequencing(jobs):
#     max_deadline = max(jobs, key=lambda x: x[1])[1]
#     job_permutations = list(permutations(jobs))
#     max_profit = 0
#     best_schedule = []
#     for permutation in job_permutations:
#         schedule = []
#         profit = 0
#         for job in permutation:
#             if job[1] <= max_deadline - len(schedule):
#                 schedule.append(job[0])
#                 profit += job[2]
#         if profit > max_profit:
#             max_profit = profit
#             best_schedule = schedule
#     return best_schedule, max_profit



jobs = [ 'j1', 'j2', 'j3', 'j4']
profit =[ 50, 15, 10, 25]
deadline = [ 2, 1, 2, 1]

size = max(deadline)
schedule = [0]*size

