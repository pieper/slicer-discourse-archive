---
topic_id: 43492
title: "Help With Landmark Placement Not Actually Placed On Ply Surf"
date: 2025-06-25
url: https://discourse.slicer.org/t/43492
---

# Help with Landmark placement: Not actually placed on PLY surface

**Topic ID**: 43492
**Date**: 2025-06-25
**URL**: https://discourse.slicer.org/t/help-with-landmark-placement-not-actually-placed-on-ply-surface/43492

---

## Post #1 by @jsguerra (2025-06-25 16:16 UTC)

<p>Hello! I was placing some landmarks on a PLY surface and noticed that when I place/reposition a landmark to my desired position (Fig. 2), the landmark is not actually touching the model surface (Fig. 2). Is this normal or am I doing something wrong?</p>
<p>I have the 3D Display placement settings as “snap to visible surface,” which I though meant that it would place the landmark on the surface. Am I misunderstanding this as well?</p>
<p><strong>Fig. 1</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75b0d2942f62a30be76fcca42a234bec3fecbca8.png" data-download-href="/uploads/short-url/gN8HGI37VUWIwJCBxqmqB2FZIq4.png?dl=1" title="slicer_landmark placement_center view_zoomed" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75b0d2942f62a30be76fcca42a234bec3fecbca8_2_290x249.png" alt="slicer_landmark placement_center view_zoomed" data-base62-sha1="gN8HGI37VUWIwJCBxqmqB2FZIq4" width="290" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75b0d2942f62a30be76fcca42a234bec3fecbca8_2_290x249.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75b0d2942f62a30be76fcca42a234bec3fecbca8_2_435x373.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75b0d2942f62a30be76fcca42a234bec3fecbca8_2_580x498.png 2x" data-dominant-color="838333"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_landmark placement_center view_zoomed</span><span class="informations">2145×1845 285 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Fig. 2</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fdc47d4ebd5746517a24ec1ee78aeabb27cd1db5.png" data-download-href="/uploads/short-url/AcVMa0UjxuL7H2SbtiaRqRJVGvz.png?dl=1" title="slicer_landmark placement_center view_zoomed_diff viewpoint" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdc47d4ebd5746517a24ec1ee78aeabb27cd1db5_2_290x249.png" alt="slicer_landmark placement_center view_zoomed_diff viewpoint" data-base62-sha1="AcVMa0UjxuL7H2SbtiaRqRJVGvz" width="290" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdc47d4ebd5746517a24ec1ee78aeabb27cd1db5_2_290x249.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdc47d4ebd5746517a24ec1ee78aeabb27cd1db5_2_435x373.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdc47d4ebd5746517a24ec1ee78aeabb27cd1db5_2_580x498.png 2x" data-dominant-color="999C9A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_landmark placement_center view_zoomed_diff viewpoint</span><span class="informations">2145×1845 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-06-25 16:22 UTC)

<p>We would need the data to replicate.</p>
<p>One possibility is that you have single vertex that’s floating in space and too small to see (though from your close up I don’t think that’s the case). Regardless, run the model through the Surface Toolbox with <strong>extract largest component option</strong>  enabled, and retry with the new model.</p>
<p>If it doesn’t work, share your model and let us know what platform you are using Slicer and the release number.</p>

---

## Post #3 by @jsguerra (2025-06-25 16:46 UTC)

<p>I ran the model through the Surface Toolbox as suggested and it improved the placement (Fig. 1 &amp; 2) but when I choose to “Refocus camera on point” and Zoom in further, I still get a floating point (Fig. 3).</p>
<p><strong>Fig. 1</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be107c46c463e4ce38d1589a025406b5e5394f89.png" data-download-href="/uploads/short-url/r7o2r6wBTKBa1nGxeBRkm9th3QZ.png?dl=1" title="slicer_landmark placement_center view_extracted" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be107c46c463e4ce38d1589a025406b5e5394f89_2_581x499.png" alt="slicer_landmark placement_center view_extracted" data-base62-sha1="r7o2r6wBTKBa1nGxeBRkm9th3QZ" width="581" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be107c46c463e4ce38d1589a025406b5e5394f89_2_581x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be107c46c463e4ce38d1589a025406b5e5394f89_2_871x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be107c46c463e4ce38d1589a025406b5e5394f89_2_1162x998.png 2x" data-dominant-color="88893C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_landmark placement_center view_extracted</span><span class="informations">2145×1845 470 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<strong>Fig. 2</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4be633a4cc9cb19fb775e8c0419c8dd048297582.png" data-download-href="/uploads/short-url/aPr0Ww1zboIzyAclQJtgVs9iMBc.png?dl=1" title="slicer_landmark placement_extracted_center view_zoomed_diff viewpoint" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4be633a4cc9cb19fb775e8c0419c8dd048297582_2_581x499.png" alt="slicer_landmark placement_extracted_center view_zoomed_diff viewpoint" data-base62-sha1="aPr0Ww1zboIzyAclQJtgVs9iMBc" width="581" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4be633a4cc9cb19fb775e8c0419c8dd048297582_2_581x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4be633a4cc9cb19fb775e8c0419c8dd048297582_2_871x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4be633a4cc9cb19fb775e8c0419c8dd048297582_2_1162x998.png 2x" data-dominant-color="A3A58A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_landmark placement_extracted_center view_zoomed_diff viewpoint</span><span class="informations">2145×1845 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<strong>Fig. 3</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ecef5c2414b21a2fca8e55d5b5ad6719f1ef223.png" data-download-href="/uploads/short-url/2705QBNtOqeGnpo3khKU2nubWtd.png?dl=1" title="slicer_landmark placement_extracted_refocus on point_zoomed_diff viewpoint" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ecef5c2414b21a2fca8e55d5b5ad6719f1ef223_2_581x499.png" alt="slicer_landmark placement_extracted_refocus on point_zoomed_diff viewpoint" data-base62-sha1="2705QBNtOqeGnpo3khKU2nubWtd" width="581" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ecef5c2414b21a2fca8e55d5b5ad6719f1ef223_2_581x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ecef5c2414b21a2fca8e55d5b5ad6719f1ef223_2_871x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ecef5c2414b21a2fca8e55d5b5ad6719f1ef223_2_1162x998.png 2x" data-dominant-color="959786"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_landmark placement_extracted_refocus on point_zoomed_diff viewpoint</span><span class="informations">2145×1845 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Happy to share the original PLY file but it won’t let me upload it here. I’m using Slicer 5.6.2 on Windows.</p>

---

## Post #4 by @muratmaga (2025-06-25 17:23 UTC)

<aside class="quote no-group" data-username="jsguerra" data-post="3" data-topic="43492">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jsguerra/48/80468_2.png" class="avatar"> jsguerra:</div>
<blockquote>
<p>Happy to share the original PLY file but it won’t let me upload it here. I’m using Slicer 5.6.2 on Windows.</p>
</blockquote>
</aside>
<p>yes, you need to put somewhere on the cloud (e.g., google drive, one drive), share it publicly and provide the link here.</p>

---

## Post #5 by @jsguerra (2025-06-25 17:28 UTC)

<p>Of course <img src="https://emoji.discourse-cdn.com/twitter/man_facepalming.png?v=14" title=":man_facepalming:" class="emoji" alt=":man_facepalming:" loading="lazy" width="20" height="20"></p>
<p>Here you go:  <a href="https://drive.google.com/drive/folders/11np3tTsxFZIx8pq5QtnxAdy0Wb4hYHRU?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">Slicer Support - Landmarks - Google Drive</a></p>

---

## Post #6 by @muratmaga (2025-06-25 17:45 UTC)

<p>I can’t replicate this with my Mac on a recent preview. It picks always on the model.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2671402c4c46d60a74728672a9eb0d340e9ad2d.png" data-download-href="/uploads/short-url/yAooi5JLPST4lhxacAJY1U3iHDL.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2671402c4c46d60a74728672a9eb0d340e9ad2d.png" alt="image" data-base62-sha1="yAooi5JLPST4lhxacAJY1U3iHDL" width="445" height="500" data-dominant-color="ACAD65"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">530×595 38 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The only I time I can sort of see this, if I zoom in unrealistically close like this, which I think the rendering breaks down. I don’t even see the scale anymore, if displayed it would be at scale of nanometers for this data. I wouldn’t worry about this…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d0291f2e42523a0e714dc84780d3f3c6c4d477e.png" data-download-href="/uploads/short-url/48DlTfHZGKMvIWGuDohE82fGy2q.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d0291f2e42523a0e714dc84780d3f3c6c4d477e_2_561x499.png" alt="image" data-base62-sha1="48DlTfHZGKMvIWGuDohE82fGy2q" width="561" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d0291f2e42523a0e714dc84780d3f3c6c4d477e_2_561x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d0291f2e42523a0e714dc84780d3f3c6c4d477e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d0291f2e42523a0e714dc84780d3f3c6c4d477e.png 2x" data-dominant-color="B6B667"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">835×744 68.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My suggestion, try with the latest preview on your window. You 5.6.2 is now deprecated.</p>

---

## Post #7 by @jsguerra (2025-06-25 19:10 UTC)

<p>Interesting… Did you run the model through Surface Toolbox or run the original?</p>
<p>I updated to Slicer 5.9.0, extracted the surface with Surface Toolbox  and tried landmarking again. I added the scale to compare to your images and I’m getting the floating issue at around wider zoom of 100um.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffc7a6b9e0c8c9c7e2a5302cb7ead3d5f1b2ce28.jpeg" data-download-href="/uploads/short-url/AuJvmtdyJv4T6akOjQfLNmMZPKw.jpeg?dl=1" title="slicer590_landmark placement_extracted_zoom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffc7a6b9e0c8c9c7e2a5302cb7ead3d5f1b2ce28_2_473x375.jpeg" alt="slicer590_landmark placement_extracted_zoom" data-base62-sha1="AuJvmtdyJv4T6akOjQfLNmMZPKw" width="473" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffc7a6b9e0c8c9c7e2a5302cb7ead3d5f1b2ce28_2_473x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffc7a6b9e0c8c9c7e2a5302cb7ead3d5f1b2ce28_2_709x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffc7a6b9e0c8c9c7e2a5302cb7ead3d5f1b2ce28_2_946x750.jpeg 2x" data-dominant-color="A6A998"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer590_landmark placement_extracted_zoom</span><span class="informations">1920×1520 39.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I then repositioned the landmark and it looked like it was on the surface but when I zoom to around 25um, I have a floating point again.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d7f3a6d89b44547c852d700053667a067e36fb3.jpeg" data-download-href="/uploads/short-url/kbJUkx2as8Lj0BvJgkjmbbcmeoX.jpeg?dl=1" title="slicer590_landmark placement_extracted_zoom_reposition" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d7f3a6d89b44547c852d700053667a067e36fb3_2_473x375.jpeg" alt="slicer590_landmark placement_extracted_zoom_reposition" data-base62-sha1="kbJUkx2as8Lj0BvJgkjmbbcmeoX" width="473" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d7f3a6d89b44547c852d700053667a067e36fb3_2_473x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d7f3a6d89b44547c852d700053667a067e36fb3_2_709x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d7f3a6d89b44547c852d700053667a067e36fb3_2_946x750.jpeg 2x" data-dominant-color="A3A45C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer590_landmark placement_extracted_zoom_reposition</span><span class="informations">1920×1520 51.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried this with the original as well. I followed the same procedure: placed landmark initially and then zoomed to adjust the placement and I get a very similar result.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/831d194750be900c4cc86bc2938fb272e908182c.jpeg" data-download-href="/uploads/short-url/iHSTkocNipmSRv5ehQcSmNxvGJC.jpeg?dl=1" title="slicer590_landmark placement_original_zoom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/831d194750be900c4cc86bc2938fb272e908182c_2_473x375.jpeg" alt="slicer590_landmark placement_original_zoom" data-base62-sha1="iHSTkocNipmSRv5ehQcSmNxvGJC" width="473" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/831d194750be900c4cc86bc2938fb272e908182c_2_473x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/831d194750be900c4cc86bc2938fb272e908182c_2_709x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/831d194750be900c4cc86bc2938fb272e908182c_2_946x750.jpeg 2x" data-dominant-color="A3A45C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer590_landmark placement_original_zoom</span><span class="informations">1920×1520 51.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could this be an issue on Windows, just my computer, or my landmarking? Realistically, would this discrepancy affect a 3DGM analysis or ALPACA?</p>

---

## Post #8 by @muratmaga (2025-06-25 19:28 UTC)

<aside class="quote no-group" data-username="jsguerra" data-post="7" data-topic="43492">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jsguerra/48/80468_2.png" class="avatar"> jsguerra:</div>
<blockquote>
<p>Interesting… Did you run the model through Surface Toolbox or run the original?</p>
</blockquote>
</aside>
<p>I used the model as is.</p>
<aside class="quote no-group" data-username="jsguerra" data-post="7" data-topic="43492">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jsguerra/48/80468_2.png" class="avatar"> jsguerra:</div>
<blockquote>
<p>Could this be an issue on Windows, just my computer, or my landmarking? Realistically, would this discrepancy affect a 3DGM analysis or ALPACA?</p>
</blockquote>
</aside>
<p>If you put the point manually on the model via markups, it should snap to the surface. However, any downstream modification (manully repositioning it) may modify it. To me it still looks like maybe a camera and rendering issue at the close range, but someone more familiar with that needs to comment on</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> any thoughts?</p>

---

## Post #9 by @lassoan (2025-06-26 15:48 UTC)

<p>We use <a href="https://vtk.org/doc/nightly/html/classvtkCellPicker.html">vtkCellPicker</a> with <a href="https://github.com/Slicer/Slicer/blob/ebdd8127bbffa9ae01c1d37eaadd24ad0cff0fef/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidgetRepresentation3D.cxx#L202-L203">tolerance set to 0.005</a> to find point on a visible surface (the tolerance allows picking a triangle if the picking line just misses the edge of a cell). This tolerance value is scaled with the window size internally, so it is hard to tell what physical distance from surface this tolerance can lead to, but I can confirm that reducing the tolerance from 0.005 to 0.00005 made the point more accurately snap to the surface (I could not zoom in enough the view to see the separation from surface anymore).</p>
<p>If this tolerance value is too high for your application (e.g., because you work with microscopic structures and your entire model’s physical size is just a few tenth of a millimeter) then you can rescale your model (using Transforms module) and adjust the length unit in the scene accordingly. However, implementation of custom unit is not fully complete (see known limitations <a href="https://github.com/Slicer/Slicer/issues/5040">here</a>), so it may be better to just rescale your model, leave the length unit unchanged, and note that you need to divide the displayed values by 10/100/1000 to get the correct physical values.</p>
<p>Alternatively, we could change this tolerance value in Slicer. Probably it would not cause perceivable difference in speed or quality of the pick, but below a certain tolerance value, numerical inaccuracies may cause picking failures. So, we would need to spend some time with testing before we reduce the tolerance value. I’ve added an issue to track this:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8512">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8512" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8512" target="_blank" rel="noopener">Markup point be slightly separated from the surface it was snapped to</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-06-26" data-time="14:07:53" data-timezone="UTC">02:07PM - 26 Jun 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

When zooming in a 3D view then markup point dropped on a surface may<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> appear at a distance of about a few micrometer from the surface.

## Steps to reproduce

See https://discourse.slicer.org/t/help-with-landmark-placement-not-actually-placed-on-ply-surface/43492/8

## Environment
- Slicer version: Slicer-5.9.1-2025-06-18
- Operating system: all</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @muratmaga (2025-06-26 15:54 UTC)

<aside class="quote no-group" data-username="jsguerra" data-post="7" data-topic="43492">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jsguerra/48/80468_2.png" class="avatar"> jsguerra:</div>
<blockquote>
<p>Realistically, would this discrepancy affect a 3DGM analysis or ALPACA?</p>
</blockquote>
</aside>
<p>Sorry, I missed this question. Answer is a solid NO. You (as the individual) would be making far larger error than 25 micron, when you try to pick the same spot on the same model at a different day. Hence this technical error is likely far smaller than your individual error, and you don’t need to be concerned about it.</p>

---
