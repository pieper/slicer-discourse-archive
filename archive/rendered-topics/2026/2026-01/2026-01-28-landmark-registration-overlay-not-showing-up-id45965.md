# Landmark registration overlay not showing up

**Topic ID**: 45965
**Date**: 2026-01-28
**URL**: https://discourse.slicer.org/t/landmark-registration-overlay-not-showing-up/45965

---

## Post #1 by @RHB (2026-01-28 09:14 UTC)

<p>Hi,<br>
I have 2 2D oct slices that I want to register mutually, these are not 3D volume, just retinal 2D slice and previously I tried to do Landmark registration using these, it worked. Now after that I am trying to do the same thing but sometimes the overlay shows up sometimes doesn’t. Basically without the overlapping slices, I can’t put marker on the slices and transform. Any idea why this is happening? ss attached below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dfd7ba867004d21fb1a4ab963538d0282d6146e.jpeg" data-download-href="/uploads/short-url/b7VQHTGxJOi5H4kSIQTV4KXmx8W.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dfd7ba867004d21fb1a4ab963538d0282d6146e_2_690x357.jpeg" alt="image" data-base62-sha1="b7VQHTGxJOi5H4kSIQTV4KXmx8W" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dfd7ba867004d21fb1a4ab963538d0282d6146e_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dfd7ba867004d21fb1a4ab963538d0282d6146e_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dfd7ba867004d21fb1a4ab963538d0282d6146e_2_1380x714.jpeg 2x" data-dominant-color="6B6B6A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1911×989 263 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2026-01-28 12:40 UTC)

<p>Sometimes you need to use the Fit button to make sure the views are set correctly.  If that’s not it, maybe you can determine a minimal set of operations to replicate the issue so someone can replicate it.</p>

---

## Post #3 by @RHB (2026-01-28 15:25 UTC)

<p>I got it worked afterwards. The problem is during data loading, only need to set the moving and fixed volume and nothing else. Although there are options to set output/<strong>transformed volume</strong> and  <strong>target transform</strong> name, if I set those up, overlaping windows stays black no matter what I try. So only load fixed volume and moving volume, set the registration type and later set the output/transformation name.</p>

---
