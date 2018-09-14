

"""

REFERENCES

How to write python classes
https://docs.python.org/3/tutorial/classes.html

Python code style guidelines
https://www.python.org/dev/peps/pep-0008/

GETTING STARTED

Please install Anaconda
https://www.anaconda.com/download/

it includes SimPy
https://docs.sympy.org/latest/index.html

and SimPy has nice geometric class such as Polygon
https://docs.sympy.org/latest/modules/geometry/polygons.html#sympy.geometry.polygon.Polygon

ooops, Anaconda can't be used directly because Rhino requires IronPython.
So first, install IronPython and use it as the interpreter
we will then need to install all Anaconda desired libraries on top of that
http://ironpython.net/

ooops, this will downgrade us to 2.7

ooops, this will force us to move to visual studio


CURRENTLY INSTALLING VISUAL STUDIO

THen, in VSS market place we have Rhino components
https://marketplace.visualstudio.com/items?itemName=McNeel.RhinoCommontemplatesforv6
https://marketplace.visualstudio.com/items?itemName=McNeel.GrasshopperAssemblyforv6

ALTERNATIVE SOLUTION TO RHINO (and open source)
https://www.blender.org/thanks/
WITH PYTHON API:
https://docs.blender.org/api/current/
Advantage: uses Python 3

how to autocomplete blender from pycharm
https://blender.community/c/today/Gfcbbc/


WISH

implement a clean math model in Python, without too strong dependency on Rhino and/or Blender
this will help us yield all benefits from Anaconda etc
then ensure we can easily export the result for visualization
ideally become 3d format agnostic

CONSIDER

http://www.open3d.org/


PYCOLLADA

a possible option to export results in 3d format
https://media.readthedocs.org/pdf/pycollada/latest/pycollada.pdf


"""
