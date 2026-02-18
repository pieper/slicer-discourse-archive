# How to color a stl file using VTK in python

**Topic ID**: 26334
**Date**: 2022-11-20
**URL**: https://discourse.slicer.org/t/how-to-color-a-stl-file-using-vtk-in-python/26334

---

## Post #1 by @Hamid_Fsian (2022-11-20 20:21 UTC)

<p>Hello,</p>
<p>I am a newbie in VTK.</p>
<p>I have generated a STL file (of bones) using VTK, and now I want to have specific color labels for each slice, for example :</p>
<ul>
<li>
<p>if the width of slice(n) &gt; N (number) =&gt; green,</p>
</li>
<li>
<p>if width of slice(n) &lt; M =&gt; red,</p>
</li>
<li>
<p>if width of M&lt;slice(n)&lt;N =&gt; orange.</p>
</li>
</ul>
<p>Is there’s a way to do it ?</p>

---

## Post #2 by @lassoan (2022-12-01 06:40 UTC)

<p>STL files cannot store color. You can use “Plane cut” tool in “Dynamic modeler” module to cut up a model with slice planes.</p>
<p>What is your overall goal?</p>

---

## Post #3 by @Hamid_Fsian (2022-12-01 07:59 UTC)

<p>Thank’s for your answer.</p>
<p>I want to parse my 3D object by slices, and check for each point “x” if the width is superior to a certain treshold, if so =&gt; Color the corresponding slice “GREEN”. Else, color it “RED”.</p>
<p>What follow is my code. But I am coloring the x-axis and not the z-axis.</p>
<pre><code class="lang-python">import vtk, sys
import statistics
# Read in your STL file
f = vtk.vtkSTLReader()
f.SetFileName("airways_no_labels.stl")
f.Update() # This is necessary to have the data ready to read.

# The vtkSTLReader reads in your file as a vtkPolyData, 'obj' is a reference to
# that output. I'm using the bounds that are automatically calculated during
# the import phase to give a range for the height of the points in the file.v
# I believe that the bounds are (xmin, xmax, ymin, ymax, zmin, zmax).
obj = f.GetOutputDataObject(0)
min_x , max_x , min_y , max_y ,min_z, max_z = obj.GetBounds()

lut = vtk.vtkLookupTable()
lut.SetTableRange(min_z, max_z)
lut.Build()

heights = vtk.vtkDoubleArray()
heights.SetName("Z_Value")

Colors = vtk.vtkUnsignedCharArray()
Colors.SetNumberOfComponents(3)
Colors.SetNumberOfTuples(obj.GetNumberOfCells())

for i in range(obj.GetNumberOfPoints()):
    z = obj.GetPoint(i)[-1] # z axis
    x = obj.GetPoint(i)[0] # x axis

# This is just a try but won't work
    if min_x &lt; x &lt; max_x: 
        Colors.InsertVariantValue(255,z)
    if min_x &lt; x &lt; 300 :
        Colors.InsertVariantValue(155,z)
    if 300 &lt; x &lt; max_x :
        heights.InsertVariantValue(0,z)
#end of the "TRY"

    # Add this array to the point data as a scalar.
obj.GetPointData().SetScalars(Colors)


mapper = vtk.vtkPolyDataMapper()
mapper.SetInputDataObject(obj)
mapper.SetScalarRange(min_z, max_z)
mapper.SetLookupTable(lut)
mapper.SetUseLookupTableScalarRange(True)

actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(.1, .2, .4)

renw = vtk.vtkRenderWindow()
renw.AddRenderer(renderer)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renw)

renw.Render()
iren.Start()

#Then save it as .vtk file
</code></pre>

---

## Post #4 by @Jeevigyay_Srivastava (2023-01-20 05:28 UTC)

<p>Hello Sir,<br>
I am facing an issue. If you are comfortable with mitk I can proceed with my question.</p>

---
