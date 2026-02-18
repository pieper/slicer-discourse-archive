# QVTKWidgetPlugin destructed after ctreating a polydata

**Topic ID**: 20890
**Date**: 2021-12-02
**URL**: https://discourse.slicer.org/t/qvtkwidgetplugin-destructed-after-ctreating-a-polydata/20890

---

## Post #1 by @dalbenzioG (2021-12-02 19:06 UTC)

<p>Hello,</p>
<p>I created the following function that should generate a polydata out of x, y, and z coordinate of points.</p>
<pre><code class="lang-auto">def createPolyData(x , y , z , maxNumPoints=1e6) :
    data = np.column_stack((x.ravel() , y.ravel() , z.ravel()))

    polyPoints = vtk.vtkPoints()
    vtkDepth = vtk.vtkDoubleArray()
    vtkCells = vtk.vtkCellArray()
    vtkPolyData = vtk.vtkPolyData()

    for k in range(size(data , 0)) :
        point = data[k]

        if polyPoints.GetNumberOfPoints() &lt; maxNumPoints :
            pointId = polyPoints.InsertNextPoint(point[:])
            vtkDepth.InsertNextValue(point[2])
            vtkCells.InsertNextCell(1)
            vtkCells.InsertCellPoint(pointId)
            vtkCells.Modified()
            polyPoints.Modified()
            vtkDepth.Modified()
    vtkPolyData.SetPoints(polyPoints)
    vtkPolyData.SetVerts(vtkCells)
    vtkDepth.SetName('Distance')
    vtkPolyData.GetPointData().SetScalars(vtkDepth)
    vtkPolyData.GetPointData().SetActiveScalars('Distance')

    return vtkPolyData
</code></pre>
<p>The attached picture is obtained after rendering that polydata in vtk using the createPolyData function<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caa602c5d287b6a70990ab4b94c3627a11f1af6f.png" alt="pointsefd" data-base62-sha1="sUI7MN09odwfOLpbT0FEoC2rDdB" width="427" height="468"><br>
When I try to display the same polydata in 3DSlicer I encounter the following error : <strong>QVTKWidgetPlugin destructed</strong> after getting the output polydata and, after a while, Slicer crash.</p>
<p>So far I have no clue how to solve this problem. Do you have any feedback?<br>
I hope I have been able to explain clearly my problem otherwise, I will be happy to give you more details.<br>
Thank you <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>Operating System: Ubuntu 20.04.3 LTS<br>
Slicer Version : 4.13.0 r30429 / 00d2939</p>

---

## Post #2 by @dalbenzioG (2022-02-10 08:32 UTC)

<p>Updating Slicer has fixed the problem <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=12" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:" loading="lazy" width="20" height="20"></p>

---
