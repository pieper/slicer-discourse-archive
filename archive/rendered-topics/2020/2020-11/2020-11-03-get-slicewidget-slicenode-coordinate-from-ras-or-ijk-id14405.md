---
topic_id: 14405
title: "Get Slicewidget Slicenode Coordinate From Ras Or Ijk"
date: 2020-11-03
url: https://discourse.slicer.org/t/14405
---

# Get SliceWidget / SliceNode Coordinate From RAS or IJK

**Topic ID**: 14405
**Date**: 2020-11-03
**URL**: https://discourse.slicer.org/t/get-slicewidget-slicenode-coordinate-from-ras-or-ijk/14405

---

## Post #1 by @EricM (2020-11-03 15:20 UTC)

<p>Hello,</p>
<p>I am trying to find the relationship between the coordinates used in the SliceWidgets / SliceNodes (Red, Yellow, Green) and the RAS or Voxel coordinates of a volumeNode.</p>
<p>Everytime I load a 3D image into Slicer, I apply “rotate to volume node” (see top of attached image) so that my slices in the Red Widget (x-y) plane are those of the DICOMS for my axial acquisitions. I have created various annotation modules where I have a button that jumps to the slices (Red, Yellow, Green) of the center of a segmentation/bounding box/markupLine etc. When I have a volumeNode that doesn’t have any off diagonal elements in the direction matrix, the RAS coordinates match perfectly with the coordinates of the SliceWidgets/Slice Nodes (Red, Yellow, Green) and I can use this to jump to a certain slice. However, when I do have an acquisition with off-diagonal elements in the direction matrix and apply “rotate to volume node”, the Slice Widget coordinates do not match the RAS coordinates anymore (see Red and Orange boxes in attached image), so I cannot use the RAS coordinates of the center of my object to choose the Red,Yellow,Green slice coordinate. Is there a way to know what would be the SlicerWidget coordinates used for a specific RAS or Voxel coordinate after applying “rotate to volume plane”? (I know how to find the IJKtoRAS correspondance, but I’m unsure how to relate that to the SliceWidget coordinate).</p>
<p>I have tried a bit of my own custom matrices and also tried sliceNode.GetXYToSlice or sliceNode.GetXYtoRAS but nothing seems to be giving me the right answer.</p>
<p>Perhaps there is already a function in Slicer that figures this out? Any help is much appreciated.</p>
<p>Best,<br>
Eric</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63effbb5ba1091a82a2d76dc797c9ccb28aefca5.jpeg" data-download-href="/uploads/short-url/eg5qJUv6rwOuXs7BWT8DMldnLF3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63effbb5ba1091a82a2d76dc797c9ccb28aefca5_2_689x425.jpeg" alt="image" data-base62-sha1="eg5qJUv6rwOuXs7BWT8DMldnLF3" width="689" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63effbb5ba1091a82a2d76dc797c9ccb28aefca5_2_689x425.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63effbb5ba1091a82a2d76dc797c9ccb28aefca5_2_1033x637.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63effbb5ba1091a82a2d76dc797c9ccb28aefca5.jpeg 2x" data-dominant-color="88878E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1194×736 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-11-03 16:51 UTC)

<p>You can use vtkMRMLSliceNode’s JumpSlice/JumpSliceByCentering/JumpSliceByOffsetting methods to show any RAS position in a slice. If you want to reimplement this method in your own module (I would not recommend it though) then you can take the implementation here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSliceNode.cxx#L1462-L1526" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSliceNode.cxx#L1462-L1526" target="_blank" rel="noopener">Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSliceNode.cxx#L1462-L1526</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="1462" style="counter-reset: li-counter 1461 ;">
<li>void vtkMRMLSliceNode::JumpSliceByCentering(double r, double a, double s)</li>
<li>{</li>
<li>  vtkMatrix4x4 *sliceToRAS = this-&gt;GetSliceToRAS();</li>
<li>  double sr = sliceToRAS-&gt;GetElement(0, 3);</li>
<li>  double sa = sliceToRAS-&gt;GetElement(1, 3);</li>
<li>  double ss = sliceToRAS-&gt;GetElement(2, 3);</li>
<li>
</li><li>  // deduce the slice spacing</li>
<li>  vtkMatrix4x4 *xyzToRAS = this-&gt;GetXYToRAS();</li>
<li>
</li><li>  double p1xyz[4] = {0.0,0.0,0.0,1.0};</li>
<li>  double p2xyz[4] = {0.0,0.0,1.0,1.0};</li>
<li>
</li><li>  double p1ras[4], p2ras[4];</li>
<li>
</li><li>  xyzToRAS-&gt;MultiplyPoint(p1xyz, p1ras);</li>
<li>  xyzToRAS-&gt;MultiplyPoint(p2xyz, p2ras);</li>
<li>
</li><li>  double sliceSpacing = sqrt(vtkMath::Distance2BetweenPoints(p2ras, p1ras));</li>
<li>
</li></ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSliceNode.cxx#L1462-L1526" target="_blank" rel="noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @EricM (2020-11-03 18:35 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Before, I was using <code>sliceWidgetLogic.SetSliceOffset(c)</code> to achieve this, but now with the following code, I can get it to work exactly how I want:</p>
<pre><code class="lang-auto">cYellow, cGreen, cRed = c #RAS coordinate
sliceWidgetColors = ['Yellow','Green','Red']

layoutManager = slicer.app.layoutManager()
for color in sliceWidgetColors:
  sliceWidget = layoutManager.sliceWidget(color)
  sliceWidgetLogic = sliceWidget.sliceLogic()
  sliceNode = sliceWidgetLogic.GetSliceNode()
  sliceNode.JumpSlice(cYellow,cGreen,cRed)
</code></pre>
<p>Thanks for the code too.</p>
<p>Best,<br>
Eric</p>

---
