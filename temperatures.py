''' In this exercise, you have to analyze records of temperature to find the
closest to zero. '''
temp = []
CLOSEST = 0
n = int(input())

for i in input().split():
    t = int(i)
    temp.append(t)

t = 0
if not temp:
    temp.append(0)
else:
    temp.sort()

for i in range(n):
    if temp[i] < 0:
        close = -(temp[i])
    else:
        close = temp[i]
    if close <= CLOSEST or CLOSEST == 0:
        CLOSEST = close
        t = temp[i]

print(t)
