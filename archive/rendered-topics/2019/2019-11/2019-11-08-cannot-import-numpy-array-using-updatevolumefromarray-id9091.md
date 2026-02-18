# Cannot import numpy array using updateVolumeFromArray

**Topic ID**: 9091
**Date**: 2019-11-08
**URL**: https://discourse.slicer.org/t/cannot-import-numpy-array-using-updatevolumefromarray/9091

---

## Post #1 by @stevenagl12 (2019-11-08 17:45 UTC)

<p>I have a numpy file that I am trying to import using the updateVolumeFromArray function. The file can load into slicer as a numpy array, but the second I go to update the volume, and display the image (clicking on the volume eye button from the data module), the entire system crashes. I can call the matrix in, and I can perform operations on it such as finding out the unique values, but I cannot display it in slicer? My matrix is a 128X256X256 numpy array with binary values of 0-4.</p>

---

## Post #2 by @lassoan (2019-11-08 18:00 UTC)

<p>Can you provide sample code and data set?</p>

---

## Post #3 by @stevenagl12 (2019-11-08 18:04 UTC)

<p>So, I import my volume with <code>np.load(filepath)['arr_0']</code>. I then create a volume node with <code>volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", nodeName)</code> and update the volume with <code>updateVolumeFromArray</code>. The second I go to click on the visualize button the system crashes. Here is a link to my file: <a href="https://drive.google.com/open?id=1C4RmyRS-4YWwO_c6IhWOGEpV3ImGqVri" rel="nofollow noopener">https://drive.google.com/open?id=1C4RmyRS-4YWwO_c6IhWOGEpV3ImGqVri</a></p>

---

## Post #4 by @lassoan (2019-11-09 13:59 UTC)

<p>The link requires authentication. Please approve the read request or share with a public link.</p>

---

## Post #5 by @lassoan (2019-11-09 14:38 UTC)

<p>The problem was that the numpy array in that file had “long long” type. You had to cast it to a type that VTK can handle:</p>
<pre><code class="lang-auto">import numpy as np
filepath=r"c:\Users\andra\Downloads\am_output.npz"
volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
voxels=np.load(filepath)['arr_0'].astype(np.int16)
updateVolumeFromArray(volumeNode,voxels)
setSliceViewerLayers(background=volumeNode, fit=True)
</code></pre>
<p>I have updated <code>updateVolumeFromArray</code> to report an error when “long long” array is attempted to be loaded.</p>

---
