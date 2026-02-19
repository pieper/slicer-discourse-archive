---
topic_id: 19244
title: "Read Data File From Disk And Convert Displayable Node To Vtk"
date: 2021-08-18
url: https://discourse.slicer.org/t/19244
---

# Read data file from disk and convert displayable node to vtkActor or vtkProp

**Topic ID**: 19244
**Date**: 2021-08-18
**URL**: https://discourse.slicer.org/t/read-data-file-from-disk-and-convert-displayable-node-to-vtkactor-or-vtkprop/19244

---

## Post #1 by @xianger-qi (2021-08-18 09:16 UTC)

<p>I have some Non-DICOM data files. such as *.nrrd, *.stl, etc. but how can i read these data files from disk in C++, and convert these to vtkActor or vtkProp class?  Thanks for replying!</p>

---

## Post #2 by @xianger-qi (2021-08-19 08:49 UTC)

<p>Another question is how can i convert slicer data node to vtkProp or vtkActor and so on, because, maybe i want to display the data node via vtk render window directly not via slicer scene.</p>

---

## Post #3 by @pieper (2021-08-19 10:48 UTC)

<p>In Slicer the mapping between mrml nodes (for image and poly data) and vtk rendering is handled by displayable managers:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/DisplayableManagers" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/DisplayableManagers</a></p>

---
