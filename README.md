# Visualisations of FCC and HCP

These visualisations are created with matplotlib which handles 3d rather simplistically and hence there are sometimes issues with clipping.

## Examples

#### Wulff crystal with side-length 1 in FCC
![Wulff crystal with side-length 1 in FCC](examples/FCC_Wulff1.png)
This was plotted with
```python
(auto_lines(fcc_wulff(opacity=0.2), 1)
 .foreach(Line, setter('always_on_top', True))
 .plot())
```

#### FCC Lattice
![FCC Lattice](examples/FCC.png)
This was plotted with
```python
fcc(upper_bound=2.5, upper_clip_plane=5.5).plot()
```

#### Wulff crystal with side-length 1 in FCC and FCC Lattice
![Wulff crystal with side-length 1 in FCC and FCC Lattice](examples/FCC_and_FCC_Wulff1.png)
This was plotted with
```python
fcc(upper_bound=2.5, upper_clip_plane=5.5).plot()
fcc_wulff(opacity=0.5).plot()
```

#### Wulff crystals with side-lengths 1 and 2 in FCC
![Wulff crystals with side-lengths 1 and 2 in FCC](examples/FCC_Wulff1_Wulff2.png)
This was plotted with
```python
a = auto_lines(fcc_wulff(color='blue', corner_color='darkblue'), 1)
b = auto_lines(fcc_wulff2(), 2)
c = a @ b
c.foreach(Triangle, setter('opacity', 0.2))

c.plot()
```

## The code

### main.py

Code to compose the different lattices and crystals using data from [data.py](#datapy) and the objects and methods from [objects.py](#objectspy) and [utils.py](#utilspy)

### data.py

The raw and slightly processed coordinates of Wulff-Crystals

### objects.py

The [Object](objects.py#L9) class represents generic graphical 3d objects. Then there are the subclasses:
- Point
- Line
- Triangle
- ObjectCollection

### utils.py

Generic functions for manipulating and generating [Object](objects.py#L9) instances and other useful functions