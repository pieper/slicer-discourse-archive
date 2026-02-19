---
topic_id: 42372
title: "How To Use 3Dslicer Software To Accurately Convert Stl Forma"
date: 2025-03-30
url: https://discourse.slicer.org/t/42372
---

# How to use 3dslicer software to accurately convert STL format files into nii format files

**Topic ID**: 42372
**Date**: 2025-03-30
**URL**: https://discourse.slicer.org/t/how-to-use-3dslicer-software-to-accurately-convert-stl-format-files-into-nii-format-files/42372

---

## Post #1 by @lirongyaoper (2025-03-30 14:15 UTC)

<p>Dear teacher, hello, recently I am doing 3D reconstruction, and some STL files need to be converted into NII format files. I tried to convert them through 3Dslicer software, but the results were not satisfactory.<br>
I would like to ask all teachers if there is a particularly good way to do this conversion accurately. Thank you.</p>

---

## Post #2 by @pieper (2025-03-30 17:44 UTC)

<p>Since STL files contain triangulated surfaces they can’t be exactly represented in nii format, which is voxel based.  You can choose to rasterize at higher resolution by changing the geometry of the segmentation using the Segment Editor.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b57016e9a8294d29737f48dbf8bc80f998636d25.jpeg" data-download-href="/uploads/short-url/pT4zvR77yE9gFB2dyKQ5punhtUV.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b57016e9a8294d29737f48dbf8bc80f998636d25_2_690x409.jpeg" alt="image" data-base62-sha1="pT4zvR77yE9gFB2dyKQ5punhtUV" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b57016e9a8294d29737f48dbf8bc80f998636d25_2_690x409.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b57016e9a8294d29737f48dbf8bc80f998636d25_2_1035x613.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b57016e9a8294d29737f48dbf8bc80f998636d25.jpeg 2x" data-dominant-color="D6D6D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1352×802 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
