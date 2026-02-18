# Non-manifold of vtk delaunay

**Topic ID**: 39682
**Date**: 2024-10-14
**URL**: https://discourse.slicer.org/t/non-manifold-of-vtk-delaunay/39682

---

## Post #1 by @Sofia_Gonzalez (2024-10-14 07:52 UTC)

<p>Hello everyone, I’m trying to calculate the diameter of a carotid making planes perpendicular to the flow of the blood, and I want to make that planes and then calculate the diameter, and it works, but in some points it gives me this error:</p>
<p>ERROR: In …\Filters\Core\vtkMassProperties.cxx, line 95<br>
vtkMassProperties (000001507ED79560): No data to measure…!</p>
<p>ERROR: In …\Filters\Core\vtkDelaunay2D.cxx, line 819<br>
vtkDelaunay2D (000001500F304260): ERROR: Edge [51 18] is non-manifold!!!</p>
<p>ERROR: In …\Common\ExecutionModel\vtkExecutive.cxx, line 784<br>
vtkCompositeDataPipeline (000001507EB4E5B0): Algorithm vtkDelaunay2D(000001500F304260) returned failure for request: vtkInformation (000001507EDAC7B0)<br>
Debug: Off<br>
Modified Time: 3127232<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_DATA<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FROM_OUTPUT_PORT: 0<br>
FORWARD_DIRECTION: 0</p>

---

## Post #2 by @chir.set (2024-10-14 09:12 UTC)

<p>You may consider the ‘Cross-section analysis’ module in SlicerVMTK extension.</p>
<p>Consider also giving comprehensive details about your workflow.</p>

---
