---
topic_id: 42350
title: "Why Stripping Lines Show Up After Using Applytransform Comma"
date: 2025-03-28
url: https://discourse.slicer.org/t/42350
---

# Why stripping lines show up after using ApplyTransform command?

**Topic ID**: 42350
**Date**: 2025-03-28
**URL**: https://discourse.slicer.org/t/why-stripping-lines-show-up-after-using-applytransform-command/42350

---

## Post #1 by @aiden.zhu (2025-03-28 20:28 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11<br>
Expected behavior: smoothy interpolation<br>
Actual behavior: strip-line shows up</p>
<p>I did use with python code (3D-image):<br>
transform2Node = slicer.mrmlScene.AddNode(slicer.vtkMRMLTransformNode())<br>
then<br>
transformStitchNode.ApplyTransform( myTransform )<br>
it is observed that some strip-lines show up like this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/545ebe90f342637ee21b6732ee6498e4a2d6a3c7.jpeg" data-download-href="/uploads/short-url/c2n5YMoBOk4K0xagtSdeNj9AXr1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/545ebe90f342637ee21b6732ee6498e4a2d6a3c7_2_568x500.jpeg" alt="image" data-base62-sha1="c2n5YMoBOk4K0xagtSdeNj9AXr1" width="568" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/545ebe90f342637ee21b6732ee6498e4a2d6a3c7_2_568x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/545ebe90f342637ee21b6732ee6498e4a2d6a3c7_2_852x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/545ebe90f342637ee21b6732ee6498e4a2d6a3c7_2_1136x1000.jpeg 2x" data-dominant-color="6F6E6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1497×1316 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
so Question:<br>
Need I pre-define some interpolation method? and how?</p>

---

## Post #2 by @pieper (2025-03-29 23:10 UTC)

<p>Please try the latest versions (5.8.1 and the latest preview builds).  If you still see the issue, try to reproduce it with publicly shareable data and the exact steps to reproduce.</p>

---

## Post #3 by @lassoan (2025-03-31 20:11 UTC)

<p>It seems to me that image interpolation is disabled! Image interpolation should never be disabled, as interpolation is required to see the original continuous physical image signal. See more detailed explanation here:</p>
<aside class="quote quote-modified" data-post="10" data-topic="13918">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/volume-display-interpolate-turned-off-by-default-in-newest-stable/13918/10">Volume display - Interpolate turned off by default in newest stable?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Interpolated image shows you the faithfully reconstructed continuous signal from the discrete samples. This reconstruction is lossless if sample-rate criterion is satisfied (see more details <a href="https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem">here</a>). The criterion is not always satisfied - that’s when you see staircase artifacts in the reconstructed image (in both slice views, volume rendering, and reconstructed surfaces): 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e2131f4e5e4dfc53650494641005ab3d8014a49.jpeg" data-download-href="/uploads/short-url/8RCIQSyJC6Le9lCBgPunGs1bNq1.jpeg?dl=1" title="image">[image]</a> 
Interpolation is still about the best thing you can do, and definitely provides much more faithful reconstruction …
  </blockquote>
</aside>

<p>If you disable interpolation then you will see discrete sample values and the abrupt intensity change at the boundary of every voxel, which were not present in the original continuous physical signal. The diagonal lines are also voxel boundaries, they appear like this when the slice view orientation is not aligned with the volume axis orientation. These lines are not real, they appear because you chose to see the sampled values instead of the reconstructed continuous signal.</p>
<p>So, everything is good, just make sure to keep interpolation enabled if you want to see the actual image (not the raw data that has not been reconstructed into image signal yet).</p>

---

## Post #4 by @aiden.zhu (2025-04-03 13:58 UTC)

<p>Thanks a lot. Not big issue anyway. Yes, interpolation will be there applied to get such lines off. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
