# Cropped volume is not accessible

**Topic ID**: 17732
**Date**: 2021-05-22
**URL**: https://discourse.slicer.org/t/cropped-volume-is-not-accessible/17732

---

## Post #1 by @KAVIYA_DHARSHINI (2021-05-22 10:21 UTC)

<p>Operating system:windows 10 ,64bit<br>
Slicer version:4.1120200930<br>
Expected behavior: able to load and do other operations with cropped volume .<br>
Actual behavior: I want to run python script to load an dicom series, get roi and do thresholding inside the roi. For that purpose, I tried to crop the roi using  this code :</p>
<p><strong>def createCroppedVolume(inputVolume, roi):</strong></p>
<hr>
<p>**    cropVolumeLogic = slicer.modules.cropvolume.logic()**<br>
**    cropVolumeParameterNode = slicer.vtkMRMLCropVolumeParametersNode()**<br>
**    cropVolumeParameterNode.SetROINodeID(roi.GetID())**</p>
<hr>
<p>**    cropVolumeParameterNode.SetInputVolumeNodeID(inputVolume.GetID())**<br>
**    cropVolumeParameterNode.SetVoxelBased(True)**<br>
**    cropVolumeLogic.Apply(cropVolumeParameterNode)**<br>
**    cropV = slicer.mrmlScene.GetNodeByID(cropVolumeParameterNode.GetOutputVolumeNodeID())**<br>
**    slicer.mrmlScene.AddNode(cropV)**<br>
**    return cropV**</p>
<p>after this step, the cropV is not visible on the red or any other slices. but I can see this in the data module as :</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31ede708e9df8f64c7025058ebb40865e1e4caa3.png" alt="image" data-base62-sha1="77H6buALV8NP7vsmozmEbOXLYVJ" width="570" height="178"><br>
once i click the data, it becomes visible and again if the cropV is given as input to thresholding function, there is an error saying “crop V is not defined”. kindly help me in this regard. Thanks in advance.</p>

---

## Post #2 by @chir.set (2021-05-23 19:02 UTC)

<p>This should be the missing step :</p>
<pre><code>def showInSliceViews(inputVolume)
    views = slicer.app.layoutManager().sliceViewNames()
    for view in views:
        view_logic = slicer.app.layoutManager().sliceWidget(view).sliceLogic()
        view_cn = view_logic.GetSliceCompositeNode()
        view_cn.SetBackgroundVolumeID(inputVolume.GetID())
        view_logic.FitSliceToAll()</code></pre>

---
