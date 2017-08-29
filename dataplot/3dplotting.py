import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def drawing3dt():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    z = np.linspace(-2, 2, 100)
    r = z**2 + 1
    x = r * 1
    y = r * 2
    ax.plot(x, y, z, label = 'testsample')
    ax.legend()
    plt.show()
