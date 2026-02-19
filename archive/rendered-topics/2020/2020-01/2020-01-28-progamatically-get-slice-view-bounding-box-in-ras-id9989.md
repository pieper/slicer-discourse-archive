---
topic_id: 9989
title: "Progamatically Get Slice View Bounding Box In Ras"
date: 2020-01-28
url: https://discourse.slicer.org/t/9989
---

# Progamatically get slice view bounding box in RAS

**Topic ID**: 9989
**Date**: 2020-01-28
**URL**: https://discourse.slicer.org/t/progamatically-get-slice-view-bounding-box-in-ras/9989

---

## Post #1 by @Felipe_Silveira (2020-01-28 19:34 UTC)

<p>Hi, I’d like to write a python script that gets the bounding box of a slice view.<br>
For example, with the attached images, I’d like to have 2 points: (-2.1, 133.1, -199.7) and (-2.1, -120.3, 178.3).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/2279cfa1ff2c86ef36cd7f464bd7af597907b1ad.jpeg" data-download-href="/uploads/short-url/4UZdcLNOJgEsxtu32bWZMEhAKXX.jpeg?dl=1" title="bottom_left" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2279cfa1ff2c86ef36cd7f464bd7af597907b1ad_2_643x499.jpeg" alt="bottom_left" data-base62-sha1="4UZdcLNOJgEsxtu32bWZMEhAKXX" width="643" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2279cfa1ff2c86ef36cd7f464bd7af597907b1ad_2_643x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2279cfa1ff2c86ef36cd7f464bd7af597907b1ad_2_964x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2279cfa1ff2c86ef36cd7f464bd7af597907b1ad_2_1286x998.jpeg 2x" data-dominant-color="444344"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bottom_left</span><span class="informations">1527×1187 296 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a8d8668938ff38c27db4348983f1ef1cb94207e.jpeg" data-download-href="/uploads/short-url/hu9sYBKc3XoxmKKid87ht6pPcGG.jpeg?dl=1" title="top_right" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a8d8668938ff38c27db4348983f1ef1cb94207e_2_644x499.jpeg" alt="top_right" data-base62-sha1="hu9sYBKc3XoxmKKid87ht6pPcGG" width="644" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a8d8668938ff38c27db4348983f1ef1cb94207e_2_644x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a8d8668938ff38c27db4348983f1ef1cb94207e_2_966x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a8d8668938ff38c27db4348983f1ef1cb94207e_2_1288x998.jpeg 2x" data-dominant-color="444344"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">top_right</span><span class="informations">1531×1187 294 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Using vtkMRMLSliceNode::GetXYZOrigin and applying the XYToRAS matrix gives me the bottom left corner. But I don’t see how to get the top right corner.<br>
I played around with the field of view, but didn’t get the right results when switching between axial/coronal/sagittal presets.</p>
<p>How can I accomplish that?</p>

---

## Post #2 by @fbordignon (2020-01-28 20:19 UTC)

<p>Get the RAS coordinates of the bottom left corner:</p>
<pre><code>xytoras = sliceNode.GetXYToRAS()
xytoras.MultiplyPoint((0, 0 , 0, 1))
</code></pre>
<p>Get the coordinate of the top right corner:</p>
<pre><code>dims = sliceNode.GetDimensions()
xytoras.MultiplyPoint((dims[0], dims[1] , 0, 1))</code></pre>

---
