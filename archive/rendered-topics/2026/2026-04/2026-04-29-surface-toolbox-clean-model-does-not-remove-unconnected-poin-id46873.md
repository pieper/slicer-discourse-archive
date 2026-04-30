---
topic_id: 46873
title: "Surface Toolbox Clean Model Does Not Remove Unconnected Poin"
date: 2026-04-29
url: https://discourse.slicer.org/t/46873
---

# Surface Toolbox Clean model does not remove unconnected points

**Topic ID**: 46873
**Date**: 2026-04-29
**URL**: https://discourse.slicer.org/t/surface-toolbox-clean-model-does-not-remove-unconnected-points/46873

---

## Post #1 by @mikebind (2026-04-29 20:44 UTC)

<p>I have a model which has points which are not part of any triangles.  When I use vtkImplicitPolyDataDistance filters, distances to these points can come back as always negative, which is supposed to indicate that the probed location is inside the model, which can trigger breach warnings for tracked tools, or, more generally, just report a very wrong distance to the closest point on a model surface. My understanding is that the SurfaceToolbox module’s “Clean” function should clean up (remove) any orphan points which are not part of any cells or edges, but when I apply “Clean”, the output model still has these floating points.  If I extract the largest connected component (another SurfaceToolbox tool), these points are removed from the output model.  So, as long as the models I’m working with have exactly one connected component, I can use that workaround, but, obviously that will fail if there were multiple components one wanted to keep within a single model node.</p>
<p>Expected Behavior: SurfaceToolbox “Clean” should remove disconnected points from a model node’s points list.</p>
<p>Actual Behavior: Applying “Clean” to at least some models does not remove all disconnected points.</p>
<p>Here is an example model this fails for <a href="https://drive.google.com/file/d/13kp2FlJRglsBGmNNJ6zkBYcYtet_0dfG/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/13kp2FlJRglsBGmNNJ6zkBYcYtet_0dfG/view?usp=sharing</a></p>
<p>The origin of the model is a segmentation segment which has been decimated to reduce the point count. Applying “Clean” leaves floating points which report negative distances, while applying “Extract largest component” removes those points.</p>
<p>This is a helper function for visualization: <a href="https://drive.google.com/file/d/1dkcnqQ95c4gwtBI06V8zg5uufnHtXX43/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1dkcnqQ95c4gwtBI06V8zg5uufnHtXX43/view?usp=sharing</a><br>
It creates grids of points on the faces of the bounding box of the model node and shows connections to the closest point on the model, with red connections indicating negative distances reported.  Since all the sampled points are outside the bounding box, there should never be any red connections for a closed model with properly oriented triangles and no extraneous points. However, you will see multiple of these for the given model.  Furthermore, you will see that the red connections end at a point which is not on the model surface, but instead at a disconnected point location.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81e2f2f16e52f04e9346e9d4ad4823045d0dee87.jpeg" data-download-href="/uploads/short-url/ix1PrfFjgA3Z1oZk0jio0gmm5bp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81e2f2f16e52f04e9346e9d4ad4823045d0dee87.jpeg" alt="image" data-base62-sha1="ix1PrfFjgA3Z1oZk0jio0gmm5bp" width="690" height="439" data-dominant-color="818F9F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">721×459 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Slicer version 5.10.0 on Windows 11.</p>
<p>The documentation for SurfaceToolbox says that “Clean” should remove unused points, so I think this represents a bug.</p>

---
