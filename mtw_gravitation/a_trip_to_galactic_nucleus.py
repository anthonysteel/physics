import numpy
import math
g = 9.8 # m/s^2
c = 299792458 # m/s
year = 31556952 # s
lightyear = c * year

galactic_center = (30*10**4) * lightyear

print(galactic_center)

def tau(x):
    return (c / g) * numpy.arccosh(g * x / c**2)

proper_time = 2 * tau(galactic_center/2)

print("Trip to galactic center:", proper_time/year)

def fuel(proper_time):
    return math.exp(-g*proper_time/c)

print(2*fuel(proper_time/2))
