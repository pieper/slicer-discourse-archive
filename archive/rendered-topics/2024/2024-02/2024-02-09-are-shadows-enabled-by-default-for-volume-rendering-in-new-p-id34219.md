# Are shadows enabled by default for Volume Rendering in new previews

**Topic ID**: 34219
**Date**: 2024-02-09
**URL**: https://discourse.slicer.org/t/are-shadows-enabled-by-default-for-volume-rendering-in-new-previews/34219

---

## Post #1 by @muratmaga (2024-02-09 04:35 UTC)

<p>This is the default volume rendering of MRHead in 5.6.1 by simply dragging and dropping to 3D viewer. No adjustment.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f08ba117d4cc758dcd774280b16f42ec93b251a.jpeg" data-download-href="/uploads/short-url/i7NkPaDGSJdsMUhlhXQtn5WIyMi.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f08ba117d4cc758dcd774280b16f42ec93b251a_2_685x499.jpeg" alt="image" data-base62-sha1="i7NkPaDGSJdsMUhlhXQtn5WIyMi" width="685" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f08ba117d4cc758dcd774280b16f42ec93b251a_2_685x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f08ba117d4cc758dcd774280b16f42ec93b251a_2_1027x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f08ba117d4cc758dcd774280b16f42ec93b251a_2_1370x998.jpeg 2x" data-dominant-color="9E8E95"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2672×1950 593 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is the same thing from the preview I just installed (r32708). It seems darker with shadows. So is this now the default in volume rendering? Is there a way to turn it off or adjust?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2722d494ca0ffb9e50b11cd0dae6c97ebef22085.jpeg" data-download-href="/uploads/short-url/5AdfcgeWxLOqxCx28gV9ZXMr9Vb.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/2722d494ca0ffb9e50b11cd0dae6c97ebef22085_2_673x500.jpeg" alt="image" data-base62-sha1="5AdfcgeWxLOqxCx28gV9ZXMr9Vb" width="673" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/2722d494ca0ffb9e50b11cd0dae6c97ebef22085_2_673x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/2722d494ca0ffb9e50b11cd0dae6c97ebef22085_2_1009x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/2722d494ca0ffb9e50b11cd0dae6c97ebef22085_2_1346x1000.jpeg 2x" data-dominant-color="86808D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2660×1976 576 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-02-09 04:37 UTC)

<p>Nevermind, I found the answer. For those of you, who are like me, and unaware of this feature, setting is in the 3D viewer widget control.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/138e6f0af14c24fdb99a20077b4b9a3de71b92f7.png" data-download-href="/uploads/short-url/2N0eyOxGaErF4L1k3yreMIyAK35.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/138e6f0af14c24fdb99a20077b4b9a3de71b92f7_2_690x344.png" alt="image" data-base62-sha1="2N0eyOxGaErF4L1k3yreMIyAK35" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/138e6f0af14c24fdb99a20077b4b9a3de71b92f7_2_690x344.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/138e6f0af14c24fdb99a20077b4b9a3de71b92f7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/138e6f0af14c24fdb99a20077b4b9a3de71b92f7.png 2x" data-dominant-color="AAADCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">734×366 56.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It looks great to have the shadows so easily available.</p>

---

## Post #3 by @lassoan (2024-02-10 18:00 UTC)

<p>You can change the default in application settings.</p>
<p>I’ll also make it disabled by default to avoid surprises (and to give some time for the feature to mature).</p>

---
