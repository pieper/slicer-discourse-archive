---
topic_id: 22955
title: "3D Model Showing Up As A Line"
date: 2022-04-14
url: https://discourse.slicer.org/t/22955
---

# 3D model showing up as a line?

**Topic ID**: 22955
**Date**: 2022-04-14
**URL**: https://discourse.slicer.org/t/3d-model-showing-up-as-a-line/22955

---

## Post #1 by @ekt (2022-04-14 00:30 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.2<br>
I am trying to get a volume rendering of my image stack, but it just shows up as a single weird black line (see screenshot)? How do I fix this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2fd0eadc1aa344d055fb0e0cf719b3910b7bb67.png" data-download-href="/uploads/short-url/nfRwqE0mRBhigIBA5U66Mx6DpRB.png?dl=1" title="Screenshot 2022-04-13 164825" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2fd0eadc1aa344d055fb0e0cf719b3910b7bb67_2_690x374.png" alt="Screenshot 2022-04-13 164825" data-base62-sha1="nfRwqE0mRBhigIBA5U66Mx6DpRB" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2fd0eadc1aa344d055fb0e0cf719b3910b7bb67_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2fd0eadc1aa344d055fb0e0cf719b3910b7bb67_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2fd0eadc1aa344d055fb0e0cf719b3910b7bb67_2_1380x748.png 2x" data-dominant-color="8D8EA0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-04-13 164825</span><span class="informations">1920×1043 312 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-04-14 00:35 UTC)

<p>It seems that you don’t have an image stack but you loaded a single image slice. Use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#read-dicom-files-into-the-scene">DICOM module</a> for loading DICOM images and SlicerMorph extension’s <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks">ImageStacks module</a> to load a TIFF/PNG/JPG stack.</p>

---

## Post #3 by @ekt (2022-04-14 00:46 UTC)

<p>I do have an image stack (I can scroll through the images) that I loaded as a nrrd file</p>

---

## Post #4 by @lassoan (2022-04-14 18:15 UTC)

<p>The image that you loaded is a single slice, because it appears as a single line in the yellow slice view. If you load a 3D image volume then you see a 2D image in all slice views.</p>

---

## Post #5 by @ekt (2022-04-15 18:51 UTC)

<p>Ahh I see what you mean. I’m going to start from scratch and see if it does that again.</p>

---
