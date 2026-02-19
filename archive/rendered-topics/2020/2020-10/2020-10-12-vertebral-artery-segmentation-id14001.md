---
topic_id: 14001
title: "Vertebral Artery Segmentation"
date: 2020-10-12
url: https://discourse.slicer.org/t/14001
---

# Vertebral artery segmentation

**Topic ID**: 14001
**Date**: 2020-10-12
**URL**: https://discourse.slicer.org/t/vertebral-artery-segmentation/14001

---

## Post #1 by @sarvpriya1985 (2020-10-12 15:02 UTC)

<p>Operating system:Windows 4.11 stable release<br>
Hi,</p>
<p>I am trying to segment vertebral arteries. After cropping volume, I used threshold to segment vertebral vessels. However, since these vessels cross within vertebral foramen, I am unable to remove adjacent bones even with ISLANDS TOOL. Is there any other way to get rid of bones and get vertebral arteries. I have tried scissors but the bone which is almost approximating vertebral artery is difficult to remove (as seen in axial view). I kept isotropic spacing to 1x to maintain resolution as changing to 3x did.t work well.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be4943490189a7d93f46a818daf30a920b56807e.jpeg" data-download-href="/uploads/short-url/r9lGqnd7Z7OGE674pzS1T3sTDky.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be4943490189a7d93f46a818daf30a920b56807e_2_513x500.jpeg" alt="Capture" data-base62-sha1="r9lGqnd7Z7OGE674pzS1T3sTDky" width="513" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be4943490189a7d93f46a818daf30a920b56807e_2_513x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be4943490189a7d93f46a818daf30a920b56807e_2_769x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be4943490189a7d93f46a818daf30a920b56807e_2_1026x1000.jpeg 2x" data-dominant-color="393C43"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1044×1017 97.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Appreciate all help!</p>

---

## Post #2 by @lassoan (2020-10-13 00:03 UTC)

<p>Since vessels and bones have similar intensity and they are close to each other, they actually touch each other in the image, so islands effect cannot separate them directly. You need to reduce the thresholded structures, then split, then grow them back. You can either do these steps manually (using Margin, Island, and optionally Grow from seeds or watershed effects) or using Local threshold effect (it performs these exact steps, on a single click; it is available in SegmentEditorExtraEffects extension).</p>

---

## Post #3 by @sarvpriya1985 (2020-10-13 00:54 UTC)

<p>Thanks for getting back Andras. I used grow from seeds and got this result. But it took me a lot of time to remove close bones manually. How can we reduce thresholding structures, split and grow- Can you pls let me know if this will save time.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00bf1b6ecea5553e1ce597118ab7e52fed7b77d2.jpeg" data-download-href="/uploads/short-url/6BrBlQYxsUnHe9TFX0LOOeesOm.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/00bf1b6ecea5553e1ce597118ab7e52fed7b77d2_2_373x500.jpeg" alt="Capture" data-base62-sha1="6BrBlQYxsUnHe9TFX0LOOeesOm" width="373" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/00bf1b6ecea5553e1ce597118ab7e52fed7b77d2_2_373x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/00bf1b6ecea5553e1ce597118ab7e52fed7b77d2_2_559x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00bf1b6ecea5553e1ce597118ab7e52fed7b77d2.jpeg 2x" data-dominant-color="999EC1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">670×898 46.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Thanks again,<br>
Sarv</p>

---

## Post #4 by @lassoan (2020-10-13 04:40 UTC)

<p>Use Local threshold effect - it automates these steps (shrink+split+grow). See detailed instructions here: <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/#slicersegmenteditorextraeffects">https://github.com/lassoan/SlicerSegmentEditorExtraEffects/#slicersegmenteditorextraeffects</a></p>

---
