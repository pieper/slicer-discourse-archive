---
topic_id: 27413
title: "Local Threshold Restrict Threshold Operation To User Defined"
date: 2023-01-23
url: https://discourse.slicer.org/t/27413
---

# Local Threshold --> restrict threshold operation to user-defined 3D region --> how to?

**Topic ID**: 27413
**Date**: 2023-01-23
**URL**: https://discourse.slicer.org/t/local-threshold-restrict-threshold-operation-to-user-defined-3d-region-how-to/27413

---

## Post #1 by @MrMarkus (2023-01-23 07:22 UTC)

<p>Operating system: Win10<br>
Slicer version: 5.2.1 r31317 / 77da381</p>
<p>Hi,</p>
<p>maybe you could help me out here:</p>
<p>I am using “Local Threshold” and the region which should be segmented is further defined by the<br>
option “ROI” → Volume rendering ROI.</p>
<p>The “volume rendering roi”  (actived in: ‘volume rendering’)  can be adjusted in 3D with the help of the colored buttons.</p>
<p>My question:</p>
<ul>
<li>is there a way to define a differently shaped ROI instead of rectangular “volume rendering roi”? The best would be some kind of 3D ellipse that can be adjusted to the area to be segmented. In this way, the threshold operation would be performed only in a well-defined area.</li>
</ul>
<p>Any help is greatly appreciated!</p>
<p>Thanks!</p>
<p>Best,<br>
Markus</p>

---

## Post #2 by @chir.set (2023-01-23 09:26 UTC)

<aside class="quote no-group" data-username="MrMarkus" data-post="1" data-topic="27413">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<p>define a differently shaped ROI</p>
</blockquote>
</aside>
<p>You may draw a first extent blocker segment using the Paint tool for example, with the sphere brush. Then create another segment for Local Threshold, while restraining the Editable Area in the masking options to the previous segment.</p>

---
