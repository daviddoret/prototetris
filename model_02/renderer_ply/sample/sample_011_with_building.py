from sympy import *
from model_02.renderer_ply.fun_custom_ply_data import custom_ply_data

from model_02 import *

f1 = Flat(position=Point3D(0, 0, 0))

f2 = Flat(position=Point3D(10, 0, 0))

l = list()
l.append(f1)
l.append(f2)

ply_text = custom_ply_data(l)

print(ply_text)

