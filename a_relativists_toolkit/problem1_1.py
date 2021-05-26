import matplotlib.pyplot as plt
import numpy as np

def cone_mesh(x0, y0, z0, r, alpha):
    phi, r = np.meshgrid(np.linspace(0, 2*np.pi, 50),\
                      np.linspace(0, r, 50))
    x = r * np.sin(alpha) * np.cos(phi)
    y = r * np.sin(alpha) * np.sin(phi)
    z = r * np.cos(alpha)
    return x + x0, y + y0, z + z0


def main():
    fig = plt.figure()
    ax = plt.axes(projection="3d")


    x, y, z = cone_mesh(0, 0, 0, 1, np.pi/16)
    ax.set_box_aspect((np.ptp(x), np.ptp(y), np.ptp(z)))  # aspect ratio is 1:1:1 in data space
    ax.plot_surface(x, y, z)
    plt.show()


if __name__ == '__main__':
    main()
