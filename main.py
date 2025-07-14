import matplotlib

import objects
from data import *

###############################################################################
# Some very technical configuration
matplotlib.rcParams["savefig.directory"] = "./examples"
objects.ax = plt.figure().add_subplot(projection='3d')
###############################################################################
# The definitions of the fcc, hcp, etc. methods

def fcc(grid_range=range(0, 4), lower_bound=0, upper_bound=1.9, upper_clip_plane=math.inf):
    """
    Generates a subset of fcc
    :grid_range: The range for the grid which will be range(-3,4) × range(-3,4) × range(-3, 4)
    """
    g = grid(grid_range, grid_range, grid_range)
    g *= fcc_transform()
    g = g.filter(lambda p: all(lower_bound <= t <= upper_bound for t in p))
    g = g.filter(lambda p: sum(p[i] for i in range(3)) <= upper_clip_plane)
    g = auto_lines(g, 1)
    return g


def fcc_wulff(opacity=1, corner_color='red', color='darkred'):
    """
    Generates the polygon that is the wulff crystal (with side length 1)
    """
    wulff = fcc_wulff_obj()
    # wulff += pos(0,0,0)  # center the crystal (somewhat)
    wulff.foreach(Point, setter('color', corner_color))
    wulff = convex_hull(wulff)
    wulff.foreach(Triangle, setter('color', color))
    wulff.foreach(Triangle, setter('alpha', opacity))
    return wulff


def fcc_wulff2(opacity=1, corner_color='red', color='darkred'):
    """
    Generates the polygon that is the wulff crystal (with side length 2)
    """
    wulff = fcc_wulff2_obj()
    wulff.foreach(Point, setter('color', corner_color))
    wulff = convex_hull(wulff)
    wulff.foreach(Triangle, setter('color', color))
    wulff.foreach(Triangle, setter('alpha', opacity))
    return wulff


def hcp():
    """
    Generates a subset of hcp
    """
    value_range = range(-2, 3)
    g = grid(value_range, value_range, value_range)
    g *= hcp_transform()
    g @= g + hcp_vector()
    lower = -1.5
    upper = 1.5
    g = g.filter(lambda p: all(lower <= t <= upper for t in p))
    g = auto_lines(g, 1)
    return g


def print_point_set(s):
    """
    Given a set s consisting of Point instances, prints their positions
    """
    print(*map(lambda p: p.pos, s))

###############################################################################
###############################################################################
# Here you can plot stuff like this:
# fcc().plot()

###############################################################################
###############################################################################
# Here is some configuration
# Set initial elevation, azimuth and roll here
elevation = 30
azimuth = 60
roll = 0
# Good values for FCC Wulff
# elevation =  64.4
# azimuth = -152.8
# roll = 112.18333534218363
# Good values for FCC
# elevation = -28.4
# azimuth =   9.1
# roll = -27.6
# plt.axis('off')  # This line turns the axis off

###############################################################################
# plot origin
# origin = Point(pos(0,0,0))
# origin.color = 'green'
# origin.plot()

###############################################################################

objects.ax.set_aspect('equal')

objects.ax.view_init(elev=elevation, azim=azimuth, roll=roll)
plt.show()
print(
    f"Final azimuth and elevation:\nelevation = {objects.ax.elev:5.1f}\nazimuth = {objects.ax.azim:5.1f}\nroll = {objects.ax.roll:5.1f}")
