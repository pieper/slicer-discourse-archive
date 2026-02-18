# Transform does not match VTM matrix array

**Topic ID**: 12370
**Date**: 2020-07-04
**URL**: https://discourse.slicer.org/t/transform-does-not-match-vtm-matrix-array/12370

---

## Post #1 by @talmazov (2020-07-04 02:49 UTC)

<p>I am obtaining a plane’s transform matrix then trying to use it elsewhere</p>
<p>transform = slicer.vtkMRMLTransformNode()<br>
transform.SetName(model.GetName()+‘_trans’)<br>
slicer.mrmlScene.AddNode(transform)<br>
model.SetAndObserveTransformNodeID(transform.GetID())<br>
my_matrix = transform.GetMatrixTransformFromParent()<br>
xmlmx = slicer.util.arrayFromVTKMatrix(my_matrix)</p>
<p>the transform in slicer is<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f839a512b013cf7e34c190b2daded916190db4a.png" alt="image" data-base62-sha1="4uML4GOt8M96AK1ENqDtARCB2Wu" width="619" height="106"></p>
<p>while VTK returns<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47784d4473629db8d1ffcf5d894d41734fc6891a.png" alt="image" data-base62-sha1="acfE2K2U2ODcZeoVFu9QGZVB9b4" width="548" height="75"></p>
<p>it seems like we not only need to transpose the matrix but the location values do not match up</p>
<p>not sure what is going</p>

---

## Post #2 by @lassoan (2020-07-04 02:51 UTC)

<p>TransformFromParent is the resampling transform (for transforming images). TransformToParent is the modeling transform (for transforming, points, meshes, etc.). Probably you are interested in TransformToParent.</p>

---

## Post #3 by @talmazov (2020-07-04 03:25 UTC)

<p>changed to<br>
transform.GetMatrixTransformToParent()<br>
and it worked very well!</p>
<p>thanks!</p>

---
