---
topic_id: 18931
title: "Reslice Driver Disable Rotation"
date: 2021-07-26
url: https://discourse.slicer.org/t/18931
---

# Reslice Driver Disable Rotation

**Topic ID**: 18931
**Date**: 2021-07-26
**URL**: https://discourse.slicer.org/t/reslice-driver-disable-rotation/18931

---

## Post #1 by @jasmine-lou (2021-07-26 19:31 UTC)

<p>Hi everyone!</p>
<p>I was wondering if there was a way to disable the rotation of the CTs when using the Reslice Driver in IGT? Right now I understand that the CTs are rotating based on the rotation of the tool, but it can appear very unintuitive at times. Is there an easy way that I could disable the rotational component and only have the slices scroll based on where the tool is depth-wise? Thanks!</p>

---

## Post #2 by @lassoan (2021-07-26 21:20 UTC)

<p>If you have a 6-DOF tool, such as a stylus then you can rotate the views by rotating the tool.</p>
<p>If you have a 5-DOF tool or the user wants to specify reslicing with a single direction (e.g., C-arm rotation angle) then you need to specify how you want to constraint the up direction to make the oblique views easier to interpret. See a full working example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-slice-position-and-orientation-from-a-normal-vector-and-position">here</a>.</p>

---

## Post #3 by @jasmine-lou (2021-07-27 18:05 UTC)

<p>Thanks so much for the response. I have a 6-DOF tool but I do NOT want to rotate the views when I rotate the tool. Is there any way/how would I implement that?</p>

---

## Post #4 by @lassoan (2021-07-27 18:13 UTC)

<p>Yes, you can use the code snippet that I referenced above.</p>
<p>Note that you can also use the anatomical axis-locked modes of Volume Reslice Driver module. Or you can show the slices in 3D view - then you don’t need rotation at all because the slice is displayed in its physical location.</p>

---

## Post #5 by @jasmine-lou (2021-07-27 20:08 UTC)

<p>Where is the axis-locked mode located? Thanks!</p>

---

## Post #6 by @lassoan (2021-07-27 23:03 UTC)

<p>You can choose a slice view to be locked to an anatomical axis (and only adjust the position of the slice with the pointer) here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c1fcb2208856ba6fd833192fe1bf6736c9b32dd.png" data-download-href="/uploads/short-url/1JfQvp4wddgg5lLINeNCxIKs7Jr.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c1fcb2208856ba6fd833192fe1bf6736c9b32dd_2_511x499.png" alt="image" data-base62-sha1="1JfQvp4wddgg5lLINeNCxIKs7Jr" width="511" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c1fcb2208856ba6fd833192fe1bf6736c9b32dd_2_511x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c1fcb2208856ba6fd833192fe1bf6736c9b32dd_2_766x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c1fcb2208856ba6fd833192fe1bf6736c9b32dd.png 2x" data-dominant-color="9B9792"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">787×769 35.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @jasmine-lou (2021-07-28 19:59 UTC)

<p>Thanks so much for the help!</p>

---
