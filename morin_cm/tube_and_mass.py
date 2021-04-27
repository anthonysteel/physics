import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')
import numpy as np
import sympy as sym
import sympy.physics.mechanics as mech

l, m, M, g = sym.symbols('l, m, M, g', positive=True)
t = sym.symbols('t')

x = sym.Function('x')(t)
theta = sym.Function('theta')(t)

T = sym.Rational(1,2) * m * (x.diff(t)**2 + x**2 * theta.diff(t)**2) +\
    sym.Rational(1,2) * M * (l**2 * theta.diff(t)**2)

print(T)

V =
