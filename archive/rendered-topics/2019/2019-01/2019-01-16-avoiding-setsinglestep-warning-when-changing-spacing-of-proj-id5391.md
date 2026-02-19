---
topic_id: 5391
title: "Avoiding Setsinglestep Warning When Changing Spacing Of Proj"
date: 2019-01-16
url: https://discourse.slicer.org/t/5391
---

# Avoiding setSingleStep warning when changing spacing of projection volume node

**Topic ID**: 5391
**Date**: 2019-01-16
**URL**: https://discourse.slicer.org/t/avoiding-setsinglestep-warning-when-changing-spacing-of-projection-volume-node/5391

---

## Post #1 by @jamesobutler (2019-01-16 18:09 UTC)

<p>When I’m changing the spacing of a volume dimension that is only 1 voxel, such as an intensity projection volume, I keep getting warnings like below whenever the spacing is increased.  Is there something I can call prior to increasing spacing so that I can avoid this issue?</p>
<p><code>ctkSliderWidget::setSingleStep()  5.43941 is out of bounds. 18.2257 21.704 19.9649</code> originates from <a href="https://github.com/commontk/CTK/blob/cccef11c938cc946789ddb25ccc613287a33c56e/Libs/Widgets/ctkSliderWidget.cpp#L414-L415" rel="noopener nofollow ugc">here</a>.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd5e3544ab234ced7a62a97ce8bdd98b081ef6bd.png" alt="image-projection-spacing" data-base62-sha1="tiLIIKSGd6WYdXwdQTctBa7pZzD" width="515" height="105"></p>

---
