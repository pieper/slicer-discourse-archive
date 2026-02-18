# Apply a linear transformation to a segmentation

**Topic ID**: 16365
**Date**: 2021-03-04
**URL**: https://discourse.slicer.org/t/apply-a-linear-transformation-to-a-segmentation/16365

---

## Post #1 by @michela.destito (2021-03-04 16:21 UTC)

<p>Hi, I have a question. I would like to apply a linear transformation to a segmentation via command line and always save it as a segmentation, so I don’t want to refer it to any volume. it’s possible?<br>
Thank you very much.<br>
Michela</p>

---

## Post #2 by @lassoan (2021-03-04 17:22 UTC)

<p>You can apply a transform to the segmentation node using <a href="http://apidocs.slicer.org/master/classvtkMRMLTransformableNode.html#a08a8e77fdd0601c29fc321087e562d4f">SetAndObserveTransformNodeID(nodeID)</a> followed by <a href="http://apidocs.slicer.org/master/classvtkMRMLTransformableNode.html#a1e1b5b0059e2eea22224b243492bdc5c">HardenTransform()</a>.</p>
<p>Note that linear transforms are applied without making any changes to the voxel array, just by simply updating the physical&lt;-&gt;voxel coordinate system mapping.</p>
<p>If you want to make changes to the voxel array then you do need to specify a reference geometry. For a complete example of doing data augmentation, including random warping transformation, look at this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Apply_random_deformations_to_image">example in the script repository</a>.</p>

---

## Post #3 by @jmhuie (2021-03-31 15:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16365">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Note that linear transforms are applied without making any changes to the voxel array, just by simply updating the physical&lt;-&gt;voxel coordinate system mapping.</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, I have a related question about this. I am currently running into an issue with my second moment of area module (as well as the segment cross-sectional area module). I want to apply a linear transformation to a segmentation node in case the initial volume was CT scanned at an oblique angle. This way, any slice geometries are calculated along an anatomically relevant axis. Although, when I input a transformed segmentation node (hardened or not hardened, doesn’t matter), it still calculates CSA along the original oblique axes. However, when I input a reference volume node then it works and CSA is calculated with the transformation in effect.</p>
<p>Why is that? Is there any way to make this work without a volume node and/or is re-slicing my only option? The reason I am trying to do this is because I’m interested in importing models into Slicer from elsewhere, converting them to segmentation nodes, and calculating slice geometries. These models may come at an oblique angle and without a reference volume.</p>
<p>Any help would be appreciated. Thanks!</p>

---

## Post #4 by @lassoan (2021-04-03 02:03 UTC)

<aside class="quote no-group" data-username="jmhuie" data-post="3" data-topic="16365">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jmhuie/48/7086_2.png" class="avatar"> jmhuie:</div>
<blockquote>
<p>Although, when I input a transformed segmentation node (hardened or not hardened, doesn’t matter), it still calculates CSA along the original oblique axes. However, when I input a reference volume node then it works and CSA is calculated with the transformation in effect.</p>
</blockquote>
</aside>
<p>Resampling of a volume is a lossy operation, therefore it is only performed if it is absolutely necessary. Since a linear transform can be applied to a volume by simply changing the origin, spacing, and axis directions of the voxel grid, there is no need to change the voxel array.</p>
<p>Of course, in your case, the goal is resampling, so you need to use one of the resampling modules (or Crop volume module).</p>
<p>You need to generate the reference volume yourself or use “Resample scalar/vector/DWI volume” module, in which you can specify the output geometry (origin, spacing, axis directions, and extents). Alternatively, you can use Crop volume module - in that case you need to create a ROI node and specify spacing. Use the new Markups ROI node, as you can specify axis directions directly there, and not just via a transform node (and the old Annotation ROI will go away at some point anyway).</p>

---
