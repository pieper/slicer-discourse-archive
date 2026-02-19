---
topic_id: 26143
title: "Problems With Flood Filling Module"
date: 2022-11-08
url: https://discourse.slicer.org/t/26143
---

# Problems with flood filling module

**Topic ID**: 26143
**Date**: 2022-11-08
**URL**: https://discourse.slicer.org/t/problems-with-flood-filling-module/26143

---

## Post #1 by @Ekaterina_Savkina (2022-11-08 14:42 UTC)

<p>Hello, I am the beginner in 3d Slicer.<br>
I wanted to use flood filling module. I’ve chosen  range of intensities and have chosen the voxel on image.But when clicking on some points nothing happened, and on some points the rectangular region is segmented. What does that mean?  I hoped region with the same intensity as I’ve clicked.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae76ce2d028fdf99f7da2e56214f41ed62913783.png" data-download-href="/uploads/short-url/oTnCocnfocL6TsrHJq24SXYEcYH.png?dl=1" title="Снимок" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae76ce2d028fdf99f7da2e56214f41ed62913783_2_690x326.png" alt="Снимок" data-base62-sha1="oTnCocnfocL6TsrHJq24SXYEcYH" width="690" height="326" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae76ce2d028fdf99f7da2e56214f41ed62913783_2_690x326.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae76ce2d028fdf99f7da2e56214f41ed62913783_2_1035x489.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae76ce2d028fdf99f7da2e56214f41ed62913783.png 2x" data-dominant-color="8A8A90"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Снимок</span><span class="informations">1364×645 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-11-08 14:47 UTC)

<p>Based on the screenshot, Flood filling seems to work as it is intended. You can see in the yellow slice view that only soft tissue is added to the segment (because the relatively large Intensity Tolerance value allowed to include all soft tissues, but bones have much higher intensity).</p>
<p>The rectangular region is there because the segmentation’s extent is smaller than the image that is currently chosen as the master volume. See how to change this in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">Segment Editor module documentation</a>.</p>

---

## Post #3 by @Ekaterina_Savkina (2022-11-10 13:43 UTC)

<p>Thanks a lot! I’ve understand what you means. I’ll listen to all tutorial about segment editor and will return if have a problem.</p>

---
