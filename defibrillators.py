''' The city of Montpellier has equipped its streets with defibrillators to
help save victims of cardiac arrests. The data corresponding to the position
of all defibrillators is available online.
Based on the data we provide in the tests, write a program that will allow
users to find the defibrillator nearest to their location using their mobile
phone. '''
from math import sqrt
from math import cos

number = []
local = []
address = []
local_lon = []
local_lat = []
CLOSEST = 0
MIN_D = 0

lon = input()
lon = float(lon.replace(",", "."))
lat = input()
lat = float(lat.replace(",", "."))
n = int(input())

for i in range(n):
    number, local, address, space, local_lon, local_lat = input().split(";")
    local_lon = float(local_lon.replace(",", "."))
    local_lat = float(local_lat.replace(",", "."))

    x = (local_lon - lon) * cos((lat + local_lat) / 2)
    y = local_lat - lat
    d = sqrt(x**2 + y**2) * 6371

    if d < MIN_D or i == 0:
        MIN_D = d
        CLOSEST = local

print(CLOSEST)
