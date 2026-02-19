---
topic_id: 28177
title: "How To Create This Type Of View Of Fastsurfer Segmented Volu"
date: 2023-03-05
url: https://discourse.slicer.org/t/28177
---

# How to create this type of view of Fastsurfer segmented volume

**Topic ID**: 28177
**Date**: 2023-03-05
**URL**: https://discourse.slicer.org/t/how-to-create-this-type-of-view-of-fastsurfer-segmented-volume/28177

---

## Post #1 by @mukund_shah (2023-03-05 00:30 UTC)

<p>I have Fastsurfer segmentation map(nifti format) of a T1 brain volume ,how do i create a view that looks like the image below.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb9c3dc182a6fc11bdc43f0f6a5a92abd5394e58.jpeg" alt="image" data-base62-sha1="t3dFEp1mcxnfRzqRowKkoDmouFO" width="484" height="256"></p>

---

## Post #2 by @Sunderlandkyl (2023-03-06 20:34 UTC)

<p>Try dragging and dropping the nifti into Slicer and selecting “Segmentation” as the description. If you have SlicerFreeSurfer installed, you can click “Show options” in the top right, and then select “FreeSurferLabels” for the color node to get the correct segment names.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4798e45eab9535b9df0a49c57845d0efd47810e.png" data-download-href="/uploads/short-url/s2610jrk4sd44JI7CowQrfBzJhA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4798e45eab9535b9df0a49c57845d0efd47810e.png" alt="image" data-base62-sha1="s2610jrk4sd44JI7CowQrfBzJhA" width="690" height="70" data-dominant-color="F5F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1186×122 6.75 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>To show the segments in 3D, you can go to the Segmentations module and click “Show 3D”.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcc00ba26d41927cdd2cbc4d3cf9be802555cbf6.png" alt="image" data-base62-sha1="A3VMeJpJDuPV4JnkttSLUSZygdg" width="509" height="45"></p>

---
