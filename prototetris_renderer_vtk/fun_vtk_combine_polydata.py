import vtk


def vtk_combine_polydata(*args):
    """
    References:
    - https://www.vtk.org/Wiki/VTK/Examples/Python/Filtering/CombinePolyData

    :param vtk_polydata_1:
    :param vtk_polydata_2:
    :return:
    """

    # Append the two meshes
    append_filter = vtk.vtkAppendPolyData()
    #if vtk.VTK_MAJOR_VERSION <= 5:
    #    append_filter.AddInputConnection(vtk_polydata_1.GetProducerPort())
    #    append_filter.AddInputConnection(vtk_polydata_2.GetProducerPort())
    #else:
    #    append_filter.AddInputData(vtk_polydata_1)
    #    append_filter.AddInputData(vtk_polydata_2)

    for arg in args:
        if isinstance(arg, vtk.vtkPolyData):
            append_filter.AddInputData(arg)
        if isinstance(arg, list):
            for i in arg:
                append_filter.AddInputData(i)

    append_filter.Update()

    clean_filter = vtk.vtkCleanPolyData()
    clean_filter.SetInputConnection(append_filter.GetOutputPort())
    clean_filter.Update()

    return clean_filter

