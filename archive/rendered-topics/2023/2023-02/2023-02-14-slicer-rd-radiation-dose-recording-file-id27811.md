---
topic_id: 27811
title: "Slicer Rd Radiation Dose Recording File"
date: 2023-02-14
url: https://discourse.slicer.org/t/27811
---

# Slicer RD (radiation dose) recording file

**Topic ID**: 27811
**Date**: 2023-02-14
**URL**: https://discourse.slicer.org/t/slicer-rd-radiation-dose-recording-file/27811

---

## Post #1 by @tenzin_kunkyab (2023-02-14 18:29 UTC)

<p>Hi Developers,</p>
<p>I have a question regarding some of the numbers that I see on the segment editor. Basically, I have a RD file, (Radiation dose file) with dose up to maximum of about 32 Gy. I wanted to threshold hold such that I can see 50% dose threshold, i.e. 16 Gy. I was thinking of using segment editor module with threshold functionality. If you see the screenshot that was uploaded, the max threshold is about 3327560.00, does this correspond to ~ 32 Gy that I see in the treatment planning system? and if so, if I end up creating a 50% threshold range to the max and creates a segment editor, that thresholds all the value and only segments the value about 50% of the radiation dose recorded?</p>
<p>Thank you!</p>
<p>best<br>
Tenzin</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa2737432f39cbf92fd870792d0b61265a1c2c15.png" data-download-href="/uploads/short-url/ohfbKM7yKDEdqaBuZLcXRf5Ki4l.png?dl=1" title="Screenshot 2023-02-14 at 10.22.59 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa2737432f39cbf92fd870792d0b61265a1c2c15_2_690x383.png" alt="Screenshot 2023-02-14 at 10.22.59 AM" data-base62-sha1="ohfbKM7yKDEdqaBuZLcXRf5Ki4l" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa2737432f39cbf92fd870792d0b61265a1c2c15_2_690x383.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa2737432f39cbf92fd870792d0b61265a1c2c15_2_1035x574.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa2737432f39cbf92fd870792d0b61265a1c2c15_2_1380x766.png 2x" data-dominant-color="393839"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-02-14 at 10.22.59 AM</span><span class="informations">2872×1598 390 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-02-15 05:37 UTC)

<p>I would recommend to install SlicerRT extension and load this series as a dose volume. They use some special fields that define voxel value scaling, which are not used when you load it as a generic image.</p>

---
