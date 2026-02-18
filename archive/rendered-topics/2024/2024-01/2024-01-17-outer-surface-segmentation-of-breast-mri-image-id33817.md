# Outer surface segmentation of breast MRI image

**Topic ID**: 33817
**Date**: 2024-01-17
**URL**: https://discourse.slicer.org/t/outer-surface-segmentation-of-breast-mri-image/33817

---

## Post #1 by @Miri_Trope (2024-01-17 08:37 UTC)

<p>Hello everyone, apologies if this question has been asked frequently. I’m a newcomer to Slicer and seeking guidance on extracting the outer surface (skin) to obtain a smoothed mesh, particularly for a breast MRI scan. I’ve attempted methods like wrap solidify and fill between slices, and the provided image shows the result I’ve achieved. Could you recommend both manual and automatic approaches for this task? I’m also exploring MONAI and wondering if it offers any solutions. Your assistance is greatly appreciated!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79bbc4de7d23b75bd584df41c1a9dc78003e926a.jpeg" data-download-href="/uploads/short-url/hmU4aif8axTludEJLJKcs8fg7AC.jpeg?dl=1" title="Screenshot 2024-01-17 at 10.29.18" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79bbc4de7d23b75bd584df41c1a9dc78003e926a_2_612x500.jpeg" alt="Screenshot 2024-01-17 at 10.29.18" data-base62-sha1="hmU4aif8axTludEJLJKcs8fg7AC" width="612" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79bbc4de7d23b75bd584df41c1a9dc78003e926a_2_612x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79bbc4de7d23b75bd584df41c1a9dc78003e926a_2_918x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79bbc4de7d23b75bd584df41c1a9dc78003e926a_2_1224x1000.jpeg 2x" data-dominant-color="3B3F42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-01-17 at 10.29.18</span><span class="informations">1458×1190 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Miri_Trope (2024-01-18 06:52 UTC)

<p>any of your comments would be greatly appriciated.</p>

---

## Post #3 by @jumbojing (2024-01-18 12:12 UTC)

<p>you can try to  <a href="https://github.com/lassoan/SlicerTotalSegmentator" rel="noopener nofollow ugc">lassoan/SlicerTotalSegmentator: Fully automatic total body segmentation in 3D Slicer using “TotalSegmentator” AI model (github.com)</a></p>

---

## Post #4 by @mangotee (2024-01-19 13:19 UTC)

<p>Goog idea, <a class="mention" href="/u/jumbojing">@jumbojing</a>, but I don’t think that TotalSegmentator will be a solution here - it is useful for larger FOVs in CT, but this is a relatively small FOV (breast) and MRI.</p>
<p><a class="mention" href="/u/miri_trope">@Miri_Trope</a> - looking at your scans, I would personally try to intensity-threshold the whole volume to separate the body from the air, then close holes with the Margin effect (first grow with 3-5mm margin size, then shrink again with the exact same margin size). This should get rid of most holes stemming from vessels. Further issues can likely be fixed by the Wrap Solidify effect.<br>
The only thing I don’t see an obvious solution to, is how to segment the two breast regions away from the torso, but perhaps you already have a solution for that (judging from the green view panel). <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
