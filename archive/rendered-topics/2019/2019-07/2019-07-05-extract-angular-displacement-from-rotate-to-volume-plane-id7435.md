---
topic_id: 7435
title: "Extract Angular Displacement From Rotate To Volume Plane"
date: 2019-07-05
url: https://discourse.slicer.org/t/7435
---

# Extract angular displacement from "Rotate to Volume Plane"

**Topic ID**: 7435
**Date**: 2019-07-05
**URL**: https://discourse.slicer.org/t/extract-angular-displacement-from-rotate-to-volume-plane/7435

---

## Post #1 by @Manuel (2019-07-05 15:13 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8.0</p>
<p>Hello everybody,</p>
<p>is there any possibility to extract the angular displacement (axial , sagittal, coronal or x, y, z) between the default aligned slicer viewers of the slice and the realigned slicer viewers after using the  “Rotate to Volume Plane” function.<br>
I want to compare this angles with my calculated angles gathered from the “ImageOrientationPatient” (0020,0037) attribute of the DICOM meta data.</p>
<p>Thanks in advanced.</p>

---

## Post #2 by @lassoan (2019-07-05 15:32 UTC)

<p>Image axis directions in RAS coordinate system is available in the first 3 columns of the <code>ijkToRasDirections</code> matrix returned by <a href="https://apidocs.slicer.org/master/classvtkMRMLVolumeNode.html#a6e54e58a3cc1064140a91745b6134c3f" rel="nofollow noopener">vtkMRMLVolumeNode.GetIJKToRASDirectionMatrix</a>:</p>
<pre><code class="lang-python">volumeNode = getNode('MRHead')
ijkToRasDirections = vtk.vtkMatrix4x4()
volumeNode.GetIJKToRASDirectionMatrix(ijkToRasDirections)
print(ijkToRasDirections)
</code></pre>

---

## Post #3 by @Manuel (2019-07-05 17:37 UTC)

<p>Thats perfect! Thank you so much and thank you for the quick response.</p>

---
