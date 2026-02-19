---
topic_id: 32931
title: "Linking Slice Views To Cropped Volume Rendering"
date: 2023-11-21
url: https://discourse.slicer.org/t/32931
---

# Linking slice views to cropped volume rendering

**Topic ID**: 32931
**Date**: 2023-11-21
**URL**: https://discourse.slicer.org/t/linking-slice-views-to-cropped-volume-rendering/32931

---

## Post #1 by @muratmaga (2023-11-21 17:35 UTC)

<p>I am playing with this excellent zebrafish embryo dataset <a href="https://datadryad.org/stash/dataset/doi:10.5061/dryad.4nb12g2">Dryad | Data – Computational 3D histological phenotyping of whole zebrafish by X-ray histotomography (datadryad.org)</a></p>
<p>I can do nice surface visualization with volume rendering, but when I try to display internal detail, it is less than ideal and I am having a hard time finding a good property to give me the full detail I am seeing in the slice views.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/629d974dea1f1a4ea810a666d2a8ec7a49eb82e1.jpeg" data-download-href="/uploads/short-url/e4oqCmnbWmquTBadTL7d5N1RjHz.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/629d974dea1f1a4ea810a666d2a8ec7a49eb82e1_2_647x500.jpeg" alt="image" data-base62-sha1="e4oqCmnbWmquTBadTL7d5N1RjHz" width="647" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/629d974dea1f1a4ea810a666d2a8ec7a49eb82e1_2_647x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/629d974dea1f1a4ea810a666d2a8ec7a49eb82e1_2_970x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/629d974dea1f1a4ea810a666d2a8ec7a49eb82e1_2_1294x1000.jpeg 2x" data-dominant-color="4F4C55"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1756×1357 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>One way to deal with is to display the current slice view and line that up with the cropping ROI.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79732122f003f6c5ee6d53c2823536d1732ef67e.jpeg" data-download-href="/uploads/short-url/hkor8aQyL7jGMnaTNohgGl14XMy.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79732122f003f6c5ee6d53c2823536d1732ef67e_2_647x500.jpeg" alt="image" data-base62-sha1="hkor8aQyL7jGMnaTNohgGl14XMy" width="647" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79732122f003f6c5ee6d53c2823536d1732ef67e_2_647x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79732122f003f6c5ee6d53c2823536d1732ef67e_2_970x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79732122f003f6c5ee6d53c2823536d1732ef67e_2_1294x1000.jpeg 2x" data-dominant-color="50505B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1752×1353 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But then every time I have to move the ROI, I have to spend time to find a way to line that up with the matching slice. How slice is displayed in 3D is also depends on the FOV is 2D viewer (e.g., if you zoom in too far, then 3D gets cut.)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbce332c27adb4a36ab9a781ea0540b6b5f38931.jpeg" data-download-href="/uploads/short-url/t4WHSwG48vvNXHnqKcV2yTJkqsN.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbce332c27adb4a36ab9a781ea0540b6b5f38931_2_646x500.jpeg" alt="image" data-base62-sha1="t4WHSwG48vvNXHnqKcV2yTJkqsN" width="646" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbce332c27adb4a36ab9a781ea0540b6b5f38931_2_646x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbce332c27adb4a36ab9a781ea0540b6b5f38931_2_969x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbce332c27adb4a36ab9a781ea0540b6b5f38931_2_1292x1000.jpeg 2x" data-dominant-color="595861"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1746×1351 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a better way of achieving this visualization, and still maintain the ease of use of cropping in volume rendering.</p>

---

## Post #2 by @ebrahim (2023-11-21 18:31 UTC)

<p>Reminds me of what was being discussed <a href="https://discourse.slicer.org/t/rendering-mri-volume-using-python-from-nii-file/">here</a></p>
<p>It would be pretty nice to have a way of linking slice views and volume cropping!</p>

---

## Post #3 by @pieper (2023-11-21 19:00 UTC)

<p>Agreed, that would be a nice view mode.  Probably not terribly hard to implement.  It would be very easy to do a python hack if you need something quick, but a bit harder to make something that is cleanly integrated.</p>

---
