---
topic_id: 43325
title: "Segmentation Of Swim Bladders In Micro Ct Scans"
date: 2025-06-11
url: https://discourse.slicer.org/t/43325
---

# Segmentation of swim bladders in micro-CT scans

**Topic ID**: 43325
**Date**: 2025-06-11
**URL**: https://discourse.slicer.org/t/segmentation-of-swim-bladders-in-micro-ct-scans/43325

---

## Post #1 by @BennyShoe (2025-06-11 19:22 UTC)

<p>Hello everyone,</p>
<p>I’m new to the Slicer community and currently working on a project involving the segmentation of swim bladders(circled in blue) from fish micro-CT scans. However, I’m running into difficulty due to the low contrast between the swim bladder and the surrounding area.</p>
<p>So far, I’ve been using the paint tool to manually segment the swim bladder slice by slice. Unfortunately, the final segment often appears irregular or incomplete.</p>
<p>I want to improve the overall quality of the results, so I was wondering if there is a recommended approach for segmenting low contrast regions like this? Are there specific segmentation tools that you’ve found helpful in similar situations?</p>
<p>Any advice or suggestions would be greatly appreciated!</p>
<p>Thank you,<br>
-B</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90ad9471cc5c100396e71baecdda6142a6a80368.png" data-download-href="/uploads/short-url/kDSEeiTuFjRizUCtq70gpYPVpZm.png?dl=1" title="SB1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90ad9471cc5c100396e71baecdda6142a6a80368_2_690x460.png" alt="SB1" data-base62-sha1="kDSEeiTuFjRizUCtq70gpYPVpZm" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90ad9471cc5c100396e71baecdda6142a6a80368_2_690x460.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90ad9471cc5c100396e71baecdda6142a6a80368_2_1035x690.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90ad9471cc5c100396e71baecdda6142a6a80368.png 2x" data-dominant-color="4B4B4C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SB1</span><span class="informations">1140×760 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-06-11 19:29 UTC)

<p>That does look tough, but maybe nnInteractive would be worth trying.</p>

---

## Post #3 by @lassoan (2025-06-13 00:54 UTC)

<p>Since there is some contrast, there is a chance that “Grow from seeds” or “Watershed” (provided by SegmentEditorExtraEffects extension) effect can do it, too.</p>

---
