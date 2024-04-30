''' Destroy the mountains before your starship collides with one of them. For
that, shoot the highest mountain on your path. '''
mountain_h = list(range(8))
MOUNTAIN_MAX = 0
CONT = 0

while True:
    for i in range(8):
        mountain_h[i] = int(input())
        if mountain_h[i] > MOUNTAIN_MAX:
            MOUNTAIN_MAX = max(MOUNTAIN_MAX, mountain_h[i])
            CONT = i

    print(CONT)
    mountain_h[CONT] = 0
    MOUNTAIN_MAX = 0
