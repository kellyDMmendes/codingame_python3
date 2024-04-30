''' You need to help the clones reach the exit in order to help them escape
the inside of the Improbability Drive. '''
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]

goal = []
goal.append([exit_floor] + [exit_pos])

for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    goal.append([elevator_floor] + [elevator_pos])
goal.sort()

while True:
    inputs = input().split()
    clone_floor = int(inputs[0])
    clone_pos = int(inputs[1])
    direction = inputs[2]

    if goal[clone_floor][1] < clone_pos and direction == "RIGHT":
        print("BLOCK")
    elif goal[clone_floor][1] > clone_pos and direction == "LEFT":
        print("BLOCK")
    else:
        print("WAIT")
