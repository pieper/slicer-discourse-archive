---
topic_id: 19750
title: "Whats The Different Between Show3D Smooth And The Segments S"
date: 2021-09-19
url: https://discourse.slicer.org/t/19750
---

# What's the different between show3D smooth and the segment's smooth?

**Topic ID**: 19750
**Date**: 2021-09-19
**URL**: https://discourse.slicer.org/t/whats-the-different-between-show3d-smooth-and-the-segments-smooth/19750

---

## Post #1 by @timeanddoctor (2021-09-19 23:01 UTC)

<p>I created a segment and show a well smooth 3D model with smooth factor=0.7. However, when I try to use the segment smooth(median,joint smoothing or closing) and the smooth factor=0 of show3D, the model seems very rough. I also tried the surface tool smooth(under smooth factor=0 of show3D), and the result still was very rough.<br>
So, what’s the vtk smoother or the pipeline of the show3D?<br>
Thanks!</p>

---

## Post #2 by @timeanddoctor (2021-09-19 23:09 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ebe57b43a6434cf8e5db3fbf835a7fd38512395.jpeg" data-download-href="/uploads/short-url/26quu8UIjGdgOtlFITjekVMUSvr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ebe57b43a6434cf8e5db3fbf835a7fd38512395_2_690x260.jpeg" alt="image" data-base62-sha1="26quu8UIjGdgOtlFITjekVMUSvr" width="690" height="260" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ebe57b43a6434cf8e5db3fbf835a7fd38512395_2_690x260.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ebe57b43a6434cf8e5db3fbf835a7fd38512395_2_1035x390.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ebe57b43a6434cf8e5db3fbf835a7fd38512395.jpeg 2x" data-dominant-color="B7B8C3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1178×444 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2021-09-21 16:52 UTC)

<p>Surface smoothing is required for reconstructing a continuous surface mesh from discrete samples stored in a labelmap volume. This smoothing <strong>does not remove any details from the segmentation</strong>. If you set surface smoothing to 0 then you will see the discrete samples instead of the reconstructed surface (each voxel of the labelmap will appear as a cube).</p>
<p>Smoothing effect is for <strong>removing irrelevant details</strong> (i.e., surface noise, speckled, small holes) from the segmentation.</p>

---

## Post #4 by @timeanddoctor (2021-09-22 03:58 UTC)

<p>Thank you very much!</p>

---
