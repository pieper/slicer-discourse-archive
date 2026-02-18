# 2D image on one slice

**Topic ID**: 15771
**Date**: 2021-02-01
**URL**: https://discourse.slicer.org/t/2d-image-on-one-slice/15771

---

## Post #1 by @nikoskot (2021-02-01 12:58 UTC)

<p>Hello,<br>
I would like to display a 2D image stored in a 3D numpy array (RGB image) only in one of the slices (for example the Red slice).</p>
<pre><code>img = np.zeros((50,50,3))
img[10:40,20:30, 0] = 200  # saturate a part of the first channel
new_volume_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
slicer.util.updateVolumeFromArray(new_volume_node, img)
slicer.app.layoutManager().sliceWidget('Red').sliceLogic().GetSliceCompositeNode().SetForegroundVolumeID(new_volume_node.GetID())
</code></pre>
<p>With the code above each dimension of the array is connected to one of the slices (1st dimension to Red, 2nd to Green, 3rd to Yellow). Is there a way to display the whole image to one slice?</p>

---

## Post #2 by @lassoan (2021-02-01 14:55 UTC)

<p>To display an RGB volume, you need to create a <code>vtkMRMLVectorVolumeNode</code> and array dimensions must be [dimZ, dimY, dimX, 3].</p>

---
