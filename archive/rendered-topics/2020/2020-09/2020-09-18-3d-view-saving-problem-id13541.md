---
topic_id: 13541
title: "3D View Saving Problem"
date: 2020-09-18
url: https://discourse.slicer.org/t/13541
---

# 3D view saving problem

**Topic ID**: 13541
**Date**: 2020-09-18
**URL**: https://discourse.slicer.org/t/3d-view-saving-problem/13541

---

## Post #1 by @opetne (2020-09-18 10:20 UTC)

<p>4.11.0 version<br>
If I want to save a screenshot of the 3D view only a small blue strip is saved. I tried to save the 3D view with transparent background as well with this script:<br>
renderWindow = slicer.app.layoutManager().threeDWidget(0).threeDView().renderWindow()<br>
renderWindow.SetAlphaBitPlanes(1)<br>
wti = vtk.vtkWindowToImageFilter()<br>
wti.SetInputBufferTypeToRGBA()<br>
wti.SetInput(renderWindow)<br>
writer = vtk.vtkPNGWriter()<br>
writer.SetFileName(“D:/DICOM/screenshot.png”)<br>
writer.SetInputConnection(wti.GetOutputPort())<br>
writer.Write()</p>
<p>but the result is the same<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d097874e35e5ec520490e84056c41256f8eca5ef.png" alt="screenshot" data-base62-sha1="tLhXESoHmemgIQ5c7b6XGB54dpt" width="100" height="14"></p>

---
