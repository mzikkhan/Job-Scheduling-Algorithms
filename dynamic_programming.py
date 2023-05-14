# def job_sequence_dp(profits, deadlines, max_deadline):
#     # Sort the jobs by profit in descending order
#     jobs = sorted(range(len(profits)), key=lambda i: profits[i], reverse=True)

#     # Initialize the memo table
#     memo = [[0] * (max_deadline + 1) for _ in range(len(jobs) + 1)]

#     # Fill the memo table using dynamic programming
#     for i in range(1, len(jobs) + 1):
#         for j in range(1, max_deadline + 1):
#             if j >= deadlines[jobs[i - 1]]:
#                 memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - deadlines[jobs[i - 1]]] + profits[jobs[i - 1]])
#             else:
#                 memo[i][j] = memo[i - 1][j]

#     # Determine the job sequence
#     sequence = []
#     i = len(jobs)
#     j = max_deadline
#     while i > 0 and j > 0:
#         if memo[i][j] != memo[i - 1][j]:
#             sequence.append(jobs[i - 1])
#             j -= deadlines[jobs[i - 1]]
#         i -= 1

#     # Reverse the job sequence to get the correct order
#     sequence = sequence[::-1]

#     return sequence

