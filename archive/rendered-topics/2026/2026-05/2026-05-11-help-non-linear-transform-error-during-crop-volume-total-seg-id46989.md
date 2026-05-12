---
topic_id: 46989
title: "Help Non Linear Transform Error During Crop Volume Total Seg"
date: 2026-05-11
url: https://discourse.slicer.org/t/46989
---

# Help Non-linear Transform Error During Crop Volume / Total Segmentation

**Topic ID**: 46989
**Date**: 2026-05-11
**URL**: https://discourse.slicer.org/t/help-non-linear-transform-error-during-crop-volume-total-segmentation/46989

---

## Post #1 by @jimenagonzalezsal (2026-05-11 21:15 UTC)

<p>Hi everyone!!</p>
<p>I wanted to ask for some help. I’m trying to crop a volume and then add Total Segmentation, but whenever I try to either crop or create the segmentation from an MRI, a message appears stating: “Output volume is under a non-linear transform” (the Fix button doesn’t work either!).</p>
<p>Thanks!!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bdab6acd58189346a01a73d26188efe925cea89.jpeg" data-download-href="/uploads/short-url/hFFjS9b07itWD6AhKmeAWstj6dj.jpeg?dl=1" title="Screenshot 2026-05-11 at 3.05.25 p.m." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bdab6acd58189346a01a73d26188efe925cea89_2_676x500.jpeg" alt="Screenshot 2026-05-11 at 3.05.25 p.m." data-base62-sha1="hFFjS9b07itWD6AhKmeAWstj6dj" width="676" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bdab6acd58189346a01a73d26188efe925cea89_2_676x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bdab6acd58189346a01a73d26188efe925cea89_2_1014x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bdab6acd58189346a01a73d26188efe925cea89_2_1352x1000.jpeg 2x" data-dominant-color="D1D0CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-05-11 at 3.05.25 p.m.</span><span class="informations">1530×1130 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2026-05-11 22:03 UTC)

<p>Did you try the ‘harden’ operation in the transforms module?</p>
<p>Also check for any errors in the log when you click the Fix button.</p>

---
