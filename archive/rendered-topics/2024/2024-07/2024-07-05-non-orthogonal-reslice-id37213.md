---
topic_id: 37213
title: "Non Orthogonal Reslice"
date: 2024-07-05
url: https://discourse.slicer.org/t/37213
---

# Non Orthogonal reslice

**Topic ID**: 37213
**Date**: 2024-07-05
**URL**: https://discourse.slicer.org/t/non-orthogonal-reslice/37213

---

## Post #1 by @philippepellerin (2024-07-05 13:11 UTC)

<p>Hi, I never found a way to perform a non orthogonal reslice easily.<br>
I found that other people face the same problem, for instance : <a href="https://discourse.slicer.org/u/1000_tiny_slices">1000_tiny_slices</a></p>
<p>[3d](<a href="https://discourse.slicer.org/t/resample-image-volume-along-user-defined-plane/">https://discourse.slicer.org/t/resample-image-volume-along-user-defined-plane/</a></p>
<p>I would like to transform and resample my CT volume so that a user-defined plane becomes one of the orthogonal slices. I used to do this in AVIZO by defining points, best-fitting a plane to those points and then resampling the image volume with the plane as a reference object. How can I go about doing something like this efficiently in 3D Slicer?</p>
<p>I wonder if it would be possible to get the h5 file from a set of slices oriented with the interactive cross?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f973a298b1d75c1f1afa8719746d30aecaa33cc9.jpeg" data-download-href="/uploads/short-url/zAKDvKv2fPWliPRBiRZed3KdV2h.jpeg?dl=1" title="non orthogonal reslice" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f973a298b1d75c1f1afa8719746d30aecaa33cc9_2_690x457.jpeg" alt="non orthogonal reslice" data-base62-sha1="zAKDvKv2fPWliPRBiRZed3KdV2h" width="690" height="457" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f973a298b1d75c1f1afa8719746d30aecaa33cc9_2_690x457.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f973a298b1d75c1f1afa8719746d30aecaa33cc9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f973a298b1d75c1f1afa8719746d30aecaa33cc9.jpeg 2x" data-dominant-color="464745"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">non orthogonal reslice</span><span class="informations">850×564 71.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-07-05 16:32 UTC)

<p>I think the easiest way is to use the CropVolume module.  Create the ROI and then right click on it and turn on rotation handles, then rotate as needed and apply.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8facc3e2cb1720942883aa1e785504c66e56ef24.jpeg" data-download-href="/uploads/short-url/kv0qpp6YXUte8DBaZX20h19yut6.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8facc3e2cb1720942883aa1e785504c66e56ef24_2_690x231.jpeg" alt="image" data-base62-sha1="kv0qpp6YXUte8DBaZX20h19yut6" width="690" height="231" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8facc3e2cb1720942883aa1e785504c66e56ef24_2_690x231.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8facc3e2cb1720942883aa1e785504c66e56ef24.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8facc3e2cb1720942883aa1e785504c66e56ef24.jpeg 2x" data-dominant-color="53605E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">875×293 71.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @philippepellerin (2024-07-06 07:02 UTC)

<p>Dear Peter, I tried it, and it works perfectly. Thank you so much.</p>

---
