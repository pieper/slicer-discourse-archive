# Transform Module

**Topic ID**: 18667
**Date**: 2021-07-13
**URL**: https://discourse.slicer.org/t/transform-module/18667

---

## Post #1 by @reddington.15 (2021-07-13 15:17 UTC)

<p>Hello,</p>
<p>In a brief synopsis I am trying to calculate the deformation of the pelvis from a pre and post CT scan after impact testing. Once I segment both pelvis bones out using segmentation editor and wrap solidfy, I align the segments using fiducial registration by placing points on each segment and then transform. I also then use segmentation registration, which gives me more transformation matrices. I just want to make sure I am understanding the matrices I am obtaining correctly. When I align with fiducial registration and then transform is that matrix the path of the points on the post to align with the pre? Then segmentation registration is the deformation between the segments once overlapped and that deformation is calculated in the deformable matrix or the affine matrix? I hope this makes sense and that I have given you enough information, but if not I am happy to add clarification.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2021-07-13 18:37 UTC)

<p>It is not necessary to use both the point based registration and segment registration - one should be enough.</p>
<aside class="quote no-group" data-username="reddington.15" data-post="1" data-topic="18667">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/34f0e0/48.png" class="avatar"> reddington.15:</div>
<blockquote>
<p>When I align with fiducial registration and then transform is that matrix the path of the points on the post to align with the pre?</p>
</blockquote>
</aside>
<p>The transform moves the “From” (or “Moving”) object to the “To” (or “Fixed”) object.</p>
<aside class="quote no-group" data-username="reddington.15" data-post="1" data-topic="18667">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/34f0e0/48.png" class="avatar"> reddington.15:</div>
<blockquote>
<p>Then segmentation registration is the deformation between the segments once overlapped and that deformation is calculated in the deformable matrix or the affine matrix?</p>
</blockquote>
</aside>
<p>You can choose to compute rigid, affine, or deformable matrix. The deformable transform is always applied on top of a linear bulk transform (otherwise the matrix inverse computation would much less stable).</p>

---

## Post #3 by @reddington.15 (2021-07-19 03:24 UTC)

<p>Okay, that sort of makes sense. Is there a reason why the compute rigid, affine, or deformable matrix are slightly different in value?</p>

---

## Post #4 by @lassoan (2021-07-19 11:44 UTC)

<p>The transforms are different in what displacements they can describe.</p>
<ul>
<li>Rigid = translation + rotation.</li>
<li>Affine = translation + rotation + shear.</li>
<li>Deformable: any smoothly changing displacement field.</li>
</ul>
<p>For bones, you usually rigid transform (if you register multiple bones then piecewise rigid) is the most suitable, unless they are warped.</p>

---
