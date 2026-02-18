# Select contour from the mrml scene

**Topic ID**: 14222
**Date**: 2020-10-24
**URL**: https://discourse.slicer.org/t/select-contour-from-the-mrml-scene/14222

---

## Post #1 by @marianaslicer (2020-10-24 13:25 UTC)

<p>Hello everyone,</p>
<p>I’m using the 3D slicer version 4.10.0 and I want to select a specific contour in my module:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5ab305ab9126da17318c83da0ed9d5346dc5e2ca.png" alt="image" data-base62-sha1="cWmwA7zuJHlvYtewnGmsivsHu9s" width="556" height="194"></p>
<p>However, in the mrml scene I can’t get any ID for the contours:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/dedcd9224cf55817567fbfacfdca430e4ec8e630.png" alt="image" data-base62-sha1="vNxa8qq4x7K8qk2oO2MQqdKur84" width="556" height="313"></p>
<p>So, the following code doesn’t work:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4aca1082c0294e28970ee92ca8f5b1b1028fb64.png" alt="image" data-base62-sha1="pMjNDN06CVF7OF95aMZvD4SqCDa" width="686" height="280"></p>
<p>Any idea how to fix this?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2020-10-24 14:23 UTC)

<p>There is a specific widget for segment selection: <a href="https://apidocs.slicer.org/master/classqMRMLSegmentSelectorWidget.html">qMRMLSegmentSelectorWidget</a>.</p>

---

## Post #3 by @marianaslicer (2020-10-25 14:23 UTC)

<p>Thanks a lot!</p>
<p>I used the connection: self.inputSegmentationSelector.connect(“currentSegmentChanged(QString)”, self.onContourChange)</p>
<p>And now I want to calculate the center of mass of the selected contour. So I used the following code:</p>
<p>modelNode = slicer.mrmlScene.GetNodesByName((str(targetContour)))<br>
pointCoordinates = slicer.util.arrayFromModelPoints(modelNode) # point coordinates of targetContour</p>
<p>but I’m having the error:</p>
<p>File “C:\Program Files\Slicer 4.10.0\bin\Python\slicer\util.py”, line 795, in arrayFromModelPoints<br>
pointData = modelNode.GetPolyData().GetPoints().GetData()<br>
AttributeError: ‘vtkCommonCorePython.vtkCollection’ object has no attribute ‘GetPolyData’</p>

---

## Post #4 by @lassoan (2020-10-25 14:48 UTC)

<p>You get the error because you pass a segmentation node to a function that  requires a model node.</p>
<p>What you are tryibg to achieve? Jumping to selected fiducial feature is already implemented. See for example in segment list widget (<a href="https://github.com/Slicer/Slicer/blob/a4017472d6220903f7f85c5e49b547f1f6830f39/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentsTableView.h#L65">https://github.com/Slicer/Slicer/blob/a4017472d6220903f7f85c5e49b547f1f6830f39/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentsTableView.h#L65</a>).</p>

---

## Post #5 by @marianaslicer (2020-10-25 15:45 UTC)

<p>I would like to select a specific segment in 3D slicer like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71217c00fcdf3fe312373989e0c76696eb9b9983.png" alt="image" data-base62-sha1="g8NH2fX1NJWuoJVjlBfE7rCSGAj" width="562" height="106"></p>
<p>And then I want to calculate the center of mass of the CTV1. So in order to use the function: getCenterOfMass(contour)</p>
<p>what I need to do?</p>

---
