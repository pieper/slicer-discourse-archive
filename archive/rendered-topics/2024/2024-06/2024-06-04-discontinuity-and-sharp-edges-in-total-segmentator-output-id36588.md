---
topic_id: 36588
title: "Discontinuity And Sharp Edges In Total Segmentator Output"
date: 2024-06-04
url: https://discourse.slicer.org/t/36588
---

# Discontinuity and sharp edges in Total Segmentator output

**Topic ID**: 36588
**Date**: 2024-06-04
**URL**: https://discourse.slicer.org/t/discontinuity-and-sharp-edges-in-total-segmentator-output/36588

---

## Post #1 by @farzad2020 (2024-06-04 13:45 UTC)

<p>Hi,</p>
<p>I am using the automated segmentation tool (total segmentator); however, after getting the segmented body, there are some discountiniouty in the organs or some sharp edges (for instance, on the ribs). Since I have a vast data set, I’m wondering if there is an automated tool for smoothing the sharp edges or filling in the discontinuities.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2024-06-04 13:46 UTC)

<p>This is probably normal. If you provide a few screenshots then we may be able to tell more.</p>

---

## Post #3 by @farzad2020 (2024-06-04 14:09 UTC)

<p>Thanks for your reply.</p>
<p>I’ve attached where there is a sharp edge as well as where there is a discontinuity ( a yellowish spot is hanging). The point is that I would use the segmented and exported stl models for EM simulation where volume meshing is needed, and the meshing of these sharp edges is a bit tricky.</p>
<p>Is there an automatic way to use the Python console to solve them in the 3D slicer before exporting the STL models?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57ace0480aa4a874f083e631242448802e670432.png" data-download-href="/uploads/short-url/cvBVmId5fw9xCx6Q78kHr7DZwwa.png?dl=1" title="01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57ace0480aa4a874f083e631242448802e670432_2_690x344.png" alt="01" data-base62-sha1="cvBVmId5fw9xCx6Q78kHr7DZwwa" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57ace0480aa4a874f083e631242448802e670432_2_690x344.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57ace0480aa4a874f083e631242448802e670432.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57ace0480aa4a874f083e631242448802e670432.png 2x" data-dominant-color="7B6E62"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01</span><span class="informations">859×429 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30b819cb834867cb7ee9d5b3fc7add972d5ce08b.png" data-download-href="/uploads/short-url/6WZlRyZ4hozdw9LMgOdhUV57p2P.png?dl=1" title="02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30b819cb834867cb7ee9d5b3fc7add972d5ce08b_2_690x469.png" alt="02" data-base62-sha1="6WZlRyZ4hozdw9LMgOdhUV57p2P" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30b819cb834867cb7ee9d5b3fc7add972d5ce08b_2_690x469.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30b819cb834867cb7ee9d5b3fc7add972d5ce08b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30b819cb834867cb7ee9d5b3fc7add972d5ce08b.png 2x" data-dominant-color="918170"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">02</span><span class="informations">737×501 226 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2024-06-04 15:51 UTC)

<p>This looks normal. The tiny pieces are just due to very small (size of few voxels) noise on the surface and result of surface smoothing. It should not affect the interpretation or analysis of the data in any way.</p>
<p>If you want to control these small details then there are several things you can do. For example, you can use <code>Smoothing</code> effect in <code>Segment Editor</code> module to make the surface smoother. You can also adjust <code>Smoothing factor</code> in the drop-down menu of <code>Show 3D</code> button.</p>
<p>What is your clinical application? How would you like to use the segmentation result? What size of segmentation errors do you consider acceptable? What is the resolution of your input image?</p>

---
