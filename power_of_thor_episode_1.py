''' Your program must allow Thor to reach the light of power. '''
DIRECTION = ""

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
thor_x = initial_tx
thor_y = initial_ty

while True:
    remaining_turns = int(input())

    if 0 <= thor_y < 18:
        if thor_y > light_y:
            DIRECTION += "N"
            thor_y -= 1
        elif thor_y < light_y:
            DIRECTION += "S"
            thor_y += 1

    if 0 <= thor_x < 40:
        if thor_x > light_x:
            DIRECTION += "W"
            thor_x -= 1
        elif thor_x < light_x:
            DIRECTION += "E"
            thor_x += 1

    print(DIRECTION)
    DIRECTION = ""
