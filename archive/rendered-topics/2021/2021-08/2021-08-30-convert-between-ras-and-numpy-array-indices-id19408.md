---
topic_id: 19408
title: "Convert Between Ras And Numpy Array Indices"
date: 2021-08-30
url: https://discourse.slicer.org/t/19408
---

# Convert between RAS and numpy array indices

**Topic ID**: 19408
**Date**: 2021-08-30
**URL**: https://discourse.slicer.org/t/convert-between-ras-and-numpy-array-indices/19408

---

## Post #1 by @M.Odaba (2021-08-30 00:05 UTC)

<p>Hi Iassoan,</p>
<p>Would you please explain how to convert the coordinates to world coordinate system (X, Y, Z)? Would you be able to provide the script that convert these coordinates (coordinates = np.where(labelArray==labelValue)) which I think ther are in IJK format, to RAS (X, Y, Z)?<br>
I know that vtk.vtkMatrix4x4() will do the job and I’ve already looked into some examples such as <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/volumes.html?highlight=coordinate#get-volume-voxel-coordinates-from-markup-fiducial-ras-coordinates" class="inline-onebox" rel="noopener nofollow ugc">Volumes — 3D Slicer documentation</a>, but have not been able to figure out the right code.</p>
<p>Thanks,<br>
Mostafa</p>

---

## Post #2 by @ungi (2021-08-31 20:04 UTC)

<p>First, download MRHead data from Sample Data module</p>
<pre><code class="lang-auto">import numpy as np
volumeArray = slicer.util.array("MRHead")  # Get the image data in numpy array format
volumeArray[60, 127, 150] = 0  # Make one voxel black, numpy array is in KJI, not IJK.
volumeNode = slicer.mrmlScene.GetFirstNodeByName("MRHead")
volumeNode.Modified()  # I think this is needed to let Slicer know the image was modified.
ijkToRasMatrix = vtk.vtkMatrix4x4()
volumeNode.GetIJKToRASMatrix(ijkToRasMatrix)
ijkPoint = np.array([150, 127, 60])  # This is IJK, opposite order compared to KJI.
rasPoint = ijkToRasMatrix.MultiplyFloatPoint(np.append(ijkPoint, 1))
print(rasPoint)
</code></pre>
<p>If you hover your mouse over the new black point in the image, Data Probe should show the same coordinates that were printed at the end of this script.</p>

---
