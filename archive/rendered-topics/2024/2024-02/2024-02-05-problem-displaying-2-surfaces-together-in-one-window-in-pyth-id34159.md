# Problem displaying 2 surfaces together in one window, in Python way

**Topic ID**: 34159
**Date**: 2024-02-05
**URL**: https://discourse.slicer.org/t/problem-displaying-2-surfaces-together-in-one-window-in-python-way/34159

---

## Post #1 by @guozhi0302 (2024-02-05 22:26 UTC)

<p>The official tutorial <a href="http://www.vmtk.org/tutorials/Centerlines.html" rel="noopener nofollow ugc">Computing Centerlines</a> has demonstrated displaying multiple surfaces (or centerlines) in one window with Pype commands.</p>
<pre><code class="lang-auto">vmtksurfacereader -ifile foo.vtp --pipe vmtkcenterlines --pipe vmtkrenderer --pipe vmtksurfaceviewer -opacity 0.25 --pipe vmtksurfaceviewer -i @vmtkcenterlines.o -array MaximumInscribedSphereRadius
</code></pre>
<p>However, the way the piping works has confused me. It seems that the last vmtkSurfaceViewer not only receive a surface (foo.vtp) from its previous vmtkSurfaceViewer, but also the centerline as a second input.<br>
Is there any way to do the same thing in Python’s object-oriented manner?</p>

---

## Post #3 by @guozhi0302 (2024-02-07 13:53 UTC)

<p>To answer my own question,<br>
After reading vmtkSurfaceViewer()'s source code, I still feel its piping too complicated to understand.<br>
However, I use VTK’s functions instead to combine polydata (surfaces and centerlines) first. The combined data is then fed into vmtkRenderer(). VTK’s own Renderer is also available, but I prefer VMTK’s.<br>
The following is my code. Part of it referenced <a href="https://discourse.vtk.org/t/how-to-change-the-colors-of-objects-in-vtk-when-using-vtkappendpolydata/2431" rel="noopener nofollow ugc">this post</a>. It allows setting color and opacity for each polydata. Readers are vmtkSurfaceReader()s.</p>
<pre><code class="lang-auto">class PolydataViewer():
    def __init__(self):
        self.appendFilter = vtk.vtkAppendPolyData()

    def add_polydata(self, polydata, color=[255, 255, 255], opacity=1):
        colors = vtk.vtkUnsignedCharArray()
        colors.SetNumberOfComponents(4)
        colors.SetName("DisplayColor")
        colors.SetNumberOfTuples(polydata.GetNumberOfCells())
        for c in range(polydata.GetNumberOfCells()):
            colors.SetTuple(c, (*color, int(opacity * 255)))
        polydata.GetCellData().AddArray(colors)
        self.appendFilter.AddInputData(polydata)

    def show(self, background=None):
        self.appendFilter.Update()
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(self.appendFilter.GetOutputPort())
        mapper.SetScalarModeToUseCellFieldData()
        mapper.SelectColorArray('DisplayColor')
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        renderer = vmtk.vmtkrenderer.vmtkRenderer()
        renderer.Initialize()
        if background is not None:
            renderer.Renderer.SetBackground(np.array(background) / 255)
        renderer.Renderer.AddActor(actor)
        renderer.Render()
        renderer.Deallocate()

viewer = PolydataViewer()
viewer.add_polydata(reader1.Surface, color=[255, 0, 0], opacity=0.3)
viewer.add_polydata(reader2.Surface, color=[255, 255, 0])
viewer.show()
</code></pre>

---
