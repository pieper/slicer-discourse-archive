---
topic_id: 18439
title: "Can We Split An Array Of Points In Islands"
date: 2021-06-30
url: https://discourse.slicer.org/t/18439
---

# Can we split an array of points in islands?

**Topic ID**: 18439
**Date**: 2021-06-30
**URL**: https://discourse.slicer.org/t/can-we-split-an-array-of-points-in-islands/18439

---

## Post #1 by @chir.set (2021-06-30 19:23 UTC)

<p>My final goal is to measure cross-section area of arterial segments.</p>
<p>The image below shows a segmented aorto-iliac aneurysm with a centerline in theaorta and the left iliac artery. The cross-section is moved along the Centerline Model with Cross-Section analysis module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/5730a5ece76b77a28bc2414bab9c05cb39603b9c.jpeg" data-download-href="/uploads/short-url/crjLCA4OnAwBf35g7bgiBoWC8MI.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5730a5ece76b77a28bc2414bab9c05cb39603b9c_2_598x500.jpeg" alt="Screenshot" data-base62-sha1="crjLCA4OnAwBf35g7bgiBoWC8MI" width="598" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5730a5ece76b77a28bc2414bab9c05cb39603b9c_2_598x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5730a5ece76b77a28bc2414bab9c05cb39603b9c_2_897x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/5730a5ece76b77a28bc2414bab9c05cb39603b9c.jpeg 2x" data-dominant-color="222118"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1112×929 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>At the iliac level, two islands of the same segment are naturally drawn in the Red slice view. The code below gets the contour of both iliacs in an array of points, and creates a model with a 2D Delaunay filter. It’s necessarily a single model, corresponding to the array input.</p>
<pre><code class="lang-auto">def TryCut(self, center, normal):
    segmentation = slicer.util.getNode("Output Volume_1-segmentation")
    segment = segmentation.GetSegmentation().GetSegment("Output Volume_1")
    plane = vtk.vtkPlane()
    plane.SetOrigin(center)
    plane.SetNormal(normal)
    
    closedSurfacePolyData = vtk.vtkPolyData()
    segmentation.GetClosedSurfaceRepresentation("Output Volume_1", closedSurfacePolyData)
    
    planeCut = vtk.vtkCutter()
    planeCut.SetInputData(closedSurfacePolyData)
    planeCut.SetCutFunction(plane)
    planeCut.Update()
    
    if self.cutModelNode is not None:
        slicer.mrmlScene.RemoveNode(self.cutModelNode)
    self.cutModelNode = slicer.modules.models.logic().AddModel(planeCut.GetOutputPort())
    cutModelDisplayNode = self.cutModelNode.GetDisplayNode()
    cutModelDisplayNode.SetColor(0,0,1)
    cutModelDisplayNode.SetOpacity(1.0)
    
    delaunay = vtk.vtkDelaunay2D()
    delaunay.SetInputData(self.cutModelNode.GetPolyData())
    self.cutModelNode.SetPolyDataConnection(delaunay.GetOutputPort())
</code></pre>
<p>I wish to be able to splt the array output of vtkCutter in as many islands as there may be, identify each island array and get hold of each of them. This would permit to create a model around the current centerline point only.</p>
<p>I don’t know if it is possible at all, simply would be best. I suppose it should be possible, because the Islands module does manage unconnected objects, but I don’t have a signe clue how this could be done simply.</p>
<p>Thanks for any input.</p>

---

## Post #2 by @lassoan (2021-07-02 03:59 UTC)

<p>A very simple solution is to assign one of the branches to another segment. It takes about 10-20 seconds. See step-by-step instructions <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">here</a>.</p>
<p>If you want to save this 10-20 seconds then you can use VMTK to split the branches fully automatically. See details <a href="http://www.vmtk.org/tutorials/BranchSplitting.html">here</a> and example script <a href="https://github.com/vmtk/vmtk/blob/63a3b990328d8dfaa6ffd31968fc341cad9dbe67/vmtkScripts/vmtkbranchclipper.py#L117-L139">here</a>. It will probably take a few days to figure out how the filter works exactly, so it pays off if you need to segment more than 5000 cases.</p>

---

## Post #3 by @chir.set (2021-07-02 13:05 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="18439">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>split the branches fully automatically. See details <a href="http://www.vmtk.org/tutorials/BranchSplitting.html" rel="noopener nofollow ugc">here</a> and example script <a href="https://github.com/vmtk/vmtk/blob/63a3b990328d8dfaa6ffd31968fc341cad9dbe67/vmtkScripts/vmtkbranchclipper.py#L117-L139" rel="noopener nofollow ugc">here</a>.</p>
</blockquote>
</aside>
<p>That seems very interesting, I’ll delve into this ASAP. Didn’t know about that. Thanks.</p>

---
