# Fusion of two adjacent parts of the vessel

**Topic ID**: 14443
**Date**: 2020-11-05
**URL**: https://discourse.slicer.org/t/fusion-of-two-adjacent-parts-of-the-vessel/14443

---

## Post #1 by @Andreas (2020-11-05 10:52 UTC)

<p>Hello everyone,</p>
<p>I have the following problem, which I would like to clarify with the help of the attached pictures:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6d2bb80e9996195abe47fd1a751d0ecf40d4f61.jpeg" data-download-href="/uploads/short-url/zduWTnPXVwcdzlZhJ9ajokb1DO1.jpeg?dl=1" title="lumen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6d2bb80e9996195abe47fd1a751d0ecf40d4f61_2_619x500.jpeg" alt="lumen" data-base62-sha1="zduWTnPXVwcdzlZhJ9ajokb1DO1" width="619" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6d2bb80e9996195abe47fd1a751d0ecf40d4f61_2_619x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6d2bb80e9996195abe47fd1a751d0ecf40d4f61_2_928x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6d2bb80e9996195abe47fd1a751d0ecf40d4f61.jpeg 2x" data-dominant-color="312D36"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">lumen</span><span class="informations">1111×897 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The top picture shows the lumen of the vessel. Two vascular branches branch off in the area of the aneurysm.</p>
<p>If I add the hollow in the required thickness, the walls of the smaller branch fuse with the aneurysm. (Bottom picture) I realize that this cannot be avoided for geometric reasons.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e5632790a9184d10e4180da76a4b6a8ee3ef1d9.jpeg" data-download-href="/uploads/short-url/22PmofQasJqZWHMOIGc3yoQ6O8h.jpeg?dl=1" title="hollow_new" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e5632790a9184d10e4180da76a4b6a8ee3ef1d9_2_616x499.jpeg" alt="hollow_new" data-base62-sha1="22PmofQasJqZWHMOIGc3yoQ6O8h" width="616" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e5632790a9184d10e4180da76a4b6a8ee3ef1d9_2_616x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e5632790a9184d10e4180da76a4b6a8ee3ef1d9_2_924x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e5632790a9184d10e4180da76a4b6a8ee3ef1d9.jpeg 2x" data-dominant-color="312C34"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">hollow_new</span><span class="informations">1111×901 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79a73f1543df075acee8901217e2d720826f5354.jpeg" data-download-href="/uploads/short-url/hmc63E5fgYDIoNJ2hgarVMttIoI.jpeg?dl=1" title="hollow model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/79a73f1543df075acee8901217e2d720826f5354_2_690x280.jpeg" alt="hollow model" data-base62-sha1="hmc63E5fgYDIoNJ2hgarVMttIoI" width="690" height="280" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/79a73f1543df075acee8901217e2d720826f5354_2_690x280.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/79a73f1543df075acee8901217e2d720826f5354_2_1035x420.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/79a73f1543df075acee8901217e2d720826f5354_2_1380x560.jpeg 2x" data-dominant-color="B8C7DB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">hollow model</span><span class="informations">1388×564 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My qustion:</p>
<p>Is there a way to cut / separate the two contact surfaces with the program?<br>
Can I choose a different wall thickness for individual vessel branches?</p>
<p>thank you in advance</p>

---

## Post #2 by @lassoan (2020-11-10 21:15 UTC)

<p>You can have different wall thickness in different regions by splitting the vasculature to several parts, growing each of them with different margins, then subtracting the original vessel lumen segment.</p>
<p>You can also slightly bend a side branch away from the aneurysm by slight warping of the image (for example, using Fiducial Registration Wizard module).</p>
<p>However, the closest to reality (mimic vessel walls touching each other but not being fused) may be to print the model as is, and separate the side branch from the aneurysm by cutting with a scalpel.</p>

---
