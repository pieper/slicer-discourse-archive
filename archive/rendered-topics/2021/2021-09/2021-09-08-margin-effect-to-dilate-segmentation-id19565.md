# Margin effect to dilate segmentation

**Topic ID**: 19565
**Date**: 2021-09-08
**URL**: https://discourse.slicer.org/t/margin-effect-to-dilate-segmentation/19565

---

## Post #1 by @Mgi (2021-09-08 10:39 UTC)

<p>Hi everyone,<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/157f5a64170d1d25cf5f19ed7246a97d1faec259.jpeg" alt="margin" data-base62-sha1="34aSxf5eGF8J1IllBhX8GfAleEV" width="537" height="216"></p>
<p>I’m using 3d slicer, 4.11.20200930 version on windows 10. When I use the Margin effect tool to dilate a segmentation I defined a margin size of 1.01 mm. However, below it appears “Actual: 0.5 x 0.5 x 1.0 mm (1 x 1 x 1 pixel)”. I attached an image.</p>
<p>I want to dilate the segmentation by 1 voxel, Is the margin size correct? Why appear 0.5 x 0.5 mm?</p>

---

## Post #2 by @Mgi (2021-09-08 10:40 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>! Could you help me? please!</p>

---

## Post #3 by @lassoan (2021-09-08 13:46 UTC)

<p>There have been fixes in this logic. Please try the latest Slicer Stable Release and latest Slicer Preview Release to see if they work as you expect.</p>
<p>Note that you can only add a margin to labelmap representations that is 2x the voxel size. If you need a different margin size then you either have to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">modify the voxel size in the segmentation</a> or export the segmentation to a model and apply a VTK filter there (this latter requires a few lines of Python scripting).</p>

---

## Post #4 by @Mgi (2021-09-08 22:08 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>! I tried in the latest Slicer stable release but It appears the same. I want to study the repeatability of radiomics features when the segmentation is dilated. Then I think the plane dilation with 1 pixel will be well.</p>

---

## Post #5 by @lassoan (2021-09-09 01:14 UTC)

<p>Could you please try with the latest preview release?</p>

---
