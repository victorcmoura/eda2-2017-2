import random

class Task():
    def __init__(self, start_time=0, end_time=0):
        self.start_time = start_time
        self.end_time = end_time

# Tasks are compatible if the start of one is equal or bigger than the other
def are_compatible(task_one, task_two):
    return task_one['end_time'] <= task_two['start_time']

# Interval scheduling algorithm
def make_schedule(tasks):
    # Sort tasks by end_time
    sorted_tasks = sorted(tasks, key=lambda x: x['end_time'])

    # Select first task
    taken_tasks = [sorted_tasks[0]]
    sorted_tasks.remove(sorted_tasks[0])

    for task in sorted_tasks:
        if are_compatible(taken_tasks[-1], task):
            taken_tasks.append(task)

    taken_tasks = sorted(taken_tasks, key=lambda x: x['start_time'])

    return taken_tasks

# Prints task dictionary in form of list
def print_tasks(tasks):
    for task in tasks:
        print('Start time:', task['start_time'], 'End time:', task['end_time'])




# Create task list
tasks = []

# Generate random tasks
for i in range(0, 100, 10):
    new_task = Task(i, random.randint(1, 15) + i)

    tasks.append(new_task.__dict__)

# Schedule tasks
taken_tasks = make_schedule(tasks)

# Print results
print('All tasks')
print_tasks(sorted(tasks, key=lambda x: x['start_time']))
print()
print('Selected tasks')
print_tasks(taken_tasks)
