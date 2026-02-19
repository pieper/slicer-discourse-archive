---
topic_id: 28625
title: "A Plane That Wont Go Away"
date: 2023-03-28
url: https://discourse.slicer.org/t/28625
---

# A plane that won't go away

**Topic ID**: 28625
**Date**: 2023-03-28
**URL**: https://discourse.slicer.org/t/a-plane-that-wont-go-away/28625

---

## Post #1 by @mohammed_alshakhas (2023-03-28 13:40 UTC)

<p>im doing usual segmentation workflow with two studies.</p>
<p>however, I ended up with a plane that won’t go away.</p>
<p>i didn’t create any plane. I only used toggle slice on and off as I usually do<br>
I tried hiding all volumes and segmentation but it didn’t help</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40abb308ebeb64969f5dc54415ac54e3b6cd43b0.png" data-download-href="/uploads/short-url/9e6qbf9dcoWFuUoB4rmYl0IL7RS.png?dl=1" title="Screenshot 2023-03-28 at 16.16.49" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40abb308ebeb64969f5dc54415ac54e3b6cd43b0_2_519x500.png" alt="Screenshot 2023-03-28 at 16.16.49" data-base62-sha1="9e6qbf9dcoWFuUoB4rmYl0IL7RS" width="519" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40abb308ebeb64969f5dc54415ac54e3b6cd43b0_2_519x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40abb308ebeb64969f5dc54415ac54e3b6cd43b0_2_778x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40abb308ebeb64969f5dc54415ac54e3b6cd43b0_2_1038x1000.png 2x" data-dominant-color="BABBBC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-03-28 at 16.16.49</span><span class="informations">1962×1890 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-03-28 13:42 UTC)

<p>What happens if you save the scene, restart Slicer, and load the scene?</p>

---

## Post #3 by @mohammed_alshakhas (2023-03-28 13:43 UTC)

<p>the same thing persists</p>

---

## Post #4 by @lassoan (2023-03-28 13:48 UTC)

<p>Perfect! Any issues that can be reproduced can be fixed. Could you share the scene (upload to dropbox/onedrive/google drive and post the link)? You can remove any nodes that you don’t want to share.</p>

---

## Post #5 by @mohammed_alshakhas (2023-03-28 17:14 UTC)

<p>is it possible to anonymize dicom date before sending it ?</p>

---

## Post #6 by @lassoan (2023-03-28 17:18 UTC)

<p>You can save the scene as an .mrb file then rename to .zip, unzip it, and edit the .mrml scene file to remove any patient health information from it. You can also remove any other data files that may contain patient information. Then zip the folder, rename the file to .mrb, and test if it still shows the rectangle.</p>

---
