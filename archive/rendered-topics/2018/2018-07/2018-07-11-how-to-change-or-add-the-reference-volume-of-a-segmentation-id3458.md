---
topic_id: 3458
title: "How To Change Or Add The Reference Volume Of A Segmentation"
date: 2018-07-11
url: https://discourse.slicer.org/t/3458
---

# How to change or add the Reference Volume of a Segmentation?

**Topic ID**: 3458
**Date**: 2018-07-11
**URL**: https://discourse.slicer.org/t/how-to-change-or-add-the-reference-volume-of-a-segmentation/3458

---

## Post #1 by @MMMPPPMMM (2018-07-11 12:07 UTC)

<p>How do I change or add the Reference Volume of an Active Segmentation?</p>
<p><strong>Change?</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6860054b9602b1150597ded981c271fc69912a3.png" data-download-href="/uploads/short-url/uBLh3zes6j8DSm8L5NigjRayNtF.png?dl=1" title="Change_Reference_Volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6860054b9602b1150597ded981c271fc69912a3_2_690x256.png" alt="Change_Reference_Volume" data-base62-sha1="uBLh3zes6j8DSm8L5NigjRayNtF" width="690" height="256" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6860054b9602b1150597ded981c271fc69912a3_2_690x256.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6860054b9602b1150597ded981c271fc69912a3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6860054b9602b1150597ded981c271fc69912a3.png 2x" data-dominant-color="C4CACC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Change_Reference_Volume</span><span class="informations">886×330 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Add?</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c034f3798d069a39e4da9f9ad99d144b2a529d42.png" data-download-href="/uploads/short-url/rql7wXAsPRYqVMWqAvSY9onsUYa.png?dl=1" title="Add_Reference_Volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c034f3798d069a39e4da9f9ad99d144b2a529d42_2_690x272.png" alt="Add_Reference_Volume" data-base62-sha1="rql7wXAsPRYqVMWqAvSY9onsUYa" width="690" height="272" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c034f3798d069a39e4da9f9ad99d144b2a529d42_2_690x272.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c034f3798d069a39e4da9f9ad99d144b2a529d42.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c034f3798d069a39e4da9f9ad99d144b2a529d42.png 2x" data-dominant-color="BEC3CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Add_Reference_Volume</span><span class="informations">884×349 75.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2018-07-12 03:04 UTC)

<p>Currently, there is no easy way to change it (you need to create a new segmentation, set reference volume, and copy segments into it). However, <a class="mention" href="/u/cpinter">@cpinter</a> has <a href="https://github.com/Slicer/Slicer/pull/975">recently implemented this</a>. It should be available in the nightly build within days.</p>

---

## Post #3 by @MMMPPPMMM (2018-07-12 09:52 UTC)

<p>Thanks, looking forward to test this.</p>

---

## Post #4 by @lassoan (2018-07-26 12:45 UTC)

<p>Changing geometry of segmentation binary labelmap representation to match a volume’s geometry is now available in nightly builds. Click the button on the right side of the master volume node selector in Segment Editor module.</p>

---
