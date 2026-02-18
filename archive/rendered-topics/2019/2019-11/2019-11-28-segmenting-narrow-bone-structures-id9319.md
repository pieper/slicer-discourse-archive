# Segmenting narrow bone structures

**Topic ID**: 9319
**Date**: 2019-11-28
**URL**: https://discourse.slicer.org/t/segmenting-narrow-bone-structures/9319

---

## Post #1 by @Umesh_Persad (2019-11-28 09:59 UTC)

<p>I am trying to segment out a scapula which has some pretty narrow sections. I tried the “Grow from Seeds” effect, but it doesn’t seem to work very well to capture the thin long cross sections. Is there a better method or is the best way to just use a threshold mask and then go in and paint through it manually?</p>

---

## Post #2 by @lassoan (2019-11-28 12:22 UTC)

<p>Can you post a few screenshots, and preferably also a download link to a typical data set, so that we can see what the problems are?</p>
<p>If the issue is that cancellous bone regions inside are not filled then you can use “Wrap Solidify” effect (provided by <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfaceWrapSolidify</a> extension) to fill them automatically.</p>

---

## Post #3 by @Umesh_Persad (2019-11-29 00:25 UTC)

<p>Here is an example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79731568cddba2fba806e3ed8de8b474c3c9a978.jpeg" data-download-href="/uploads/short-url/hkol2U6HoqGV7kK5tbwBnT9JxTq.jpeg?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/79731568cddba2fba806e3ed8de8b474c3c9a978_2_690x493.jpeg" alt="Untitled" data-base62-sha1="hkol2U6HoqGV7kK5tbwBnT9JxTq" width="690" height="493" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/79731568cddba2fba806e3ed8de8b474c3c9a978_2_690x493.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/79731568cddba2fba806e3ed8de8b474c3c9a978_2_1035x739.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79731568cddba2fba806e3ed8de8b474c3c9a978.jpeg 2x" data-dominant-color="1E1E1E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1302×932 95.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What is happening is that the smallest diameter of the paint brush (1%) is larger that the width of the bone profile, so I am getting a smaller than adequate segmentation area or larger adequate segmentation area depending on how I seed it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50872a71fd5ac672445022d16372ddd4de43c90f.jpeg" data-download-href="/uploads/short-url/bunMV288dkSnS3vxA4t3Y8cR8Cz.jpeg?dl=1" title="Untitled2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/50872a71fd5ac672445022d16372ddd4de43c90f_2_690x492.jpeg" alt="Untitled2" data-base62-sha1="bunMV288dkSnS3vxA4t3Y8cR8Cz" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/50872a71fd5ac672445022d16372ddd4de43c90f_2_690x492.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/50872a71fd5ac672445022d16372ddd4de43c90f_2_1035x738.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50872a71fd5ac672445022d16372ddd4de43c90f.jpeg 2x" data-dominant-color="1F1F1E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled2</span><span class="informations">1342×958 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-01-17 19:05 UTC)

<p>I’m not sure if you managed to solve this by yourself. If the resolution of the input image is so low that it is not usable to represent thin structures then you need to oversample the segmentation (click the segmentation geometry editing button - on the right side of master volume selector in Segment Editor module).</p>

---

## Post #5 by @Umesh_Persad (2020-01-18 02:02 UTC)

<p>Thanks, I will give it a go.</p>

---
