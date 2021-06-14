import matplotlib.pyplot as plt
import numpy as np

def cone_mesh(x0, y0, z0, r, alpha):
    phi, r = np.meshgrid(np.linspace(0, 2*np.pi, 50),\
                      np.linspace(0, r, 50))
    x = r * np.sin(alpha) * np.cos(phi)
    y = r * np.sin(alpha) * np.sin(phi)
    z = r * np.cos(alpha)
    return x + x0, y + y0, z + z0

def cone_mesh_2(x0, y0, z0, phi, r, alpha):
    phi, r = np.meshgrid((1/np.sin(alpha))* np.arctan(np.linspace(-1000, 1000, 50)),\
                      np.linspace(0, r, 50))
    x = r * np.sin(alpha) * np.cos(phi)
    y = r * np.sin(alpha) * np.sin(phi)
    z = r * np.cos(alpha)
    return x + x0, y + y0, z + z0

def phi(x, y, alpha):
    return (1/np.sin(alpha))* np.arctan(y/x)

def r_i(x, y):
    return np.sqrt(x**2 + y**2)


def main():
    fig = plt.figure()
    ax = plt.axes(projection="3d")


    alpha = np.pi/8
    r = 1
    x, y, z = cone_mesh(0, 0, 0, r, alpha)
    ax.set_box_aspect((np.ptp(x), np.ptp(y), np.ptp(z)))  # aspect ratio is 1:1:1 in data space
    #ax.plot_surface(x, y, z)

    x = np.linspace(0, 1, 50)
    y = np.linspace(0, 1, 50)

    phi_arr = phi(x, y, alpha)
    r_arr = r_i(x, y)

    x, y, z = cone_mesh_2(0, 0, 0, phi_arr, 1, alpha)
    ax.plot_surface(x, y, z)

    plt.show()


if __name__ == '__main__':
    main()
