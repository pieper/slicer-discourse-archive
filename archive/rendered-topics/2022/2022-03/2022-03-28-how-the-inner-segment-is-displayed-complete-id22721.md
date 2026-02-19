---
topic_id: 22721
title: "How The Inner Segment Is Displayed Complete"
date: 2022-03-28
url: https://discourse.slicer.org/t/22721
---

# How the inner segment is displayed complete

**Topic ID**: 22721
**Date**: 2022-03-28
**URL**: https://discourse.slicer.org/t/how-the-inner-segment-is-displayed-complete/22721

---

## Post #1 by @zl980215 (2022-03-28 11:18 UTC)

<p>Operating system:Ubuntu-20.04<br>
Slicer version:SLicer-4.13.0<br>
Expected behavior:Internal segment display complete<br>
Actual behavior:If you set the outer segment transparency to 0 and the inner segment transparency to 0.5, and then rotate the entire 3D model, the internal segment is incomplete at a certain angle. However, if the external segment is set to 0 in the 3D view or the transparency is also set to 0.5, the internal segment will not be in this situation. How to display the internal segment in its entirety with an external segment visibility of 1 but a transparency of 0?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c8de807229709d0c9b2e25e802ebbbe75cdf011.jpeg" data-download-href="/uploads/short-url/1N3Lhv0lYP6CRJzpzAh4vyhbh2p.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8de807229709d0c9b2e25e802ebbbe75cdf011_2_582x500.jpeg" alt="image" data-base62-sha1="1N3Lhv0lYP6CRJzpzAh4vyhbh2p" width="582" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8de807229709d0c9b2e25e802ebbbe75cdf011_2_582x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c8de807229709d0c9b2e25e802ebbbe75cdf011.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c8de807229709d0c9b2e25e802ebbbe75cdf011.jpeg 2x" data-dominant-color="1D1F1F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">671×576 50 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56b23074bc16509fe1a27412c7fd41f50171fac6.png" alt="image" data-base62-sha1="cmWPxg5s1cMlnlEswLCWEWaFZrM" width="626" height="494"></p>

---

## Post #2 by @pieper (2022-03-28 11:33 UTC)

<p>Make sure depth peeling is enabled for the 3D view.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view</a></p>

---

## Post #3 by @zl980215 (2022-03-29 02:39 UTC)

<p>Why is the internal segment display incomplete when the deep peeling switch is turned on, but not when it is turned off?</p>

---
