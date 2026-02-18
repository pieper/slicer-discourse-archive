# Slicer vmtk centerline network model in coronary artery

**Topic ID**: 41619
**Date**: 2025-02-11
**URL**: https://discourse.slicer.org/t/slicer-vmtk-centerline-network-model-in-coronary-artery/41619

---

## Post #1 by @yoonjh119 (2025-02-11 01:41 UTC)

<p>I am extracting the centerline through a network model based on coronary artery segmentation including the aorta. When extracting the centerline, the centerline of the aorta-LM connection (red arrow) often deviates from the mask. When I looked through the forum, it said that oversampling could be a solution, so I oversampled and compared the results (2x, 3x), but the same problem occurred. Do you have a recommended solution to avoid this problem?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d07591e4b0f51c2ef2c3dd761e44db59bbc0e21b.jpeg" data-download-href="/uploads/short-url/tK7cMBFAopb1My3tiybmRcqR3Xd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d07591e4b0f51c2ef2c3dd761e44db59bbc0e21b_2_690x310.jpeg" alt="image" data-base62-sha1="tK7cMBFAopb1My3tiybmRcqR3Xd" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d07591e4b0f51c2ef2c3dd761e44db59bbc0e21b_2_690x310.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d07591e4b0f51c2ef2c3dd761e44db59bbc0e21b_2_1035x465.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d07591e4b0f51c2ef2c3dd761e44db59bbc0e21b_2_1380x620.jpeg 2x" data-dominant-color="9096BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1972×887 342 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2025-02-11 19:56 UTC)

<p>Have you tried the ‘Tree’ centerline extraction? This mode accounts for blood flow, while the ‘Network’ mode is based on geometry. We see that twisted locations pointed by your arrows become problematic, though I don’t know the exact cause of unexpected result.</p>

---

## Post #3 by @yoonjh119 (2025-02-13 11:35 UTC)

<p>Yes. We tried it with the tree algorithm, but the centerline is not output to the thin part of the coronary artery, so we are considering extracting the centerline with the network.</p>

---
