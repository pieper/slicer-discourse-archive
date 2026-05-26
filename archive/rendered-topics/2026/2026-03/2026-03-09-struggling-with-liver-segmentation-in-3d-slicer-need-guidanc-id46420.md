---
topic_id: 46420
title: "- Struggling With Liver Segmentation in 3D Slicer — Need Guidance"
date: 2026-03-09
url: https://discourse.slicer.org/t/46420
last_bumped: 2026-03-10T17:57:27.714Z
---

# - Struggling With Liver Segmentation in 3D Slicer — Need Guidance

**Topic ID**: 46420
**Date**: 2026-03-09
**URL**: https://discourse.slicer.org/t/struggling-with-liver-segmentation-in-3d-slicer-need-guidance/46420

---

## Post #1 by @Marco_Ribeiro_Silva (2026-03-09 22:40 UTC)

<p>Hello everybody</p>
<p>I’m currently struggling to find up‑to‑date datasets to learn how to segment the liver in 3D Slicer. Many of the extensions I come across are outdated, incompatible, or no longer maintained, which makes the learning process quite challenging.</p>
<p>I’m looking for guidance on reliable tutorials, recommended workflows, and effective approaches to improve my skills. Any help or shared resources would be greatly appreciated.<br>
My best regards</p>

---

## Post #2 by @pieper (2026-03-09 23:51 UTC)

<p>How detailed do your segmentations need to be?  TotalSegmentator does a pretty good job at the overall organ, and not so bad for the vessels if you scans have good contrast.  There are also several tumor segmentation models out there you could try.  There’s one in Auto3DSeg I think and probably in mhub too.  In terms of datasets there are a lot in the Imaging Data Commons.</p>

---

## Post #3 by @Marco_Ribeiro_Silva (2026-03-10 14:09 UTC)

<p>My main goal is to <strong>3D‑print the segmented liver and present it to the medical team during the pre‑operative planning meeting</strong>. The idea is simply to give them a <strong>physical sense of the anatomy</strong> — ultra‑high precision isn’t required, but <strong>clearly identifying all 8 liver segments is essential</strong>.</p>
<p>I would really appreciate guidance on:</p>
<ul>
<li>
<p>reliable and current tutorials</p>
</li>
<li>
<p>recommended workflows for liver segmentation</p>
</li>
<li>
<p>datasets that still work with the latest versions of 3D Slicer</p>
</li>
<li>
<p>any effective approaches you’ve used in similar projects</p>
</li>
</ul>
<p>Any help or shared resources would be greatly appreciated.</p>
<hr>
<h2><a name="p-132535-h-1" class="anchor" href="#p-132535-h-1" aria-label="Heading link"></a></h2>

---

## Post #4 by @pieper (2026-03-10 15:42 UTC)

<p>You can definitely do that with TotalSegmenator.</p>
<p><a href="https://discourse.slicer.org/t/new-extension-fully-automatic-whole-body-ct-segmentation-in-2-minutes-using-totalsegmentator/26710">https://discourse.slicer.org/t/new-extension-fully-automatic-whole-body-ct-segmentation-in-2-minutes-using-totalsegmentator/26710</a></p>
<p>Here’s an example I did recently with it:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/379b76f63a59c57ecea0281a7948a5810728707f.jpeg" data-download-href="/uploads/short-url/7VVlemF6wSOF9D28cRpCYGBhdbp.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/379b76f63a59c57ecea0281a7948a5810728707f_2_469x500.jpeg" alt="image" data-base62-sha1="7VVlemF6wSOF9D28cRpCYGBhdbp" width="469" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/379b76f63a59c57ecea0281a7948a5810728707f_2_469x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/379b76f63a59c57ecea0281a7948a5810728707f_2_703x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/379b76f63a59c57ecea0281a7948a5810728707f_2_938x1000.jpeg 2x" data-dominant-color="4A4543"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1092×1163 302 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In terms of datasets, you can look on the <a href="https://portal.imaging.datacommons.cancer.gov/">Imaging Data Commons</a> and related resources.</p>

---

## Post #5 by @Marco_Ribeiro_Silva (2026-03-10 17:51 UTC)

<p>Thank you very much . I´ll dig into into it asap . The lobes , how you manage to differentiate them ?</p>

---

## Post #6 by @pieper (2026-03-10 17:57 UTC)

<aside class="quote no-group" data-username="Marco_Ribeiro_Silva" data-post="5" data-topic="46420">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/marco_ribeiro_silva/48/82062_2.png" class="avatar"> Marco_Ribeiro_Silva:</div>
<blockquote>
<p>The lobes , how you manage to differentiate them ?</p>
</blockquote>
</aside>
<p>That’s all handled automatically by the tool.</p>

---
