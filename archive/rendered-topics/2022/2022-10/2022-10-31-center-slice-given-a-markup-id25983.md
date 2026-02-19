---
topic_id: 25983
title: "Center Slice Given A Markup"
date: 2022-10-31
url: https://discourse.slicer.org/t/25983
---

# Center slice given a markup

**Topic ID**: 25983
**Date**: 2022-10-31
**URL**: https://discourse.slicer.org/t/center-slice-given-a-markup/25983

---

## Post #1 by @bserrano (2022-10-31 16:27 UTC)

<p>Hi,</p>
<p>I have a markups curve along a vessel and I would like the red slice to be automatically centred on the markups point. This would be very useful when setting a plane perpendicular to the centreline, how can I do this?</p>
<p>Furthermore, is it possible to obtain which coordinate in i,k,j of the perpendicular reformatted images corresponds to each point of the centreline in x,y,z?</p>
<p>Thanks,</p>
<p>Belén</p>

---

## Post #2 by @lassoan (2022-10-31 16:39 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="1" data-topic="25983">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>I have a markups curve along a vessel and I would like the red slice to be automatically centred on the markups point. This would be very useful when setting a plane perpendicular to the centreline, how can I do this?</p>
</blockquote>
</aside>
<p>The easiest is to click on the markup point, which centers all slice views on the point (except the view that you are interacting with, as you would not want the point to jump away from your mouse pointer).</p>
<p>You can also use <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/CrossSectionAnalysis.md">Cross-section analysis</a> module in SlicerVMTK extension to explore/adjust a centerline.</p>
<aside class="quote no-group" data-username="bserrano" data-post="1" data-topic="25983">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>Furthermore, is it possible to obtain which coordinate in i,k,j of the perpendicular reformatted images corresponds to each point of the centreline in x,y,z?</p>
</blockquote>
</aside>
<p>You can find code snippets for all these kind of commonly needed operations in the script repository. See for example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates">here</a>.</p>

---

## Post #4 by @bserrano (2022-11-03 16:05 UTC)

<p>Hi,</p>
<p>The code you suggest (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates" rel="noopener nofollow ugc">voxel-coordinates-from-markup</a>) works perfectly when using the original volume. However it does not work when using the resliced volume.</p>
<p>What I have is a centerline along a vessel. Then I use endoscopy and volume reslice driver modules to obtain a perpendicular view as in:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e62b551785dfb0c5fadabd419c9556ff52b6adef.png" alt="imagen" data-base62-sha1="wQaEL7QIAUiN83ClML2EbG604gv" width="375" height="258"></p>
<p>I need to obtain the coordinate of the centerline point of the perpendicular image (red point in the image). What I’m doing now is</p>
<pre><code class="lang-auto">    curveNode = slicer.util.getNode("MarkupsCurve")
    points = vtk.util.numpy_support.vtk_to_numpy(curveNode.GetCurve().GetPoints().GetData())
    
    input("Adjust view") #Manually adjust view (I want to automatize this aswell)
    
    # Create a Fiducial so I can use getCenter
    myFidNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
    myFidNode.SetName("myFidNode")
    
    centers = []
    
    for index in range(0, len(points)):
        
        sliceNodeID = "vtkMRMLSliceNodeRed"
        
        # Get image data from slice view
        sliceNode = slicer.mrmlScene.GetNodeByID(sliceNodeID)
        appLogic = slicer.app.applicationLogic()
        sliceLogic = appLogic.GetSliceLogic(sliceNode)
        sliceLayerLogic = sliceLogic.GetBackgroundLayer()
        reslice = sliceLayerLogic.GetReslice()
        reslicedImage = vtk.vtkImageData()
        reslicedImage.DeepCopy(reslice.GetOutput())
        
        # Create new volume node using resliced image 
        volumeNodeResliced = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
        volumeNodeResliced.SetIJKToRASMatrix(sliceNode.GetXYToRAS())
        volumeNodeResliced.SetAndObserveImageData(reslicedImage)
        volumeNodeResliced.CreateDefaultDisplayNodes()
        volumeNodeResliced.CreateDefaultStorageNode()
        
        # Get voxels as a numpy array
        voxels = slicer.util.arrayFromVolume(volumeNodeResliced)
        
        # Get vessel center in (i,j)
        myFidNode.AddFiducialFromArray(points[index])
        center = getCenter("myFidNode", volumeNodeResliced)
        myFidNode.RemoveAllControlPoints()
</code></pre>
<p>Where getCenter is <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates" rel="noopener nofollow ugc">voxel-coordinates-from-markup</a>. <em>voxels</em> contains pixel information of the resliced image in redSlice view (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-reformatted-image-from-a-slice-viewer-as-numpy-array" rel="noopener nofollow ugc">get-reformatted-image-from-a-slice-viewer-as-numpy-array</a>).</p>
<p>I want <strong>center</strong> and <strong>voxels</strong> to correspond but it’s not working in all slices.<br>
How can I fix that?</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @lassoan (2022-11-03 17:50 UTC)

<p>I would recommend using <a href="https://github.com/PerkLab/SlicerSandbox#curved-planar-reformat">Curved Planar Reformat</a> module (in Sandbox extension). It provides a straightened image (series of slices obtained by reslicing along the curve) and also a transform that you can conveniently use to transform between the original image space and the straightened image space.</p>
<p>If this is not what you want then you can use or customize <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/CrossSectionAnalysis.md">Cross-section analysis</a> module (in SlicerVMTK extension), it probably already contains all the computations you need.</p>

---
