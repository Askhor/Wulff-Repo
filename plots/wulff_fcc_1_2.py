(fcc(range(-4, 5), lower_bound=-4, upper_bound=4, add_lines=False)
 .foreach(Point, setter('size', 2.5))
 .plot())

a = auto_lines(fcc_wulff(color='blue', corner_color='darkblue'), 1)
b = auto_lines(fcc_wulff2(), 2)
a.foreach(Line, setter('always_on_top', True))
c = a @ b
c.foreach(Triangle, setter('opacity', 0.2))

c.plot()