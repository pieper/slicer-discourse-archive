# Loading multiple volumes

**Topic ID**: 1455
**Date**: 2017-11-14
**URL**: https://discourse.slicer.org/t/loading-multiple-volumes/1455

---

## Post #1 by @jperdomo23 (2017-11-14 11:31 UTC)

<p>Hi slicer-devel,</p>
<p>Does anyone know a Python call in the Slicer API for loading multiple volumes at once? I have been trying different parameters with slicer.util.loadVolume() without success. I am trying to avoid for-looping across filenames with this call, since it shows a progress dialog for each individual volume.</p>
<p>Thank you,</p>
<p>Jonathan Perdomo</p>

---

## Post #2 by @lassoan (2017-11-14 11:50 UTC)

<p>You can use VTK file readers to read into vtkImageData and create volume nodes and set the image data in them.</p>

---

## Post #3 by @jperdomo23 (2017-11-14 13:23 UTC)

<p>I will try, thank you.</p>

---
