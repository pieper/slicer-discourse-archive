# `CreateClosedSurfaceRepresentation()` does not work when closing a segmentation surfaces

**Topic ID**: 24617
**Date**: 2022-08-03
**URL**: https://discourse.slicer.org/t/createclosedsurfacerepresentation-does-not-work-when-closing-a-segmentation-surfaces/24617

---

## Post #1 by @jumbojing (2022-08-03 13:43 UTC)

<p>I want to convert a model to a segmentation and close the surface, but using <code>CreateClosedSurfaceRepresentation()</code> doesn’t work, what’s wrong?</p>
<pre><code class="lang-python">seg = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
seg.SetReferenceImageGeometryParameterFromVolumeNode(Vol)
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(model, seg)
seg.CreateClosedSurfaceRepresentation()
</code></pre>
<p>(<a href="https://drive.google.com/file/d/1mAKBc3qNRiLrMZF_S4_T8gWI6hMlAbZS/view?usp=sharing" rel="noopener nofollow ugc">the MRBfile link</a>…)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/152dc10857efdeeec2b48d6a051bc28b42ce9e22.jpeg" data-download-href="/uploads/short-url/31m3nhAlRQa1zkmfBDu2Aivcizg.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/152dc10857efdeeec2b48d6a051bc28b42ce9e22_2_690x385.jpeg" alt="image" data-base62-sha1="31m3nhAlRQa1zkmfBDu2Aivcizg" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/152dc10857efdeeec2b48d6a051bc28b42ce9e22_2_690x385.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/152dc10857efdeeec2b48d6a051bc28b42ce9e22_2_1035x577.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/152dc10857efdeeec2b48d6a051bc28b42ce9e22.jpeg 2x" data-dominant-color="D3D4D2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1298×726 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, I can achieve the goal by pressing the 'make master` button in the module of segmentation…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c48d7a609ca0a176429cb2f3dfa4d1b7074da90e.jpeg" data-download-href="/uploads/short-url/s2MHmTiVtOlGUM7p6NPCoazTYN8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c48d7a609ca0a176429cb2f3dfa4d1b7074da90e_2_690x360.jpeg" alt="image" data-base62-sha1="s2MHmTiVtOlGUM7p6NPCoazTYN8" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c48d7a609ca0a176429cb2f3dfa4d1b7074da90e_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c48d7a609ca0a176429cb2f3dfa4d1b7074da90e_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c48d7a609ca0a176429cb2f3dfa4d1b7074da90e.jpeg 2x" data-dominant-color="D6D7D5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1294×676 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2022-08-03 15:04 UTC)

<p>If the original representation for the segments will be model nodes, then you can set the master representation to closed surface.</p>
<pre><code class="lang-auto">seg = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
seg.SetReferenceImageGeometryParameterFromVolumeNode(Vol)
seg.SetMasterRepresentationToClosedSurface()
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(model, seg)
</code></pre>

---

## Post #3 by @jumbojing (2022-08-03 19:33 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="2" data-topic="24617">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p><code>seg.SetMasterRepresentationToClosedSurface()</code></p>
</blockquote>
</aside>
<p>Thank <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> !<br>
I used <code>seg.SetMasterRepresentationToClosedSurface()</code> to get the following seg. Why is the dyeing area of green slices different from that of other slices?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f3a28381395036ae4198436082ead673bb7df1a.png" data-download-href="/uploads/short-url/dApXyZJrmPqWmiLsqh6gH0a1KFs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f3a28381395036ae4198436082ead673bb7df1a_2_608x500.png" alt="image" data-base62-sha1="dApXyZJrmPqWmiLsqh6gH0a1KFs" width="608" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f3a28381395036ae4198436082ead673bb7df1a_2_608x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f3a28381395036ae4198436082ead673bb7df1a_2_912x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f3a28381395036ae4198436082ead673bb7df1a_2_1216x1000.png 2x" data-dominant-color="303034"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1698×1396 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Sunderlandkyl (2022-08-03 19:38 UTC)

<p>Probably the slicing of the surface along the coronal plane isn’t able to correctly distinguish between the inside/outside of the model.</p>
<p>It looks like your surface mesh is not actually a closed surface. Displaying the segmentation in 2D and converting it to a labelmap representation is likely going to have unexpected results since the algorithms cannot determine what is “inside” vs what is “outside”,</p>

---

## Post #5 by @jumbojing (2022-08-03 19:41 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> How to close the surface?Or tell the algorithms I want “inside” instead of “outside”???</p>

---

## Post #6 by @Sunderlandkyl (2022-08-03 19:44 UTC)

<p>I’m not sure if there is a easy solution to the problem of converting an open surface to a closed one.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> do you know of an approach that might work?</p>

---

## Post #7 by @lassoan (2022-08-04 06:46 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="6" data-topic="24617">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>I’m not sure if there is a easy solution to the problem of converting an open surface to a closed one.</p>
</blockquote>
</aside>
<p>It is impossible to solve this problem automatically. It is better to generate a closed surface when the surface is created (e.g., enable capping when cutting the surface).</p>

---
