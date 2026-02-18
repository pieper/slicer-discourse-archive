# Question about instancing efficiency between vtk8.2 and vtk9.0

**Topic ID**: 23885
**Date**: 2022-06-15
**URL**: https://discourse.slicer.org/t/question-about-instancing-efficiency-between-vtk8-2-and-vtk9-0/23885

---

## Post #1 by @xianger-qi (2022-06-15 03:44 UTC)

<p>Hey guys, i took a test about variable instancing efficiency between vtk8.2 and vtk9.0 on different class.<br>
Here was what i got:</p>
<p>testing times: 10000<br>
Statistical method: average instancing time<br>
the method instancing: vtkSmartPointer《class》 variable = vtkSmartPointer《class》::New();</p>
<p>VTK 9.0.3:<br>
vtkGenericCell: 1.5002 us<br>
vtkSphere: 0.0703 us<br>
vtkSTLReader: 4.3552 us</p>
<p>====================================</p>
<p>VTK 8.2:<br>
vtkGenericCell: 8.6075 us<br>
vtkSphere: 0.2852 us<br>
vtkSTLReader: 34.239 us</p>
<p>There are two questions for me.<br>
FIRST, on the different version vtk, the same classes have significant instancing time that approximately is 10 times, and is there any optimizations?<br>
SECOND, on the same version vtk, the different classes also have significant instancing time. what causes the difference?</p>
<p>Thanks for your reading!</p>

---

## Post #2 by @pieper (2022-06-15 12:10 UTC)

<p>FYI, This would be a better topic for the vtk discourse.  In general though I think it’s good that the times are going down.  To know exactly why you would need to look at the constructors for the various classes and if you are really interested you could use a code profiler to see where the time is being spent.</p>

---
