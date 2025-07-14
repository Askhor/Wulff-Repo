## Visualisations of FCC and HCP

### main.py

Code to compose the different lattices and crystals using data from [data.py](#datapy) and the objects and methods from [objects.py](#objectspy) and [utils.py](#utilspy)

### data.py

The raw and slightly processed coordinates of Wulff-Crystals

### objects.py

The [Object](objects.py) class represents generic graphical 3d objects. Then there are the subclasses:
- Point
- Line
- Triangle
- ObjectCollection

### utils.py

Generic functions for manipulating and generating [Object](objects.py) instances and other useful functions