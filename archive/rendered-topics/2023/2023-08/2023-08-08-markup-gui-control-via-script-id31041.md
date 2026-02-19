---
topic_id: 31041
title: "Markup Gui Control Via Script"
date: 2023-08-08
url: https://discourse.slicer.org/t/31041
---

# Markup gui control via script

**Topic ID**: 31041
**Date**: 2023-08-08
**URL**: https://discourse.slicer.org/t/markup-gui-control-via-script/31041

---

## Post #1 by @Ylim (2023-08-08 08:10 UTC)

<p>Hi,<br>
Would like to be able script the (a)options to snap at stl, (b) enable length measurement and (c) resample (with defined no. of points) via the markup module? please advise.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be3175cfa0d4cf11ec605969c2d0e470986bc383.jpeg" data-download-href="/uploads/short-url/r8wGCgqDdgtsFSocKLA6HE5BUfp.jpeg?dl=1" title="SlicerApp-real_Q6IqC8JfsI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be3175cfa0d4cf11ec605969c2d0e470986bc383_2_280x500.jpeg" alt="SlicerApp-real_Q6IqC8JfsI" data-base62-sha1="r8wGCgqDdgtsFSocKLA6HE5BUfp" width="280" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be3175cfa0d4cf11ec605969c2d0e470986bc383_2_280x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be3175cfa0d4cf11ec605969c2d0e470986bc383_2_420x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be3175cfa0d4cf11ec605969c2d0e470986bc383_2_560x1000.jpeg 2x" data-dominant-color="F3F4F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerApp-real_Q6IqC8JfsI</span><span class="informations">684×1218 99.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-08-09 17:41 UTC)

<p>All these options can be configured by calling <code>Set...</code> methods of the MRML node (markup node or its display node). See more details and examples in the <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true">PerkLab Slicer Programming tutorial</a>.</p>

---
