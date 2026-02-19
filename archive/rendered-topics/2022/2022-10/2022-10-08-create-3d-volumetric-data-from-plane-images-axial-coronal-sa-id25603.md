---
topic_id: 25603
title: "Create 3D Volumetric Data From Plane Images Axial Coronal Sa"
date: 2022-10-08
url: https://discourse.slicer.org/t/25603
---

# Create 3d volumetric data from plane images (Axial, Coronal, Sagittal)

**Topic ID**: 25603
**Date**: 2022-10-08
**URL**: https://discourse.slicer.org/t/create-3d-volumetric-data-from-plane-images-axial-coronal-sagittal/25603

---

## Post #1 by @Muhammed_Fatih_Talu (2022-10-08 11:06 UTC)

<p>I have three 2d projection images (Axial, Coronal and Sagittal).<br>
I want to generate 3d volumetric data using these images.<br>
Is there a ready module that I can use in Slicer?<br>
Or is there any method you would recommend?<br>
Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/affb0c3ecab1d5f2ff9ee30d6e4b7ad4656b665e.jpeg" data-download-href="/uploads/short-url/p6Nql2ZjzwHstkkSKsizBmOoKGq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/affb0c3ecab1d5f2ff9ee30d6e4b7ad4656b665e_2_502x500.jpeg" alt="image" data-base62-sha1="p6Nql2ZjzwHstkkSKsizBmOoKGq" width="502" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/affb0c3ecab1d5f2ff9ee30d6e4b7ad4656b665e_2_502x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/affb0c3ecab1d5f2ff9ee30d6e4b7ad4656b665e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/affb0c3ecab1d5f2ff9ee30d6e4b7ad4656b665e.jpeg 2x" data-dominant-color="5D5D75"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">624×621 79.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Melodicpinpon (2023-10-25 14:21 UTC)

<p>Same question:<br>
As dicoms are often difficult of access; I import series of images (.png) into Slicer and can segment them.<br>
As Blender also has a function to create a mesh from a volume (VolumeToMesh modifier), I would like to try it using these image stacks.<br>
(It would also make the visualisation fully three dimensional (no more transparency-effect from the side-views).</p>
<p>The problem is that I don’t know how to generate a .vdb file from my image stacks.</p>
<p>Is there a way to do this conversion of .png stack images into a single .vdb volume in Slicer?</p>

---

## Post #3 by @lassoan (2023-10-26 02:34 UTC)

<p>I think the question of the original poster was about reconstructing a volume from 3 projection images, which is generally not possible (the information is just too sparse).</p>
<p>Regarding volum rendering in Blender. Considering <a href="https://discourse.slicer.org/t/screen-space-ambient-occlusion-for-volume-rendering/32323/26">Slicer’s most recent volume rendering improvements</a>, Blender’s volume rendering may be a downgrade. Converting a volume to mesh is such a tremendous amount of information loss that you probably want to avoid. Instead, you can augment your volume rendering with the information you get from segmentation.</p>
<p>Anyway, if you want to try what Blender can do with volumes, you can load an image stack into Slicer, export it into mha or nrrd format, load it into ParaView, and save as .vdb format. If you come up with something nice then please post it (probably in a new topic, as this topic is not about high-quality volume rendering).</p>

---
