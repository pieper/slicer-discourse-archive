---
topic_id: 44955
title: "How To Calculate The Internal Cranial Volume Space Occupied"
date: 2025-11-03
url: https://discourse.slicer.org/t/44955
---

# How to calculate the internal cranial volume (space occupied by the brain) in 3D Slicer

**Topic ID**: 44955
**Date**: 2025-11-03
**URL**: https://discourse.slicer.org/t/how-to-calculate-the-internal-cranial-volume-space-occupied-by-the-brain-in-3d-slicer/44955

---

## Post #1 by @Luz_Velasco (2025-11-03 21:45 UTC)

<p>Hello everyone,</p>
<p>I have a 3D CT scan of a skull (without the brain visible), and I would like to calculate the <em>internal cranial volume</em> — that is, the volume corresponding to the space where the brain would normally be located inside the skull.</p>
<p>Is there any tool or recommended workflow in 3D Slicer that allows me to compute this internal volume?<br>
For example, is it possible to segment the inner surface of the cranial cavity and then calculate the enclosed volume?</p>
<p>Any guidance or suggested modules (e.g., Segment Editor, Segment Statistics, or other approaches) would be greatly appreciated.</p>
<p>Thank you very much for your help!</p>

---

## Post #2 by @muratmaga (2025-11-04 06:12 UTC)

<p>You can use <strong>SurfaceWrapSolidify</strong> extension to fill the cranial cavity, and extra an endocast. Then you can use the <code>SegmentStatistics</code> module to calculate the volume of the endocast.</p>
<p>There is also a SlicerMorph module called SegmentEndocranium, which under the hood uses the SurfaceWrapSolidify.</p>

---

## Post #3 by @philippepellerin (2025-11-05 11:03 UTC)

<p>This is the right tool, indeed, but to have an accurate result, you must segment the skull itself, remove the spine, and have the setting like that.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/1934264d23bb3c65231e50d7ca623969ca1298f8.png" data-download-href="/uploads/short-url/3AXFl9WJTtkXnNHObbz9S9hXUco.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/1934264d23bb3c65231e50d7ca623969ca1298f8_2_690x365.png" alt="image" data-base62-sha1="3AXFl9WJTtkXnNHObbz9S9hXUco" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/1934264d23bb3c65231e50d7ca623969ca1298f8_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/1934264d23bb3c65231e50d7ca623969ca1298f8_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/1934264d23bb3c65231e50d7ca623969ca1298f8.png 2x" data-dominant-color="E3E3E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1170×620 67.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
