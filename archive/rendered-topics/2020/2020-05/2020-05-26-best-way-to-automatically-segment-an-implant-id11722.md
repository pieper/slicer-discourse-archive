---
topic_id: 11722
title: "Best Way To Automatically Segment An Implant"
date: 2020-05-26
url: https://discourse.slicer.org/t/11722
---

# Best way to automatically segment an implant

**Topic ID**: 11722
**Date**: 2020-05-26
**URL**: https://discourse.slicer.org/t/best-way-to-automatically-segment-an-implant/11722

---

## Post #1 by @Amn3s14 (2020-05-26 20:34 UTC)

<p>Hello, I am looking for the best way to automatically segment a breast implant, or atleast by using minimal user interaction. I have been trying region growing or fast marching approaches with poor success. I am using MRI data. Any input or advice would be greatly appreciated! Thank you.</p>

---

## Post #2 by @pieper (2020-05-26 20:55 UTC)

<p>There might be intensity inhomogeneity, so <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/N4ITKBiasFieldCorrection">the N4</a> algorithm might help the intensity-based segmentation methods do better.  Also since the implants are probably very smooth compared to tissue you could maybe try <a href="https://pyradiomics.readthedocs.io/en/latest/usage.html#voxel-based-extraction">voxel-based radiomics</a>.</p>

---

## Post #3 by @lassoan (2020-05-27 04:16 UTC)

<p>Could you post a few screenshots (or links to publicly available images) so that we can see what could be the main challenges? I would expect that “Grow from seeds” or “Watershed” effects can segment it quite well.</p>

---

## Post #4 by @Amn3s14 (2020-05-28 22:38 UTC)

<p>I am trying to develop a way to measure the implant volume using minimal user input. Using grow from seeds on some small circles placed inside and outside the implant, I can get slices that are perfect, like <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c27cae0325e29fb66fcc1cd72e07356072e88fe5.png" data-download-href="/uploads/short-url/rKvKLN8SQmspz9eIwUUcIqiYxKZ.png?dl=1" title="growcircles" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c27cae0325e29fb66fcc1cd72e07356072e88fe5_2_690x373.png" alt="growcircles" data-base62-sha1="rKvKLN8SQmspz9eIwUUcIqiYxKZ" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c27cae0325e29fb66fcc1cd72e07356072e88fe5_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c27cae0325e29fb66fcc1cd72e07356072e88fe5_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c27cae0325e29fb66fcc1cd72e07356072e88fe5_2_1380x746.png 2x" data-dominant-color="9E9EA0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">growcircles</span><span class="informations">1920×1040 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But then other slices look like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ab8676570608976eb210809c81d95e21547cf40.png" data-download-href="/uploads/short-url/m4IC44ZKFPW5OyFQQ9Tqc5iaZWg.png?dl=1" title="growcircles2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ab8676570608976eb210809c81d95e21547cf40_2_690x374.png" alt="growcircles2" data-base62-sha1="m4IC44ZKFPW5OyFQQ9Tqc5iaZWg" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ab8676570608976eb210809c81d95e21547cf40_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ab8676570608976eb210809c81d95e21547cf40_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ab8676570608976eb210809c81d95e21547cf40_2_1380x748.png 2x" data-dominant-color="9F9EA0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">growcircles2</span><span class="informations">1920×1042 348 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The boundaries are well defined so I’m not sure why it’s leaking so much in the second image. The volume calculation is returning 110cc and should be 95 cc (before adjusting for spacing), so this error is really significant. I’d really appreciate any help.</p>

---

## Post #5 by @lassoan (2020-05-29 01:02 UTC)

<p>When contrast between the tissue and implant is not strong enough then seeds may grow into incorrect regions. All you need to do is paint with more seeds (after initializing Grow from seeds, but before clicking Apply), until the segmentation is good. You might also try to slightly increase “Seed locality” parameter, which localizes growth more around the placed seeds (especially useful when you have fairly homogeneous regions in an image). I would also recommend to enable 3D preview to find obvious errors quickly, without the need to scroll through a lot of slices.</p>
<p>You might also try Watershed effect, which is similar to Grow from seeds, but you can enforce spatial smoothness constrain (“object size” parameter), so it is less likely to leak. The disadvantage of this effect is that it is much slower than Grow from seeds. You need to install SegmentEditorExtraEffects extension for Watershed effect to appear in the Segment Editor.</p>

---
