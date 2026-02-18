# Change transform display spacing less than 1 mm

**Topic ID**: 44440
**Date**: 2025-09-10
**URL**: https://discourse.slicer.org/t/change-transform-display-spacing-less-than-1-mm/44440

---

## Post #1 by @sulli419 (2025-09-10 21:31 UTC)

<p>Hi,</p>
<p>I applied a transform to a small rodent volume, but the various arrow and grid options seem far too large for visualizing the transform.  The key seems to be lowering the “spacing” under the “advanced” menu, but it won’t let me set this lower than 1mm (see red circle in 2nd image).  Is this a known stopping point, or am I doing something wrong?</p>
<p>Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a55720a43f94b0e588305d2dc177fd2a433f22a.png" data-download-href="/uploads/short-url/62v7qDmQzPK4leofkKUUXCMJTnA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a55720a43f94b0e588305d2dc177fd2a433f22a_2_690x236.png" alt="image" data-base62-sha1="62v7qDmQzPK4leofkKUUXCMJTnA" width="690" height="236" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a55720a43f94b0e588305d2dc177fd2a433f22a_2_690x236.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a55720a43f94b0e588305d2dc177fd2a433f22a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a55720a43f94b0e588305d2dc177fd2a433f22a.png 2x" data-dominant-color="303030"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">703×241 42.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9ce99a2a8433cd0488ec5dae836380a2c513b45.png" data-download-href="/uploads/short-url/v4Ofuon3Kk0nRTsUvpq1d2nXkwt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9ce99a2a8433cd0488ec5dae836380a2c513b45_2_690x348.png" alt="image" data-base62-sha1="v4Ofuon3Kk0nRTsUvpq1d2nXkwt" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9ce99a2a8433cd0488ec5dae836380a2c513b45_2_690x348.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9ce99a2a8433cd0488ec5dae836380a2c513b45_2_1035x522.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9ce99a2a8433cd0488ec5dae836380a2c513b45.png 2x" data-dominant-color="35342C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1253×633 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-09-10 21:42 UTC)

<p>Yeah, that’s one of the long-standing issues that small voxel values are not consistently supported in Slicer. You can open a issue and request this feature on the github.</p>
<p>Until then, I suggest applying a scaling transform (like x100 or x10 depending on your voxel size) and hardening it, and then applying your transform to visualize…</p>

---

## Post #3 by @sulli419 (2025-09-10 22:21 UTC)

<p>Good to know, thanks.  Silly question, would the original transform that I’m trying to visualize have to be scaled by the same factor (e.g., 10x 100x) the volume is?</p>

---

## Post #4 by @muratmaga (2025-09-10 22:25 UTC)

<p>If it is strictly rotation, I don’t think so. But if there is translation as well you will probably have to redo the transform (or correctly scale only the translation values in the matrix).</p>

---
