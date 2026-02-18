# Is there a way to add a vector for the fiducials?

**Topic ID**: 20574
**Date**: 2021-11-11
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-add-a-vector-for-the-fiducials/20574

---

## Post #1 by @Saima (2021-11-11 03:17 UTC)

<p>Hi,<br>
Is there a way to add a vector for the fiducial.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #2 by @lassoan (2021-11-11 04:28 UTC)

<p>Each fiducial point has a position and orientation. If the vector defines an orientation then that would be a convenient place to store it. If the vector stores an RGB value or any other signal or other property then you can add store it in the markups fiducials as a static measurement. This is used for example for storing curvatures in curves.</p>
<p>Example for storing a 4-component vector for each control point:</p>
<pre><code class="lang-python">pointListNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode')

myVector = vtk.vtkDoubleArray()
myVector.SetName('SomeVector')
myVector.SetNumberOfComponents(4)

pointListNode.AddControlPointWorld(vtk.vtkVector3d(40, 50, -10.2))
myVector.InsertNextTuple4(1,1,4,2)

pointListNode.AddControlPointWorld(vtk.vtkVector3d(-20, -20, -10.2))
myVector.InsertNextTuple4(1,2,4,5)

pointListNode.AddControlPointWorld(vtk.vtkVector3d(-50, -60, -10.2))
myVector.InsertNextTuple4(3,3,4,1)

pointListNode.AddControlPointWorld(vtk.vtkVector3d(90, 40, -10.2))
myVector.InsertNextTuple4(4,4,4,7)

pointListNode.AddControlPointWorld(vtk.vtkVector3d(140, 70, -10.2))
myVector.InsertNextTuple4(5,5,4,3)

someMeasurement = slicer.vtkMRMLStaticMeasurement()
someMeasurement.SetName('SomeMeasurement')
someMeasurement.SetUnits('mm')
someMeasurement.SetPrintFormat('')  # Prevent from showing up in SH Description
someMeasurement.SetControlPointValues(myVector)
pointListNode.AddMeasurement(someMeasurement)
</code></pre>
<p>The points can be accessed using VTK array interface as shown above but can also be accessed (read and written) as a numpy array:</p>
<pre><code class="lang-python">print(slicer.util.arrayFromMarkupsControlPointData(pointListNode, 'SomeVector'))
</code></pre>
<p>The data is stored in the .mrk.json file:</p>
<pre><code class="lang-auto">{
...
    "markups": [
        {
            "type": "Fiducial",
...
            "controlPoints": [
                {
                    "id": "1",
                    "label": "MarkupsFiducial-1",
                    "position": [-40.0, -50.0, -10.2],
                    "orientation": [-1.0, -0.0, 0.0, -0.0, -1.0, 0.0, -0.0, -0.0, 1.0],
...
                },
                {
                    "id": "2",
                    "label": "MarkupsFiducial-2",
                    "description": "",
                    "position": [20.0, 20.0, -10.2],
                    "orientation": [-1.0, -0.0, 0.0, -0.0, -1.0, 0.0, -0.0, -0.0, 1.0],
...
                },
...
            ],
            "measurements": [
                {
                    "name": "SomeMeasurement",
                    "enabled": true,
                    "units": "mm",
                    "controlPointValues": [[1.0, 1.0, 4.0, 2.0], [1.0, 2.0, 4.0, 5.0], [3.0, 3.0, 4.0, 1.0], [4.0, 4.0, 4.0, 7.0], [5.0, 5.0, 4.0, 3.0]
                    ]
                }
            ],
   ...
     }
    ]
}
</code></pre>

---

## Post #3 by @Saima (2021-11-11 05:38 UTC)

<p>Hi Andras,<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e01f36972dbbf567d0dbb95804a7b7c4f4e82dc3.png" alt="image" data-base62-sha1="vYFPiI2XD2Glt1OulO2k3VmjwVd" width="425" height="291"></p>
<p>is there a way to change the orientation using user interaction with the fiducial instead of adding the values to the orientation array.</p>
<p>does the pointing of arrow fiducial changes with the change in the orientation matrix?</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #4 by @lassoan (2021-11-11 05:50 UTC)

<p>In the future we’ll probably have an option to orient the markups control point glyphs using the point’s orientation, but there are no concrete plans. There are many alternative options, though.</p>
<p>Option A: You can get the point positions and orientations from the markups node and use those as inputs for a vtkgGlyph3D filter to generate a model of oriented glyphs.</p>
<p>Option B: Use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#visualization-modes">transform visualization features</a> (oriented glyphs in 2D and 3D, contours, deformed grids, etc.). You can choose to display the vector field at fiducial positions only. If the vectors are already defined with a dense displacement field (bspline or grid) then those can be loaded directly as a transform. If you have the vectors computed for each fiducial only, then you can generate the displacement field using Fiducial registration wizard module (in SlicerIGT extension).</p>
<p>There are many other options, but to be able to give an informed advice, we would need to know what your end goal is. What would you like to visualize for what purpose?</p>

---
