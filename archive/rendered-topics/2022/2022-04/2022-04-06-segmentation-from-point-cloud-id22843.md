# Segmentation from point cloud

**Topic ID**: 22843
**Date**: 2022-04-06
**URL**: https://discourse.slicer.org/t/segmentation-from-point-cloud/22843

---

## Post #1 by @Saima (2022-04-06 03:11 UTC)

<p>Dear Andras,<br>
I have .vtk a surface mesh, which I generated using pyvista using cloud of points.<br>
I could not see .vtk in slicer but I can see in paraview and I convert it into vtp and now ican see the file in slicer. I now need to convert it into nrrd file. I tried export it into segmentation node but it is not visible in axial, sagital or coronal view. I could not see it.</p>
<p>is there any solution to it</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #2 by @lassoan (2022-04-06 05:24 UTC)

<p>Where does the cloud of points come from? From a surface scanner, biomechanical simulation, …?</p>
<p>An issue with the .vtk file format that you don’t know what it contains (polygonal mesh, unstructured grid, image volume, etc.) - could you share an example file?</p>
<p>I suspect that you have not actually generated a surface mesh in pyvista, but you probably just visualized the point cloud.  What exact VTK filters did you use via pyvista? (if you are not sure then look into the source code or debug into pyvista or ask its developer)</p>
<p>How did you convert the .vtk file to .vtp in ParaView? Maybe you just saved the points. There are many tools to reconstruct surfaces from point cloud, but they each have its own limitations. To decide which one to use, we would need to learn more about where the data comes from, how it looks like, and what it will be used for.</p>

---
