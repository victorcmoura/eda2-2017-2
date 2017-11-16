import random

class Task():
    def __init__(self, time_taken=0, due_to=0):
        self.time_taken = time_taken
        self.due_to = due_to

# Tasks are compatible if the start of one is equal or bigger than the other
def are_compatible(task_one, task_two):
    return task_one['end_time'] <= task_two['start_time']

# Minimizing lateness algorithm
def minimize_lateness(tasks):
    # Sort tasks by deadline
    sorted_tasks = sorted(tasks, key=lambda x: x['due_to'])

    total_time_taken = 0

    assigned_jobs = []

    # Simply append sorted tasks to assigned_jobs
    for task in sorted_tasks:
        assigned_jobs.append({
            'task': task,
            'start_time': total_time_taken,
            'end_time': total_time_taken + task['time_taken']
            })

        # Updates total time taken to complete the jobs
        total_time_taken = total_time_taken + task['time_taken']


    return {'assigned_jobs': assigned_jobs, 'total_time_taken': total_time_taken}


# Prints task dictionary in form of list
def print_tasks(tasks):
    for task in tasks:
        print('Time taken:', task['time_taken'], 'Due to:', task['due_to'])

# Prints schedule
def print_scheduled_tasks(assigned_jobs):
    max_lateness = assigned_jobs['assigned_jobs'][0]['end_time'] - assigned_jobs['assigned_jobs'][0]['task']['due_to']
    for task in assigned_jobs['assigned_jobs']:
        print(
        'Start time:',
        task['start_time'],
        'End time:',
        task['end_time'],
        'Due to:',
        task['task']['due_to'],
        'Lateness:',
        task['end_time'] - task['task']['due_to'] if task['end_time'] - task['task']['due_to'] > 0 else 0
        )

        # Update max_lateness
        if task['end_time'] - task['task']['due_to'] > max_lateness:
            max_lateness = task['end_time'] - task['task']['due_to']

    print('Max Lateness:', max_lateness if max_lateness > 0 else 0, 'Total time:', assigned_jobs['assigned_jobs'][-1]['end_time'])

# Create task list
tasks = []
number_of_tasks = int(input('How many tasks:'))

# Generate random tasks
for i in range(0, number_of_tasks*10, 10):
    random_int = random.randint(1, 10)

    new_task = Task(random_int, random.randint(1, i+10) + random_int)

    tasks.append(new_task.__dict__)

# Schedule tasks
scheduled_tasks = minimize_lateness(tasks)

# Print results
print('All tasks.', 'There are', len(tasks), 'tasks')
print_tasks(sorted(tasks, key=lambda x: x['due_to']))

print('='*50)

print('Selected tasks')
print_scheduled_tasks(scheduled_tasks)
