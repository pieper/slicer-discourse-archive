---
topic_id: 2931
title: "Create A Volumetric Mesh"
date: 2018-05-25
url: https://discourse.slicer.org/t/2931
---

# Create a volumetric mesh

**Topic ID**: 2931
**Date**: 2018-05-25
**URL**: https://discourse.slicer.org/t/create-a-volumetric-mesh/2931

---

## Post #1 by @Hikmat (2018-05-25 14:07 UTC)

<p>Operating system: Windows 10<br>
Slicer version: Slicer 4.8.1</p>
<p>I have clipped a ScalarVolumeNode to define the region of interest. I would now like to create a volumetric mesh from this scalar volume. I am aware of tools and methods to create a surface model (ie. grayMaker, modelMaker). However, are there any tools for volumetric meshes? I have tried Cleaver Tet Mesher but with no success.</p>
<p>Thanks.</p>

---

## Post #2 by @Michael_Hardisty (2018-05-25 15:37 UTC)

<p>Hi Hikmat,</p>
<p>I have previously used cleaver to generate a volumetric mesh.  There is previous discussion on discourse about this, here is the relevant text:</p>
<p>“I tried using cleaver with limited success. I had a lot of trouble with the extension initially. After I spoke with Andras Lasso I was able to get the meshing working. The main thing I did to get cleaver to work with my data was to create a label map with a value of 75 on the inside and -75 on the outside. I used simple filters to do the shifting and scaling.”</p>
<p>Here is a link to the discussion:  <a href="https://discourse.slicer.org/t/usage-of-volumetric-meshes/620/3">https://discourse.slicer.org/t/usage-of-volumetric-meshes/620/3</a></p>
<p>Best,</p>
<p>Michael</p>

---

## Post #3 by @lassoan (2018-05-25 15:56 UTC)

<p>Segment mesher extension greatly simplifies volumetric mesh generation. It can create volumetric meshes directly from segmentation nodes. It takes care of creating image data in the format that Cleaver2 expects.</p>
<p>If your input is a surface mesh in a model node then you can convert it to segmentation node using Segmentations module.</p>

---

## Post #4 by @Hikmat (2018-05-25 18:02 UTC)

<p>Thanks Andras, this works great.</p>
<p>I now have an overlay of my surface model and the corresponding volumetric mesh.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f50d0bf0eb56644bd8a530efee9e780e85eb0603.jpeg" data-download-href="/uploads/short-url/yXOVON0KIzFwjzUB0WswHHAzcpZ.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f50d0bf0eb56644bd8a530efee9e780e85eb0603_2_690x380.jpg" alt="image" data-base62-sha1="yXOVON0KIzFwjzUB0WswHHAzcpZ" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f50d0bf0eb56644bd8a530efee9e780e85eb0603_2_690x380.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f50d0bf0eb56644bd8a530efee9e780e85eb0603_2_1035x570.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f50d0bf0eb56644bd8a530efee9e780e85eb0603.jpeg 2x" data-dominant-color="89899B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1190×656 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I would like to “fuse” their properties: the surface mesh defines only the exterior whereas the volumetric mesh discretizes the interior structure.</p>
<p>Is there a way to manipulate the volumetric mesh (or the surface mesh) in Slicer so that I have a model whose exterior is well-visualized (as in the surface mesh) but whose interior structure is also defined (as in the volumetric mesh)?</p>

---

## Post #5 by @lassoan (2018-05-25 18:17 UTC)

<p>For visualization, I would only use surface meshes. Why do you need volumetric meshes for visualization?</p>

---

## Post #6 by @Hikmat (2018-05-25 18:29 UTC)

<p>I am writing a simulator for decompression surgery - in which a lamina needs to be removed (laminectomy).<br>
I have created a tool that “grinds” away at the bone surface - kind of like an “Erasing” tool.</p>
<p>Although I agree that a surface mesh is adequate for visualization, the spine would be a hollow structure and thus not a useful representation for laminectomy. Thus, it would be nice if I had a “solid” model so that there would be underlying layers of bone as the surface is grinded away at.</p>

---

## Post #7 by @lassoan (2018-05-25 19:09 UTC)

<p>For all these you don’t need a volumetric mesh. Segment Editor can do volumetric visualization already. Enable “Show 3D”, maybe disable smoothing to make updates faster (you can later set up volume rendering to make 3D updates even faster). You can use the Erase effect with a sphere option to grind bone.</p>

---

## Post #8 by @Hikmat (2018-05-25 19:23 UTC)

<p>This is exactly what I needed and the Erase tool is a huge plus.<br>
Wish I had known this beforehand so that I didn’t have to develop my own Erase tool.<br>
Thanks Andras; it is much appreciated.</p>

---

## Post #9 by @cpinter (2018-08-28 13:19 UTC)

<p>A post was merged into an existing topic: <a href="/t/convert-a-surface-mesh-to-a-volumetric-mesh-in-3dslicer/1416/6">Convert a surface mesh to a volumetric mesh in 3DSLICER</a></p>

---
