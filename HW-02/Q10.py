import random
# Implementation of FCFS

# Generate a random sequence of disk requests.
def createSequences(num_requests,cylinders):
    return [random.randint(0, cylinders) for _ in range(num_requests)]


# Accept the initial head position as input.
initial_head_position = int(input("Enter initial head position: "))

total_cylinders = int(input("Enter total number of cylinders: "))
requests = int(input("Please enter # of requests: "))
disk_request = createSequences(num_requests=requests, cylinders=total_cylinders)

print(disk_request)

total_head_movement = 0
current_position = initial_head_position

for index in range(len(disk_request)):
    distance = abs(current_position - disk_request[index])
    print(f"Distance from {current_position} and {disk_request[index]}: {distance}")
    total_head_movement += distance
    current_position = disk_request[index]
print(f"Total Head Movement: {total_head_movement}")