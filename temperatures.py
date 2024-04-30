''' In this exercise, you have to analyze records of temperature to find the
closest to zero. '''
temp = []
CLOSEST = 0
n = int(input())

for i in input().split():
    T = int(i)
    temp.append(T)

T = 0
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
        T = temp[i]

print(T)
