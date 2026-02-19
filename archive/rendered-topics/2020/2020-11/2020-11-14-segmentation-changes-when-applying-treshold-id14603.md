---
topic_id: 14603
title: "Segmentation Changes When Applying Treshold"
date: 2020-11-14
url: https://discourse.slicer.org/t/14603
---

# Segmentation changes when applying Treshold

**Topic ID**: 14603
**Date**: 2020-11-14
**URL**: https://discourse.slicer.org/t/segmentation-changes-when-applying-treshold/14603

---

## Post #1 by @Papis (2020-11-14 18:25 UTC)

<p>Operating system: MacOS Mojave 10.14.6<br>
Slicer version: 4.11.20200930<br>
Expected behavior: Save segmented area within chosen threshold<br>
Actual behavior: Cuts off majority of segmented area when applying threshold leaving irrelevant shape</p>
<p>Hi!</p>
<p>I have imported a DICOM-file through a CD-drive, rendered the volume visible in the purple box, added a new segment under segment editor, changed the threshold so only relevant structures are shown and when i click apply I’m not left with what I had highlighted but some other shape instead? Anyone have a clue what I’m doing wrong?</p>
<p>See attached photos. My intention is to convert the DICOM into .stl and be able to work with it in Blender…</p>
<p>Thanks /S<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/1993d4729ec8beee65680f11b8c112cb9e8acd4c.jpeg" data-download-href="/uploads/short-url/3EgEY8rQRgMLiOTBTZcMpmviAws.jpeg?dl=1" title="Skärmavbild 2020-11-14 kl. 16.48.25" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1993d4729ec8beee65680f11b8c112cb9e8acd4c_2_690x388.jpeg" alt="Skärmavbild 2020-11-14 kl. 16.48.25" data-base62-sha1="3EgEY8rQRgMLiOTBTZcMpmviAws" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1993d4729ec8beee65680f11b8c112cb9e8acd4c_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1993d4729ec8beee65680f11b8c112cb9e8acd4c_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1993d4729ec8beee65680f11b8c112cb9e8acd4c_2_1380x776.jpeg 2x" data-dominant-color="3B3F44"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Skärmavbild 2020-11-14 kl. 16.48.25</span><span class="informations">5120×2880 1.02 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5dc522ec5a1b1b2b5fe49e5731dad530412a6a1.jpeg" data-download-href="/uploads/short-url/wNrnkHNtwGqXUJSFUWYBjEKCiuB.jpeg?dl=1" title="Skärmavbild 2020-11-14 kl. 16.48.56" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5dc522ec5a1b1b2b5fe49e5731dad530412a6a1_2_616x500.jpeg" alt="Skärmavbild 2020-11-14 kl. 16.48.56" data-base62-sha1="wNrnkHNtwGqXUJSFUWYBjEKCiuB" width="616" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5dc522ec5a1b1b2b5fe49e5731dad530412a6a1_2_616x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5dc522ec5a1b1b2b5fe49e5731dad530412a6a1_2_924x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5dc522ec5a1b1b2b5fe49e5731dad530412a6a1_2_1232x1000.jpeg 2x" data-dominant-color="252825"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Skärmavbild 2020-11-14 kl. 16.48.56</span><span class="informations">3150×2556 533 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0aa78dfe82fde04e9b3cc16ac1a2f3361c67a81d.jpeg" data-download-href="/uploads/short-url/1wfL3hs6Y0FMc2e4Cg19VRynJVj.jpeg?dl=1" title="Skärmavbild 2020-11-14 kl. 16.49.19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0aa78dfe82fde04e9b3cc16ac1a2f3361c67a81d_2_690x471.jpeg" alt="Skärmavbild 2020-11-14 kl. 16.49.19" data-base62-sha1="1wfL3hs6Y0FMc2e4Cg19VRynJVj" width="690" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0aa78dfe82fde04e9b3cc16ac1a2f3361c67a81d_2_690x471.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0aa78dfe82fde04e9b3cc16ac1a2f3361c67a81d_2_1035x706.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0aa78dfe82fde04e9b3cc16ac1a2f3361c67a81d_2_1380x942.jpeg 2x" data-dominant-color="222322"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Skärmavbild 2020-11-14 kl. 16.49.19</span><span class="informations">3056×2090 307 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d028eb63e2dda2c9859bed2644eb0cc105224ba3.jpeg" data-download-href="/uploads/short-url/tHsYYqFM9FyP9s1qmhPfKAlAZJp.jpeg?dl=1" title="Skärmavbild 2020-11-14 kl. 16.50.15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d028eb63e2dda2c9859bed2644eb0cc105224ba3_2_687x500.jpeg" alt="Skärmavbild 2020-11-14 kl. 16.50.15" data-base62-sha1="tHsYYqFM9FyP9s1qmhPfKAlAZJp" width="687" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d028eb63e2dda2c9859bed2644eb0cc105224ba3_2_687x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d028eb63e2dda2c9859bed2644eb0cc105224ba3_2_1030x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d028eb63e2dda2c9859bed2644eb0cc105224ba3_2_1374x1000.jpeg 2x" data-dominant-color="252526"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Skärmavbild 2020-11-14 kl. 16.50.15</span><span class="informations">2578×1876 264 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa7d985335204ccc7819193a3cb13b645831d97a.jpeg" data-download-href="/uploads/short-url/zJWs81C6kVogtjbeIoJ2vQwc4Hw.jpeg?dl=1" title="Skärmavbild 2020-11-14 kl. 16.50.34" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa7d985335204ccc7819193a3cb13b645831d97a_2_300x500.jpeg" alt="Skärmavbild 2020-11-14 kl. 16.50.34" data-base62-sha1="zJWs81C6kVogtjbeIoJ2vQwc4Hw" width="300" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa7d985335204ccc7819193a3cb13b645831d97a_2_300x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa7d985335204ccc7819193a3cb13b645831d97a_2_450x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa7d985335204ccc7819193a3cb13b645831d97a_2_600x1000.jpeg 2x" data-dominant-color="3D3E40"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Skärmavbild 2020-11-14 kl. 16.50.34</span><span class="informations">720×1198 42 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Papis (2020-11-15 08:54 UTC)

<p>Ok I managed to solve this one myself. Problem was the segmentation geometry and when that was changed to desirable dimensions so was the segmentation upon applying.</p>
<p>All the best / S</p>

---
