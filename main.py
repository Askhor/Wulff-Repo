import objects
from data import *

objects.ax = plt.figure().add_subplot(projection='3d')


def fcc():
    value_range = range(-3, 4)
    g = grid(value_range, value_range, value_range)
    g *= fcc_transform()
    lower = -2.5
    upper = 2.5
    g = g.filter(lambda p: all(lower <= t <= upper for t in p))
    g = auto_lines(g, 1)
    g.plot()


def fcc_wulff():
    wulff = fcc_wulff_obj()
    wulff.foreach(Point, setter('color', 'red'))
    wulff = convex_hull(wulff)
    wulff.foreach(Triangle, setter('color', 'darkred'))
    wulff.foreach(Triangle, setter('alpha', 0.7))
    wulff.plot()


def hcp():
    value_range = range(-2, 3)
    g = grid(value_range, value_range, value_range)
    g *= hcp_transform()
    g @= g + hcp_vector()
    lower = -1.5
    upper = 1.5
    g = g.filter(lambda p: all(lower <= t <= upper for t in p))
    g = auto_lines(g, 1)
    g.plot()


fcc()
fcc_wulff()

# plt.axis('off') # This line turns the axis off
objects.ax.set_aspect('equal')

plt.show()
