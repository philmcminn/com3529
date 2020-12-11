
def x_equals_y(x, y):
    if x == y:
        return 0
    else:
        return 1


def format_labels():
    labels = [""] * 10
    labels[1] = "-1000"
    labels[3] = "0"
    labels[5] = "1000"
    return labels

LANDSCAPE_FN = x_equals_y
AXES_MIN = -1200
AXES_MAX = 1200
AXES_STEP = 100
X_VAR = 'side2'
Y_VAR = 'side1'
COLOR_MAP = 'Oranges'
LABELS_FN = format_labels
OUT_FILE = 'rt-side1-equals-side2'
OUT_FORMAT = 'pdf'
SHOW = False
ELEVATION_ANGLE = 35
AZIMUTH_ANGLE = 25

######################

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rc, rcParams

rc('text', usetex=True)
rcParams['text.latex.preamble'] = [r'\usepackage{sfmath}']

def normalise(val):
    return 1 - pow(1.001, -(abs(val)))

def landscape(x_points, y_points, landscape_fn):
    z_points = [0] * len(x_points)
    for i in range(len(x_points)):
        z_points[i] = landscape_fn(x_points[i], y_points[i])
    return z_points

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
x_points = y_points = np.arange(AXES_MIN, AXES_MAX, AXES_STEP)
X, Y = np.meshgrid(x_points, y_points)
zs = np.array(landscape(np.ravel(X), np.ravel(Y), LANDSCAPE_FN))
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z, cmap=COLOR_MAP)

ax.xaxis.set_rotate_label(False)
ax.yaxis.set_rotate_label(False)
ax.zaxis.set_rotate_label(False)
ax.set_xlabel(r'{\tt ' + X_VAR + r'}', fontsize=12)
ax.set_ylabel(r'{\tt ' + Y_VAR + r'}', fontsize=12)
ax.set_zlabel("fitness", fontsize=12, rotation='vertical')

ax.set_xticklabels(LABELS_FN())
ax.set_yticklabels(LABELS_FN())

ax.view_init(ELEVATION_ANGLE, AZIMUTH_ANGLE)

if SHOW:
 plt.show()

plt.savefig(OUT_FILE + '.' + OUT_FORMAT, format=OUT_FORMAT, transparent=True)