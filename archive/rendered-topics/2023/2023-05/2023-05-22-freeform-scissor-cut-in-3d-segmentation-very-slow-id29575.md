---
topic_id: 29575
title: "Freeform Scissor Cut In 3D Segmentation Very Slow"
date: 2023-05-22
url: https://discourse.slicer.org/t/29575
---

# Freeform scissor cut in 3D segmentation very slow

**Topic ID**: 29575
**Date**: 2023-05-22
**URL**: https://discourse.slicer.org/t/freeform-scissor-cut-in-3d-segmentation-very-slow/29575

---

## Post #1 by @ziri (2023-05-22 13:03 UTC)

<p>Hi, I was trying to cut my 3D segmentation map with scissor tool, but it performs very slow: for the scissor-cut task below it takes &gt;10min. I also disabled surface smoothing in segmentation rendering.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2ba3c55ca42b4ec5949857953a35c0894411797.jpeg" data-download-href="/uploads/short-url/wlIUOLY4zdMCU3Xk6oexrLPd4ur.jpeg?dl=1" title="cut3d" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2ba3c55ca42b4ec5949857953a35c0894411797_2_680x500.jpeg" alt="cut3d" data-base62-sha1="wlIUOLY4zdMCU3Xk6oexrLPd4ur" width="680" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2ba3c55ca42b4ec5949857953a35c0894411797_2_680x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2ba3c55ca42b4ec5949857953a35c0894411797_2_1020x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2ba3c55ca42b4ec5949857953a35c0894411797.jpeg 2x" data-dominant-color="8993B1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cut3d</span><span class="informations">1204×884 257 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My platform: i7-11700k desktop CPU | Windows 10 | Slicer v.5.0.3<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c1d1ea2225aef120459efd1df9908c943b13ea6.png" data-download-href="/uploads/short-url/8zN2hvMKi3ds3SQeMA6Fttcyxym.png?dl=1" title="Image 003" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c1d1ea2225aef120459efd1df9908c943b13ea6_2_690x86.png" alt="Image 003" data-base62-sha1="8zN2hvMKi3ds3SQeMA6Fttcyxym" width="690" height="86" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c1d1ea2225aef120459efd1df9908c943b13ea6_2_690x86.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c1d1ea2225aef120459efd1df9908c943b13ea6_2_1035x129.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c1d1ea2225aef120459efd1df9908c943b13ea6_2_1380x172.png 2x" data-dominant-color="F6EBDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image 003</span><span class="informations">1505×189 14.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My data:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c8f7c9f77d714beb465f9b5838e8c8916a5e8cc.png" data-download-href="/uploads/short-url/44EMS01L8R1AJM79hMtmVIWBntO.png?dl=1" title="Image 005" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c8f7c9f77d714beb465f9b5838e8c8916a5e8cc.png" alt="Image 005" data-base62-sha1="44EMS01L8R1AJM79hMtmVIWBntO" width="690" height="273" data-dominant-color="F6F6F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image 005</span><span class="informations">1337×529 14.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’m also using a 4k monitor so not sure if takes more resources to compute but I tried using a 1080p screen resolution it doesn’t help too much. I appreciate any advice!</p>

---

## Post #2 by @pieper (2023-05-22 14:48 UTC)

<p>Recalculating the 3D surface is probably taking all the time.  Try turning off 3D and do as much cleanup as you can in the slice views and then turn on 3D when you have less noise in the model.</p>

---

## Post #3 by @ziri (2023-05-25 01:51 UTC)

<p>Thanks for the suggestion! This does improve the speed. However, it was not like this slow (&gt;10min) before (with older slicer version or on a different dataset I’m not sure), so I’m trying to figure out the fundamental issue here.</p>

---

## Post #4 by @pieper (2023-05-25 13:39 UTC)

<p>If you have a chance to experiment with different slicer versions and datasets and can report a reproducible difference in behavior that would be helpful.  From looking at your screenshot it appears you have a lot of noise, and those small islands take time to update in 3D on every edit operation is a good workaround.</p>

---
