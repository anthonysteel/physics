# http://www.physics.usu.edu/Wheeler/GenRel2013/Notes/Geodesics.pdf
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

def spherical_mesh(x0, y0, z0, radius):
    phi = np.linspace(0, np.pi, 25)
    theta = np.linspace(0, 2 * np.pi, 25)
    phi_mesh, theta_mesh = np.meshgrid(theta, phi)
    x = radius * np.sin(phi_mesh) * np.cos(theta_mesh)
    y = radius * np.sin(phi_mesh) * np.sin(theta_mesh)
    z = radius * np.cos(phi_mesh)
    return x + x0, y + y0, z + z0

def spherical2cartesian(theta, phi, r):
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)
    return x, y, z

def covariant_metric(theta, phi, r)
    return np.matrix(\
        [[  r**2,                         0],\
         [     0, r**2 * (np.sin(theta))**2]])

ax = plt.figure().add_subplot(projection='3d')

phi = np.linspace(0, np.pi/2, 50)
theta = 0
r = 1
x, y, z = spherical2cartesian(theta, phi, r)
ax.plot(x, y, z, color="r", linewidth=1)

theta = -np.pi/2
x, y, z = spherical2cartesian(theta, phi, r)
ax.plot(x, y, z, color="r", linewidth=1)

phi = np.pi/2
theta = np.linspace(-np.pi/2, 0, 50)
x, y, z = spherical2cartesian(theta, phi, r)
ax.plot(x, y, z, color="r", linewidth=1)

x, y, z = spherical_mesh(0, 0, 0, 1)
ax.plot_wireframe(x, y, z, alpha=0.4)


plt.show()
