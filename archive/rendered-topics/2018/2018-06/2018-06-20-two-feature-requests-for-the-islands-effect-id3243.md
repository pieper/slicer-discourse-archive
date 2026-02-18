# Two feature requests for the Islands effect

**Topic ID**: 3243
**Date**: 2018-06-20
**URL**: https://discourse.slicer.org/t/two-feature-requests-for-the-islands-effect/3243

---

## Post #1 by @Fernando (2018-06-20 11:45 UTC)

<p>Hi all,</p>
<p>I’m working on brain vessels segmentation. I need manually annotated data from clinicians, so I wrote a module that uses some effects from the Segment Editor. Their current pipeline for segmentation is:</p>
<ol>
<li>MITK: Intensity threshold of the vessels image and surface generation</li>
<li>MeshLab: mesh cleaning by removing small (diameter) islands and manually selected ones</li>
</ol>
<p>My Slicer module is very similar, but works on a <code>Segmentation</code> node with label map as master representation. I use <code>Remove small islands</code> and the <code>Scissors</code> effect, but my feature requests are:</p>
<ol>
<li>Being able to remove an island by clicking on it in the 3D view. I guess this shouldn’t be too hard since one can already move the 2D crosshair by placing the mouse on the 3D mesh and pressing Shift</li>
<li>Add an option to use islands diameters (longest distance between points on the surface) instead of number of voxels for the <code>Remove small islands</code>. This one might be harder, I don’t know whether that filter is available on VTK.</li>
</ol>
<p>An elongated, thin island (long diameter, small volume) is more likely to be a vessel than a spherical island (small diameter, high volume). That’s why this difference is important for my case.</p>

---

## Post #2 by @lassoan (2018-06-20 14:18 UTC)

<aside class="quote no-group quote-modified" data-username="Fernando" data-post="1" data-topic="3243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>Being able to remove an islands by clicking on it in the 3D view. I guess this shouldn’t be too hard since one can already move the 2D crosshair by placing the mouse on the 3D mesh and pressing Shift</p>
</blockquote>
</aside>
<p>This would be nice. The complication in 3D views is that when you pick a point position in 3D view, it is always at the boundary of a segments, so you need to analyze what is around that position and look around, maybe move a bit farther along the viewing ray until you find a non-empty voxel and use that position. Should not be too difficult, it’s just not completely trivial. Getting 3D position from a click position is already available in qSlicerSegmentEditorPaintEffectPrivate::brushPositionInWorld - this method could be moved to the common segment editor effect base class so that all effects can access it; everything else could be implemented in the Islands effect in Python. <a class="mention" href="/u/fernando">@Fernando</a>  Would you be interested in trying to implement this?</p>
<aside class="quote no-group" data-username="Fernando" data-post="1" data-topic="3243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>Add an option to use islands diameters (longest distance between points on the surface)</p>
</blockquote>
</aside>
<p>This metric is quite special and not easy or fast to compute. I would recommend to use bounding box shape or first moment to perform some filtering based on the island shape. This could be implemented as an additional filtering step after small islands have been removed, in Islands effect. <a class="mention" href="/u/fernando">@Fernando</a> We don’t know how useful this shape-based filtering would be (maybe it will be often useful, maybe not), so the best would be if you could implement a prototype, play with different shape characterization options, etc., and if you find something that seems to work well then we can integrate it in the Slicer core. We can help you with any specific problems.</p>

---

## Post #3 by @Fernando (2018-06-20 14:32 UTC)

<p>Ok, thanks Andras. I’ll try to make some time to look into it if clinicians think it would be very useful.</p>

---
