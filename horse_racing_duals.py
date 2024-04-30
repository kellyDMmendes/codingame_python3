''' Casablanca’s hippodrome is organizing a new type of horse racing: duals.
During a dual, only two horses will participate in the race. In order for the
race to be interesting, it is necessary to try to select two horses with
similar strength.
Write a program which, using a given number of strengths, identifies the two
closest strengths and shows their difference with an integer (≥ 0). '''
d = float("inf")
n = int(input())

pi = list(range(n))
for i in range(n):
    pi[i] = int(input())
pi.sort()

for i in range(1, len(pi)):
    dif = pi[i] - pi[i - 1]
    if dif < d:
        d = dif

print(d)
