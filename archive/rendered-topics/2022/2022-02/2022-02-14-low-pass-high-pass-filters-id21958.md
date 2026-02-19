---
topic_id: 21958
title: "Low Pass High Pass Filters"
date: 2022-02-14
url: https://discourse.slicer.org/t/21958
---

# Low-Pass High-Pass Filters

**Topic ID**: 21958
**Date**: 2022-02-14
**URL**: https://discourse.slicer.org/t/low-pass-high-pass-filters/21958

---

## Post #1 by @Effand (2022-02-14 14:25 UTC)

<p>Hi All, I am working on vessel segmentation for my ultrasound images, I have tried VMTK but it didn’t work so now I am annotating the vessels manually and to eliminate the high noise signal for sharper and finer detailed segmentation I wanna apply simple filter such as Low pass High Pass filters or try to find the background noise intensity and filter it later using a tool you would recommend. I added some images for the noise signal and its overlap with the vessel segmentation at the top right of the image where you can see the noise effect and greyness of the image.</p>
<p>Thank you again all and I hope I would get some help from your forum to overcome this problem in processing my data using 3D Slicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfc39732dbfcf197aec0bfaa87c867d20bd73b15.jpeg" data-download-href="/uploads/short-url/rmqfmDT0TJ74k2pulJrV78bVfYF.jpeg?dl=1" title="Screenshot 2022-02-14 at 15.22.57" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfc39732dbfcf197aec0bfaa87c867d20bd73b15_2_386x500.jpeg" alt="Screenshot 2022-02-14 at 15.22.57" data-base62-sha1="rmqfmDT0TJ74k2pulJrV78bVfYF" width="386" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfc39732dbfcf197aec0bfaa87c867d20bd73b15_2_386x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfc39732dbfcf197aec0bfaa87c867d20bd73b15_2_579x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfc39732dbfcf197aec0bfaa87c867d20bd73b15_2_772x1000.jpeg 2x" data-dominant-color="616361"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-02-14 at 15.22.57</span><span class="informations">1212×1566 66.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56ecfdeb9d5c2d7c845abb4368edd328b92746e3.jpeg" data-download-href="/uploads/short-url/coYOxFSWU4NXG2Y7mY0LNrI4pLt.jpeg?dl=1" title="Screenshot 2022-02-14 at 15.23.13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/56ecfdeb9d5c2d7c845abb4368edd328b92746e3_2_451x500.jpeg" alt="Screenshot 2022-02-14 at 15.23.13" data-base62-sha1="coYOxFSWU4NXG2Y7mY0LNrI4pLt" width="451" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/56ecfdeb9d5c2d7c845abb4368edd328b92746e3_2_451x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/56ecfdeb9d5c2d7c845abb4368edd328b92746e3_2_676x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/56ecfdeb9d5c2d7c845abb4368edd328b92746e3_2_902x1000.jpeg 2x" data-dominant-color="767A76"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-02-14 at 15.23.13</span><span class="informations">1220×1352 61.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
