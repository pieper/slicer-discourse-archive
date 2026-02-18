# Erasing Segments for 3D View

**Topic ID**: 29866
**Date**: 2023-06-06
**URL**: https://discourse.slicer.org/t/erasing-segments-for-3d-view/29866

---

## Post #1 by @cy787 (2023-06-06 15:38 UTC)

<p>Hi all! I’m new to 3D Slicer and am trying to create a 3D rendering of a set of lungs and the airways. I tried to use the Fill Between Slices feature from the Segment Editor, but it created this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6957bdc23c2a278205094ad934bb13f93cf24b32.png" data-download-href="/uploads/short-url/f1U7o0e4Pl1mRNwIUI3M8iclkkO.png?dl=1" title="Screenshot 2023-06-06 101736" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6957bdc23c2a278205094ad934bb13f93cf24b32_2_519x500.png" alt="Screenshot 2023-06-06 101736" data-base62-sha1="f1U7o0e4Pl1mRNwIUI3M8iclkkO" width="519" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6957bdc23c2a278205094ad934bb13f93cf24b32_2_519x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6957bdc23c2a278205094ad934bb13f93cf24b32.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6957bdc23c2a278205094ad934bb13f93cf24b32.png 2x" data-dominant-color="8589AF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-06 101736</span><span class="informations">768×739 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there any way to delete the extra airways the tool created?</p>
<p>Thanks!</p>

---

## Post #2 by @mikebind (2023-06-06 19:07 UTC)

<p>A simple approach which looks like it would work for your data (as long as the airway you care about is one contiguous piece and it’s the biggest one) is to use the Islands tool and click “Keep largest island”.</p>

---

## Post #3 by @cy787 (2023-06-06 19:09 UTC)

<p>Thanks! I’ll try that!</p>

---

## Post #4 by @lassoan (2023-06-06 23:21 UTC)

<p>“Fill between slices” connects even small speckles. If you want to prevent the effect from creating those long spikes from tiny segmentation errors, you can remove those speckles using Smoothing effect. You can also exclude the blue segments from “Fill between slices” effect by hiding the blue segment before initializing the effect.</p>
<p>Note that you can segment lung and airways fully automatically in Slicer using “LungCTAnalyzer” extension.</p>

---
