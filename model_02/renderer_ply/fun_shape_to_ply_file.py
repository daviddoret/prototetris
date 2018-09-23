from model_02.renderer_ply.fun_shape_to_ply_text import *


def shape_to_ply_file(shape, file_path):
    """Export an arbtrary abstract shape and convert it to PLY and save everything in a file"""
    file = open(file_path, "w")
    ply_text = shape_to_ply_text(shape)
    file.write(ply_text)
    file.close()

