import objects
from data import *

objects.ax = plt.figure().add_subplot(projection='3d')


def fcc():
    """
    Generates a subset of fcc
    """
    value_range = range(-3, 4)
    g = grid(value_range, value_range, value_range)
    g *= fcc_transform()
    lower = -2.5
    upper = 2.5
    g = g.filter(lambda p: all(lower <= t <= upper for t in p))
    g = auto_lines(g, 1)
    return g


def fcc_wulff():
    """
    Generates the polygon that is the wulff crystal (with side length 1)
    """
    wulff = fcc_wulff_obj()
    wulff += (-1 * pos(1, 2, 1))  # center the crystal (somewhat)
    wulff.foreach(Point, setter('color', 'red'))
    wulff = convex_hull(wulff)
    wulff.foreach(Triangle, setter('color', 'darkred'))
    wulff.foreach(Triangle, setter('alpha', 0.7))
    return wulff


def fcc_wulff2():
    """
    Generates the polygon that is the wulff crystal (with side length 2)
    """
    wulff = fcc_wulff2_obj()
    wulff.foreach(Point, setter('color', 'red'))
    wulff = convex_hull(wulff)
    wulff.foreach(Triangle, setter('color', 'darkred'))
    wulff.foreach(Triangle, setter('alpha', 0.7))


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

##############################################################################
# Plot stuff here like this
# fcc().plot()



##############################################################################

# plt.axis('off') # This line turns the axis off
objects.ax.set_aspect('equal')

plt.show()
