---
topic_id: 12160
title: "Recover 2D Curve From 2D Slices"
date: 2020-06-22
url: https://discourse.slicer.org/t/12160
---

# Recover 2d curve from 2d slices

**Topic ID**: 12160
**Date**: 2020-06-22
**URL**: https://discourse.slicer.org/t/recover-2d-curve-from-2d-slices/12160

---

## Post #1 by @loubna (2020-06-22 16:37 UTC)

<p>Hi,<br>
Is there any way to recover the points of 2D curve corresponding to segmented area into 2D slices as shown in figure. I want recover the coordinates of red points (red curve) surrounded the green area.</p>
<p>I know that in slicerRT, the labelMap is computed automatically from reconstructed surface, but how can I access to this labelMap in my code.<br>
Thank’s in advance</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54983cb54d557493ab34ccfd4ce98244cb86c5b0.jpeg" data-download-href="/uploads/short-url/c4mgZB5mdLSknPUEj8PVo7udXfa.jpeg?dl=1" title="slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54983cb54d557493ab34ccfd4ce98244cb86c5b0_2_690x387.jpeg" alt="slicer" data-base62-sha1="c4mgZB5mdLSknPUEj8PVo7udXfa" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54983cb54d557493ab34ccfd4ce98244cb86c5b0_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54983cb54d557493ab34ccfd4ce98244cb86c5b0_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54983cb54d557493ab34ccfd4ce98244cb86c5b0.jpeg 2x" data-dominant-color="313131"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer</span><span class="informations">1334×749 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2020-06-22 17:54 UTC)

<p>Do you want just an unordered list of the coordinates or do you want something like clockwise order fitted curve (the first is easier)/</p>

---

## Post #3 by @loubna (2020-06-22 17:56 UTC)

<p>Yes, i would just recover an unordered list of the coordinates.</p>

---

## Post #4 by @pieper (2020-06-22 18:11 UTC)

<p>The <code>points</code> variable in this snippet would have that info.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_the_values_of_all_voxels_for_a_label_value" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_the_values_of_all_voxels_for_a_label_value</a></p>

---

## Post #5 by @loubna (2020-06-22 18:13 UTC)

<p>Thank you very much for the answer</p>

---
