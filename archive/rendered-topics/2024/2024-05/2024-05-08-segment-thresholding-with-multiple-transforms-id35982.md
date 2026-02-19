---
topic_id: 35982
title: "Segment Thresholding With Multiple Transforms"
date: 2024-05-08
url: https://discourse.slicer.org/t/35982
---

# Segment thresholding with multiple transforms

**Topic ID**: 35982
**Date**: 2024-05-08
**URL**: https://discourse.slicer.org/t/segment-thresholding-with-multiple-transforms/35982

---

## Post #1 by @bruce (2024-05-08 01:34 UTC)

<p>Hello</p>
<p>This might be a bit obscure but I note inconsistent behaviour with the Segment Editor Threshold tool when working with a segmentation based on a volume with nested transforms. In particular, the thresholding range is unusable (both limits stuck as one extreme) when the source volume had both a grid and linear transform applied to it (see screenshots below). The order of the linear and grid transforms doesn’t appear to affect the outcome. If either of the transforms are applied to the volume individually (or indeed, two nested linear transforms are applied) the thresholding works as expected.</p>
<p>Maybe I doing something wrong? Is this known behaviour? The solution might be to harden the grid transform before segmentation but I was intrigued by the inconsistency.</p>
<p><strong>Transform heirarchy:</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e86d3bfaa37f3403b3fd4d4b54e09143ab5f0839.png" alt="image" data-base62-sha1="xa8O0kAp8MR1yLJWwzgPajEiMc1" width="402" height="117"></p>
<p><strong>Segment Editor</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77d0d4dcd0012af2d930ad462051d875cb892fd7.png" alt="image" data-base62-sha1="h5WeMozLIAFv1VxMlgj07Viof2v" width="398" height="276"></p>

---

## Post #2 by @muratmaga (2024-05-08 02:51 UTC)

<p>Both of those transforms require interpolation, which will change the intensity values. so it makes sense that threshold volume is having a hard time doing that on the fly.<br>
Is there a reason why you are not working with the hardened volume?</p>

---

## Post #3 by @bruce (2024-05-08 20:21 UTC)

<p>Thanks for your response.<br>
Yes, that makes sense. I only raised this out of curiousity as I’d identified it when extending one of our existing scripted processes. We can adjust our script to harden all transforms before segmentation.</p>

---
