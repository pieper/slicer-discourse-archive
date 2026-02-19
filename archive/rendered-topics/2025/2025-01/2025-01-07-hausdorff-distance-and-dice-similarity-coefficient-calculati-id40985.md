---
topic_id: 40985
title: "Hausdorff Distance And Dice Similarity Coefficient Calculati"
date: 2025-01-07
url: https://discourse.slicer.org/t/40985
---

# Hausdorff Distance and Dice Similarity Coefficient calculations

**Topic ID**: 40985
**Date**: 2025-01-07
**URL**: https://discourse.slicer.org/t/hausdorff-distance-and-dice-similarity-coefficient-calculations/40985

---

## Post #1 by @juy13 (2025-01-07 14:06 UTC)

<p>Hello,</p>
<p>I am currently working on histology mapping onto radiology using Python. I am looking to do DSC and Hausdorff distance calculations for the mappings but encountered a few issues. I want to be able to do a Hausdorff distance calculation of the histology slide segment (with a certain threshold applied) against the original CT segment (with another threshold applied), however, Slicer’s module only does 3D calculations. I tried to pass it into a Python script to do so but learnt that I could not properly export the histology .tif file into a .nii labelmap, but I could with the CT segmentation.</p>
<p>Does anyone have a workaround/an idea about how I might go about this?</p>
<p>Cheers</p>

---

## Post #2 by @lassoan (2025-01-07 14:25 UTC)

<p>While we recommend using .nrrd instead of .nii due to ambiguities and other issues of .nii file format, you can and <em>export</em> a segmentation to a .nii file (or export the segmentation to a labelmap volume and then <em>save</em> that as .nii).</p>
<p>All Slicer features work in 3D and in some cases these don’t work for 2D images. This is the case for DSC and HD metric computations. One solution is to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume">export the segmentation using the histology slice as reference</a> and then compute the error metric in Python. For HD computation, make sure you use a package that takes image spacing into account (such as <a href="https://simpleitk.org/doxygen/latest/html/classitk_1_1simple_1_1HausdorffDistanceImageFilter.html">ITK/SimpleITK</a>. If you use a tool that cannot deal with image spacing (such as most scipy processing functions) then you may need to resample the images.</p>

---

## Post #3 by @juy13 (2025-01-07 20:31 UTC)

<p>When you say export the segmentation, you mean export only the CT scan segmentation and keep the histology slide unsegmented? One of the issues I had with exporting was also that I could not segment out the histology label (which was a yellow colour) from its background (which was white) and therefore to work around this I had to get rid of the background in Photoshop. But I believe what you are suggesting is that I keep the histology slide as it is with its original background, and then export the CT segmentation reference to the full size histology slide. Does this ensure that the alignment of the two images stays the same, and when exporting the segmentation, does it only pull out the 2D slice that is on the same plane as the histology slice?</p>
<p>Thank you for your help!</p>

---

## Post #4 by @lassoan (2025-01-07 20:40 UTC)

<aside class="quote no-group" data-username="juy13" data-post="3" data-topic="40985">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/juy13/48/79040_2.png" class="avatar"> juy13:</div>
<blockquote>
<p>When you say export the segmentation, you mean export only the CT scan segmentation and keep the histology slide unsegmented?</p>
</blockquote>
</aside>
<p>For DSC and HD metrics, you need to segment both.</p>
<aside class="quote no-group" data-username="juy13" data-post="3" data-topic="40985">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/juy13/48/79040_2.png" class="avatar"> juy13:</div>
<blockquote>
<p>One of the issues I had with exporting was also that I could not segment out the histology label (which was a yellow colour) from its background (which was white) and therefore to work around this I had to get rid of the background in Photoshop.</p>
</blockquote>
</aside>
<p>You can use <code>Vector to scalar volume</code> module to get a color channel or combination of channels from a color image that makes it easy to distinguish the background.</p>
<p>I would not recommend to use Photoshop for processing biomedical images. It is not intended to work on such images and may change your data in unexpected ways.</p>
<aside class="quote no-group" data-username="juy13" data-post="3" data-topic="40985">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/juy13/48/79040_2.png" class="avatar"> juy13:</div>
<blockquote>
<p>Does this ensure that the alignment of the two images stays the same, and when exporting the segmentation, does it only pull out the 2D slice that is on the same plane as the histology slice?</p>
</blockquote>
</aside>
<p>Yes, you get the reformatted image slice from of the CT that exactly matches the geometry (position, orientation, spacing, extent) of the histology slice.</p>

---

## Post #5 by @juy13 (2025-01-08 03:45 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/500d392b8f5f7c03f6f37dd02f528d17b662ad6e.png" data-download-href="/uploads/short-url/bqawLrhlFYG1DNKZ3yTV2QihDMq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/500d392b8f5f7c03f6f37dd02f528d17b662ad6e.png" alt="image" data-base62-sha1="bqawLrhlFYG1DNKZ3yTV2QihDMq" width="400" height="213"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">400×213 31.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05270a6e2e22c330401ca146dba59a936a555188.png" data-download-href="/uploads/short-url/JA1Y5gS22k8ndU9XAAizysI1HW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05270a6e2e22c330401ca146dba59a936a555188.png" alt="image" data-base62-sha1="JA1Y5gS22k8ndU9XAAizysI1HW" width="389" height="276"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">389×276 30.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi Andras, I am exporting the bone CT segmentation out with reference to the histology slide (S9) volume. However I get two error messages - one saying that the geometry does not fit into the new one and therefore it would need a crop (which I assume is because the CT’s cross sectional image is larger than the histology slide), and this one that I have pasted suggesting my RAM is not enough. Is there a workaround to this? I would have thought my 40gb of RAM in this computer would be enough. The settings I am using to export the CT segmentation are above as well.</p>
<p>Cheers</p>

---
