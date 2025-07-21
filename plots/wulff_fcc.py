wulff = auto_lines(fcc_wulff(), 1)
wulff = ObjectCollection([ o for o in wulff.objs if isinstance(o, Line)])
wulff.plot()