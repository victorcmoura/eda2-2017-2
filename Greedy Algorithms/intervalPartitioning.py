import random

class Task():
    def __init__(self, start_time=0, end_time=0):
        self.start_time = start_time
        self.end_time = end_time

# Tasks are compatible if the start of one is equal or bigger than the other
def are_compatible(task_one, task_two):
    return task_one['end_time'] <= task_two['start_time']

# Interval partitioning algorithm
def make_partitioning(tasks):
    # Sort tasks by start_time
    sorted_tasks = sorted(tasks, key=lambda x: x['start_time'])

    slots = [[]]

    # Append first task
    slots[0].append(sorted_tasks[0])
    sorted_tasks.remove(sorted_tasks[0])

    for task in sorted_tasks:
        task_not_inserted = True
        for slot in slots:
            # If task is compatible with a slot, append
            if are_compatible(slot[-1], task):
                slot.append(task)
                task_not_inserted = False
                break

        # If task is not compatible with any slot, create new one
        if task_not_inserted:
            slots.append([task])


    return slots


# Prints task dictionary in form of list
def print_tasks(tasks):
    for task in tasks:
        print('Start time:', task['start_time'], 'End time:', task['end_time'])




# Create task list
tasks = []
number_of_tasks = int(input('How many tasks:'))

# Generate random tasks
for i in range(0, number_of_tasks*10, 10):
    new_task = Task(i, random.randint(1, 30) + i)

    tasks.append(new_task.__dict__)

# Schedule tasks
slots = make_partitioning(tasks)

# Print results
print('All tasks.', 'There are', len(tasks), 'tasks')
print_tasks(sorted(tasks, key=lambda x: x['start_time']))

print('='*50)

print('Selected tasks')
slot_number = 1
for tasks in slots:
    print('Slot:', slot_number, 'Slot size:', len(tasks))
    slot_number = slot_number + 1
    print_tasks(tasks)
