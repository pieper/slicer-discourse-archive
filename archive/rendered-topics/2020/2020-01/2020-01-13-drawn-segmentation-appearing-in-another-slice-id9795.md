# Drawn segmentation appearing in another slice

**Topic ID**: 9795
**Date**: 2020-01-13
**URL**: https://discourse.slicer.org/t/drawn-segmentation-appearing-in-another-slice/9795

---

## Post #1 by @DanTran (2020-01-13 16:47 UTC)

<p>Hi, I have an issue with the draw feature for one DICOM set. Every time I draw a segmentation, it disappears from the slice I work on and appears on the next slice. How can I fix it? Thanks.</p>

---

## Post #2 by @lassoan (2020-01-13 18:51 UTC)

<p>Can you try with latest Slicer Preview Release?<br>
Also try if the problem is fixed if you slightly reposition slice views using Shift + Mouse Move.</p>
<p>Could you check if the slice view is positioned at the boundary between two slices? Zoom in a slice view, turn off interpolation in slice view controller (so that you can see each pixel edge) and display slice intersections (crosshair toolbar’s drop-down menu) - you will see if slice intersection line goes through the center of pixels or at the boundary.</p>

---

## Post #3 by @juday (2020-01-13 21:59 UTC)

<p>I too had similar issue. Solution that worked for me was to drag the slice position to either of the extremes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a778ec73aa3066f34bd6970f5fd4ab799fb76ca1.png" data-download-href="/uploads/short-url/nTwOxTlgNvX51jeKPIdFBkDp6HT.png?dl=1" title="Slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a778ec73aa3066f34bd6970f5fd4ab799fb76ca1_2_690x106.png" alt="Slicer" data-base62-sha1="nTwOxTlgNvX51jeKPIdFBkDp6HT" width="690" height="106" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a778ec73aa3066f34bd6970f5fd4ab799fb76ca1_2_690x106.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a778ec73aa3066f34bd6970f5fd4ab799fb76ca1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a778ec73aa3066f34bd6970f5fd4ab799fb76ca1.png 2x" data-dominant-color="976763"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer</span><span class="informations">700×108 5.37 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
