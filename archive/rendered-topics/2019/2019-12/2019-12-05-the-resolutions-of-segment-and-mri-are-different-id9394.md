---
topic_id: 9394
title: "The Resolutions Of Segment And Mri Are Different"
date: 2019-12-05
url: https://discourse.slicer.org/t/9394
---

# The resolutions of segment and mri are different

**Topic ID**: 9394
**Date**: 2019-12-05
**URL**: https://discourse.slicer.org/t/the-resolutions-of-segment-and-mri-are-different/9394

---

## Post #1 by @Crispy13 (2019-12-05 07:33 UTC)

<p>Operating system: Win 10 Pro x64<br>
Slicer version: 4.10.2<br>
Expected behavior:</p>
<p>Actual behavior:</p>
<p>Some segmentation file resolutions are different with originial mri image resolutions.<br>
ex1) mri - (150, 512, 512) / seg - (44, 101, 101)</p>
<p>This seems to happen to the most of the segmentation files with multiple segmentations.<br>
I created multiple nodes for each tumor and merged them into one node. Was this the cause for it?</p>
<p>Is there any way to fit seg’s res to mri’s? and if the above method causes problems, how do i make a segmentation file with multiple segmentations?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2019-12-05 07:37 UTC)

<p>The segmentation’s resolution matches the master volume’s resolution but the extent is cropped to the minimum necessary by default (the origin is adjusted accordingly, so the segment’s physical position remains correct). You can export the segmentation to labelmap volume before saving it if you prefer saving the blank parts of the segmentation (so that extents are exactly the same as the master volume’s).</p>
<p>We see that many users are surprised by this behavior, so we will change it to not crop to minimum extent by default (see <a href="https://discourse.slicer.org/t/segmentation-image-size/9364" class="inline-onebox">Segmentation image size</a>).</p>

---

## Post #3 by @Crispy13 (2019-12-05 08:29 UTC)

<p>Thank you for explanation.<br>
Then is it impossible to fit the resolution of segmentation which was saved already to that of mri image in this situation?</p>

---

## Post #4 by @lassoan (2019-12-05 14:21 UTC)

<aside class="quote no-group" data-username="Crispy13" data-post="3" data-topic="9394">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/crispy13/48/5316_2.png" class="avatar"> Crispy13:</div>
<blockquote>
<p>Then is it impossible to fit the resolution of segmentation which was saved already to that of mri image in this situation?</p>
</blockquote>
</aside>
<p>It is not just possible but very easy to do. In Segmentations module Export/import section, choose your MRI image as reference volume before clicking Export button:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3937cde893dee3fa32d8964a5d2d17265eb20a1d.png" data-download-href="/uploads/short-url/8aaM76p03GgV3L4fWHH6FtXFW4R.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3937cde893dee3fa32d8964a5d2d17265eb20a1d_2_313x500.png" alt="image" data-base62-sha1="8aaM76p03GgV3L4fWHH6FtXFW4R" width="313" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3937cde893dee3fa32d8964a5d2d17265eb20a1d_2_313x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3937cde893dee3fa32d8964a5d2d17265eb20a1d_2_469x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3937cde893dee3fa32d8964a5d2d17265eb20a1d_2_626x1000.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">787×1257 51.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Crispy13 (2019-12-05 14:59 UTC)

<p>I appreciate your help.<br>
I solved this with your answer.</p>

---
