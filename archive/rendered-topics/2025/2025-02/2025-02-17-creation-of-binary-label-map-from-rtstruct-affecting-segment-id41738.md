---
topic_id: 41738
title: "Creation Of Binary Label Map From Rtstruct Affecting Segment"
date: 2025-02-17
url: https://discourse.slicer.org/t/41738
---

# Creation of binary label map from RTSTRUCT affecting segmentations

**Topic ID**: 41738
**Date**: 2025-02-17
**URL**: https://discourse.slicer.org/t/creation-of-binary-label-map-from-rtstruct-affecting-segmentations/41738

---

## Post #1 by @yasmin.mcquinlan (2025-02-17 12:18 UTC)

<p>On import of RTSTRUCT into Segmentation Editor, I am asked to convert to a binary label map from a Planar contour. But on doing so, the segmentations have undesirable artefacts that weren’t present previously (see below).</p>
<p>I have a lot of RTSTRUCT files that need working on!</p>
<p>Is there a workaround for this?</p>
<p>Error message:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7f20cd7fcae9e169e38b9dec336a19da95fd9ac.png" data-download-href="/uploads/short-url/znqwzfGgS3zY4rSSTXvmWld9PXK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7f20cd7fcae9e169e38b9dec336a19da95fd9ac.png" alt="image" data-base62-sha1="znqwzfGgS3zY4rSSTXvmWld9PXK" width="502" height="130"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">502×130 5.71 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Undesirable artefacts:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38f3f62eb4c93fed4ed415aeb93446e1c85f665c.jpeg" data-download-href="/uploads/short-url/87PqgYgLBHphlz3q7yH3bPb7Upm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38f3f62eb4c93fed4ed415aeb93446e1c85f665c_2_533x500.jpeg" alt="image" data-base62-sha1="87PqgYgLBHphlz3q7yH3bPb7Upm" width="533" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38f3f62eb4c93fed4ed415aeb93446e1c85f665c_2_533x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38f3f62eb4c93fed4ed415aeb93446e1c85f665c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38f3f62eb4c93fed4ed415aeb93446e1c85f665c.jpeg 2x" data-dominant-color="647985"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">771×722 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2025-02-17 12:39 UTC)

<aside class="quote no-group" data-username="yasmin.mcquinlan" data-post="1" data-topic="41738">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/9fc29f/48.png" class="avatar"> yasmin.mcquinlan:</div>
<blockquote>
<p>On import of RTSTRUCT into Segmentation Editor, I am asked to convert to a binary label map from a Planar contour.</p>
</blockquote>
</aside>
<p>OK so this is not an error message, just a confirmation that you will “lose” the original planar contours, because the source representation needs to be changed from the original “gold standard” contour set to the binary labelmap, because Segment Editor can only work on labelmaps.</p>
<p>The artifacts you see are probably due to issues during the triangulation process. The basics of the segmentation representations are explained in the documentation:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a></p>
<p>You can read more about how all this works in (and why) in this paper:</p>
<p>Pinter, C., Lasso, A., &amp; Fichtinger, G. (2019). Polymorph segmentation representation for medical image computing. Computer Methods and Programs in Biomedicine, 171, 19–26. <a href="https://doi.org/10.1016/j.cmpb.2019.02.011" class="inline-onebox">Redirecting</a></p>
<p>(Full text: <a href="https://labs.cs.queensu.ca/perklab/wp-content/uploads/sites/3/2024/02/Pinter2019_Manuscript.pdf">https://labs.cs.queensu.ca/perklab/wp-content/uploads/sites/3/2024/02/Pinter2019_Manuscript.pdf</a>)</p>
<p>The only way currently to prevent such artifacts is by changing the “conversion path” and working around the triangulation by falling back to the “ribbon” method. The disadvantage is that you will lose the interpolation along the sparse axis (IS, perpendicular to axial). You can do this in the Segmentations in the Representations section.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c27759d89d29ae648ce995c0b5d482282c0d759b.png" data-download-href="/uploads/short-url/rKkkVr93074NkdCndAx3nxa8pQv.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c27759d89d29ae648ce995c0b5d482282c0d759b_2_386x500.png" alt="image" data-base62-sha1="rKkkVr93074NkdCndAx3nxa8pQv" width="386" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c27759d89d29ae648ce995c0b5d482282c0d759b_2_386x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c27759d89d29ae648ce995c0b5d482282c0d759b_2_579x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c27759d89d29ae648ce995c0b5d482282c0d759b.png 2x" data-dominant-color="EBEFF4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">633×819 38.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef82904a451649f4f734dde4cb14052ebb7d2568.png" data-download-href="/uploads/short-url/yaNQuPP3CmYUT9UizdnOgcOkwg8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef82904a451649f4f734dde4cb14052ebb7d2568.png" alt="image" data-base62-sha1="yaNQuPP3CmYUT9UizdnOgcOkwg8" width="509" height="443"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">509×443 12.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
