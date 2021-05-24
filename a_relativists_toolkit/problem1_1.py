import matplotlib.pyplot as plt
import numpy as np

def sphere_mesh(x0, y0, z0, r):
    theta, phi = np.meshgrid(np.linspace(0, 2*np.pi, 50),\
                              np.linspace(0, np.pi, 50))      
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)
    return x + x0, y + y0, z + z0


def main():
    fig = plt.figure()
    ax = plt.axes(projection="3d")

    x, y, z = sphere_mesh(0, 0, 0, 1)
    ax.plot_surface(x, y, z)
    plt.show()


if __name__ == '__main__':
    main()
