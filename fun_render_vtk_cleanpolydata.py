import vtk


def render_vtk_cleanpolydata(vtk_cleanpolydata):
    """
    References:
    - https://www.vtk.org/Wiki/VTK/Examples/Python/Filtering/CombinePolyData

    :param vtk_cleanpolydata:
    :return:
    """

    # Needed or not?
    #  Remove any duplicate points.

    # Create a mapper and actor
    #mapper = vtk.vtkPolyDataMapper()
    #if vtk.VTK_MAJOR_VERSION <= 5:
    #    mapper.SetInput(vtk_polydata)
    #else:
    #    mapper.SetInputData(vtk_polydata)

    # Create a mapper and actor
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(vtk_cleanpolydata.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Visualize
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(.5, .3, .31)  # Background color salmon

    renderWindow.Render()
    renderWindowInteractor.Start()
