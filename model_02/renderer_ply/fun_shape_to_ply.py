import model_02


def shape_to_ply(shape):
    """
    Takes a list of prisms and merge them together into a PLY file.

    References:
     - https://github.com/dranjan/python-plyfile
    """

    # Export the Point3D list and polygon "by index" list
    data_structure = shape.get_flattened_point3d_list_with_polygon_by_index_list()

    ply_point_text = ""
    ply_polygon_text = ""

    for prism_point in data_structure["point3d_list"]:
        ply_line = "\n{} {} {} {} {} {}".format(prism_point.x, prism_point.y, prism_point.z, 255, 255, 255)
        # prism.surface_color.red, prism.surface_color.green, prism.surface_color.blue)
        ply_point_text = ply_point_text + ply_line

    for prism_polygon in data_structure["polygon_by_index_list"]:
        ply_line = "\n{}".format(len(prism_polygon))  # The first number in PLY is the number of vertices in the polygon
        for prism_polygon_point_index in prism_polygon:
            ply_line = "{} {}".format(ply_line, prism_polygon_point_index)
        ply_polygon_text = ply_polygon_text + ply_line

    ply_header = """ply
format ascii 1.0
element vertex {}
property float x
property float y
property float z
property uchar red
property uchar green
property uchar blue
element face {}
property list uchar int vertex_indices
property uchar red
property uchar green
property uchar blue
end_header""".format(len(data_structure["point3d_list"]), len(data_structure["polygon_by_index_list"]))

    return ply_header + ply_point_text + ply_polygon_text
