---
topic_id: 23657
title: "How To Fill Gaps Locally"
date: 2022-05-31
url: https://discourse.slicer.org/t/23657
---

# How to fill gaps locally? 

**Topic ID**: 23657
**Date**: 2022-05-31
**URL**: https://discourse.slicer.org/t/how-to-fill-gaps-locally/23657

---

## Post #1 by @dbgraf20 (2022-05-31 21:34 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 4.11<br>
Expected behavior: Clean Aorta Segmentation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/352bd7acc09ba38557e86e639f50586811b1bd61.png" data-download-href="/uploads/short-url/7AneKVgw7ShBAkMnZnHJuBKk9Yl.png?dl=1" title="Disk1_Aorta_Broken" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/352bd7acc09ba38557e86e639f50586811b1bd61_2_597x500.png" alt="Disk1_Aorta_Broken" data-base62-sha1="7AneKVgw7ShBAkMnZnHJuBKk9Yl" width="597" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/352bd7acc09ba38557e86e639f50586811b1bd61_2_597x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/352bd7acc09ba38557e86e639f50586811b1bd61.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/352bd7acc09ba38557e86e639f50586811b1bd61.png 2x" data-dominant-color="788897"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Disk1_Aorta_Broken</span><span class="informations">799×669 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Actual behavior: I am segmenting several Aortas. This one is behaving rather differently. When I manually make the ROI for the volume it leaves the material between slices out. Normally it fills between the slices, but for some reason it is not. Is there a way to fill these gaps locally and not globally. I cant use the smoothing fill because there are some fine areas between the aorta that need to remain open.</p>

---

## Post #2 by @JohnMarston (2022-05-31 22:24 UTC)

<p>You can use “smoothing” locally. Choose closing holes and then go to Smoothing brush option, enable sphere brush and edit in 3D view.</p>

---
