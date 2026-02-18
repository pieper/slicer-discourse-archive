# GetPlaneCornerPoints function and vtkPoints Class

**Topic ID**: 37125
**Date**: 2024-07-01
**URL**: https://discourse.slicer.org/t/getplanecornerpoints-function-and-vtkpoints-class/37125

---

## Post #1 by @ahenry (2024-07-01 17:55 UTC)

<p>Hello,</p>
<p>I am interested in calling the RAS coordinates of the corners of markup planes after they have been created and rotated. I checked the api docs and found that the vtkMRMLMarkupsPlaneNode class has a GetPlaneCornerPoints function that takes in a vtkPoints object, but I did not see anything in the docs about the vtkPoints object. Is there a way I can get the plane corner points easily and is there any other info on the vtkPoints object?</p>
<p>Thanks,</p>

---

## Post #2 by @ahenry (2024-07-03 18:37 UTC)

<p>I was able to find a solution. I found the vtkPoints class in the vtk api documentation. Here is how I solved my issue.</p>
<pre><code class="lang-auto">from vtkmodules.util.numpy_support import vtk_to_numpy

#create instance of plane markup class
plane = getNode('Name_of_Plane_Markup')

#create instance of vtkPoints
points = vtk.vtkPoints()

plane.GetPlaneCornerPoints(points)

corner_points = vtk_to_numpy(points.GetData())
</code></pre>

---
