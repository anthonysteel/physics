from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def Generate2Sphere():
  phi = np.linspace(0, np.pi, 20)
  theta = np.linspace(0, 2 * np.pi, 40)
  x = np.outer(np.sin(theta), np.cos(phi))
  y = np.outer(np.sin(theta), np.sin(phi))
  z = np.outer(np.cos(theta), np.ones_like(phi))
  return [x, y, z]

def PlotHemispheres(xyz, ax):
  for i in range(0, 2):
    for j in range(0, 3):
      X = np.stack((xyz[0].flatten(),xyz[1].flatten(),xyz[2].flatten()))
      mask = X[j] < 0 if i == 0 else X[j] > 0
      x_neg, y_neg, z_neg = X.T[mask].T
      sign = str("-" if i == 0 else "+")
      label = r'$O^'+sign+'_'+str(j+1)+'$'
      ax[i][j].plot(x_neg, y_neg, z_neg, color='b', label=label)
def PlotProjectionMaps(xyz, ax):
  for i in range(0,2):
    for j in range(0,3):
      ax[i,j].plot_wireframe(xyz[0], xyz[1], xyz[2],\
                             color='k', rstride=1, cstride=1,
                             label=r'$S^2$')
      sign = str("-" if i == 0 else "+")
      label = r'$f^'+sign+'_'+str(j+1)+'$'
      if j == 0:
        ax[i,j].plot_wireframe((-1 if i == 0 else 1)*np.ones(xyz[0].shape),\
                                xyz[1],\
                                xyz[2],\
                                color='r', rstride=1, cstride=1,\
                                label=label)
      elif j == 1:
        ax[i,j].plot_wireframe(xyz[0],\
                               (-1 if i == 0 else 1)*np.ones(xyz[0].shape),\
                               xyz[2],\
                               color='r', rstride=1, cstride=1,
                               label=label)
      elif j == 2:
        ax[i,j].plot_wireframe(xyz[0],\
                               xyz[1],\
                               (-1 if i == 0 else 1)*np.ones(xyz[0].shape),\
                               color='r', rstride=1, cstride=1,
                               label=label)
      ax[i,j].legend()

def main():
  fig, ax = plt.subplots(2, 3, subplot_kw={'projection':'3d', 'aspect':'equal'})
  x, y, z = Generate2Sphere()
  xyz = [x,y,z]
  PlotHemispheres(xyz, ax)
  PlotProjectionMaps(xyz, ax)
  plt.show()

if __name__ == "__main__":
  main()
