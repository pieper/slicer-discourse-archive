---
topic_id: 44355
title: "Can T Visualize My Liver Segmentation In 3D After Cropping S"
date: 2025-09-05
url: https://discourse.slicer.org/t/44355
---

# Can’t visualize my liver segmentation in 3D after cropping (Scalar Range shows 0–2 but nothing displays)

**Topic ID**: 44355
**Date**: 2025-09-05
**URL**: https://discourse.slicer.org/t/can-t-visualize-my-liver-segmentation-in-3d-after-cropping-scalar-range-shows-0-2-but-nothing-displays/44355

---

## Post #1 by @era_888 (2025-09-05 09:44 UTC)

<p>Hello everyone.<br>
I am working on a liver surgery simulation project. I have:</p>
<ul>
<li>
<p>Pre-operative MRI resampled to isotropic (<code>preop_n4_iso</code>)</p>
</li>
<li>
<p>Liver segmentation exported as labelmap (<code>liver_full_seg</code>)</p>
</li>
</ul>
<p>What I did:</p>
<ol>
<li>
<p>Resampled the segmentation with <strong>NearestNeighbor</strong> using <code>preop_n4_iso</code> as reference → got <code>liver_full_seg_iso</code></p>
</li>
<li>
<p>Cropped MRI (<code>preop_n4_iso_crop</code>, Linear) and mask (<code>liver_full_seg_iso_crop</code>, NearestNeighbor) with the same ROI</p>
</li>
<li>
<p>In <strong>Volumes → Information</strong>:</p>
<ul>
<li>
<p><code>liver_full_seg_iso_crop</code> shows <strong>Scalar Range = 0–2</strong>, valid dimensions and spacing (1 mm)</p>
</li>
<li>
<p>So it is not empty</p>
</li>
</ul>
</li>
<li>
<p>When I <strong>Import labelmap to Segmentation</strong>, I get Segment_1 and Segment_2, but neither looks like the full liver in 2D or 3D. ( There is no 3D liver at all is just showing a small thing</p>
</li>
<li>
<p>Clicking <strong>Show 3D</strong> shows nothing</p>
</li>
</ol>
<p>My question:</p>
<ul>
<li>
<p>Why doesn’t the liver appear in 3D even though Scalar Range = 0–2?</p>
</li>
<li>
<p>Did I crop incorrectly, or is my export wrong?</p>
</li>
<li>
<p>Should I re-export my liver segmentation as a binary (0/1) labelmap before resampling/cropping?</p>
</li>
</ul>
<p>I have attached screenshots showing the Volumes Information panel and the empty 3D view.</p>
<p>Any help to understand what I am doing wrong would be greatly appreciated, because Ive been doing the same things for more than 3 days and cannot find the solution.</p>
<p>Thank you!</p>

---

## Post #2 by @cpinter (2025-09-05 10:34 UTC)

<p>To facilitate the process I suggest that you at the least make some relevant screenshots, but if the issue can be reproduced with a saved MRB scene, even better (only anonymized data please). Thank you!</p>

---
