# UKF tractography: orientation issue

**Topic ID**: 14223
**Date**: 2020-10-24
**URL**: https://discourse.slicer.org/t/ukf-tractography-orientation-issue/14223

---

## Post #1 by @Vinny (2020-10-24 15:20 UTC)

<p>Slicer version: 4.11.0 2020-06-06</p>
<p>Hi,</p>
<p>When I run UKF tractography, the bundles (red) are being seeded on the opposite side of the label map.  However, using the Tractography Seeding module, the tracts (green) are seeded from the correct side.</p>
<p>Any idea on how to rectify the orientation issue that I’m getting with UKF tractography?</p>
<p>Thanks for your help,</p>
<p>Vinny</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ada7b2de646334c0dedbc3e211a5eb21f802d71.jpeg" data-download-href="/uploads/short-url/8oDMNlMbkxtZFBxIjyfvtMPmPGV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ada7b2de646334c0dedbc3e211a5eb21f802d71_2_690x379.jpeg" alt="image" data-base62-sha1="8oDMNlMbkxtZFBxIjyfvtMPmPGV" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ada7b2de646334c0dedbc3e211a5eb21f802d71_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ada7b2de646334c0dedbc3e211a5eb21f802d71_2_1035x568.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ada7b2de646334c0dedbc3e211a5eb21f802d71_2_1380x758.jpeg 2x" data-dominant-color="858593"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1855×1020 346 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2020-10-24 15:41 UTC)

<p>Can you try the latest stable version? (4.11-20200930)</p>

---

## Post #3 by @Vinny (2020-10-24 16:46 UTC)

<p>The latest stable version worked, thanks!</p>

---
