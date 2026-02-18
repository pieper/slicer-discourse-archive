# Generate 2D X-ray image from volume, just like DRR

**Topic ID**: 976
**Date**: 2017-08-31
**URL**: https://discourse.slicer.org/t/generate-2d-x-ray-image-from-volume-just-like-drr/976

---

## Post #1 by @langderyos (2017-08-31 13:31 UTC)

<p>Hi,<br>
I’m finding a way to generate 2D X-ray image from volume data, just like what DRR does.<br>
Is there any extension which can do this?Or can I do it in a python way?</p>
<p>thanks<br>
langderyos,</p>

---

## Post #2 by @lassoan (2017-08-31 13:58 UTC)

<p>Probably the easiest way to get DRR-like images is to set up thick slice display using Python. For example, copy-paste this code snippets into the Python console to get started:</p>
<p>Maximum intensity projection:</p>
<pre><code>sliceNode = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed')
appLogic = slicer.app.applicationLogic()
sliceLogic = appLogic.GetSliceLogic(sliceNode)
sliceLayerLogic = sliceLogic.GetBackgroundLayer()
reslice = sliceLayerLogic.GetReslice()
reslice.SetSlabModeToMax()
reslice.SetSlabNumberOfSlices(600)
reslice.SetSlabSliceSpacingFraction(0.5)
sliceNode.Modified()
</code></pre>
<p>Result for CTChest example data set:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9eec191b459a546649043480efe82c708c1be57.png" alt="image_00036" data-base62-sha1="sOnvgb1IhLKUiBvzSFDAVjuRd4j" width="548" height="446"></p>
<p>You could get more DRR-like image if you change slab mode to mean instead of max (<code>reslice.SetSlabModeToMean()</code>), but usually it makes details more difficult to see.</p>
<p>Same data set with DRR-like mean slab mode:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1c09bada673304ee908e68ee898b223ca47dd5c.png" alt="image_00035" data-base62-sha1="wd65H2qJ4KX3NX6t8snwsQKvxuI" width="548" height="446"></p>
<p>See some more examples <a href="http://slicer-devel-archive.65872.n3.nabble.com/Faster-slice-view-thick-slices-and-MIP-slice-view-mode-td4033264.html">here</a>.</p>
<p>For faster updates and display in 3D view, you can configure Volume rendering module to show a maximum intensity projection (MIP). For most realistic DRR rendering, you can try to use Plastimatch extension.</p>

---

## Post #3 by @langderyos (2017-09-01 05:30 UTC)

<p>Hi, Andras</p>
<p>Thanks a lot for your reply! I tried it and find it very helpful for me.But in slicer 4.6.0, there  is no content in  plastimatch module.Perhaps it’s a problem about version.</p>
<p>thanks again<br>
langderyos</p>

---
