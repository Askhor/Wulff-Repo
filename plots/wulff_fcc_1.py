(fcc(range(-4, 5), lower_bound=-4, upper_bound=4, add_lines=False)
 .foreach(Point, setter('size', 2.5))
 .plot())

a = auto_lines(fcc_wulff(color='blue', corner_color='darkblue'), 1)
a.foreach(Line, setter('always_on_top', True))
a.foreach(Triangle, setter('opacity', 0.2))
a.plot()