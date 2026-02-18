# Aligning PET image with CT

**Topic ID**: 42444
**Date**: 2025-04-05
**URL**: https://discourse.slicer.org/t/aligning-pet-image-with-ct/42444

---

## Post #1 by @imbeatriz (2025-04-05 14:01 UTC)

<p>Hi everyone,</p>
<p>This may seem like a simple question but I am having trouble understanding how to do it correctly on 3D Slicer.</p>
<p>I have a CT image with the following .mhd file description:</p>
<p>ObjectType = Image<br>
NDims = 3<br>
BinaryData = True<br>
BinaryDataByteOrderMSB = False<br>
CompressedData = False<br>
TransformMatrix = 1 0 0 0 1 0 0 0 1<br>
Offset = 91.654800415039062 140.35000610351562 -140.18800354003906<br>
CenterOfRotation = 0 0 0<br>
AnatomicalOrientation = LPI<br>
ElementSpacing = 2.2100000381469727 2.2100000381469727 2.2100000381469727<br>
DimSize = 125 122 93<br>
ElementType = MET_FLOAT<br>
ElementDataFile = ct_pet_y90.raw</p>
<p>However, on Volume Information on 3D Slicer, a different Image offset and matrix show up:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db2e3d1b19a40032fb4854b315cc4da17d650cd1.png" data-download-href="/uploads/short-url/vgXDbjkNVHPGC5hFqn4dCFpt7Oh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db2e3d1b19a40032fb4854b315cc4da17d650cd1.png" alt="image" data-base62-sha1="vgXDbjkNVHPGC5hFqn4dCFpt7Oh" width="452" height="286"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">452×286 78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am trying to align this CT image with my obtained reconstruction PET image, which has this image info:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/accb13c6efee0213e9e8fb986191042ec8ccc33c.png" data-download-href="/uploads/short-url/oEBdo1FL4h8mNl8QQaSX7y3rkiU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/accb13c6efee0213e9e8fb986191042ec8ccc33c.png" alt="image" data-base62-sha1="oEBdo1FL4h8mNl8QQaSX7y3rkiU" width="443" height="285"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">443×285 76.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The offset on the .hdr headfile says that it’s zero. However, when opening it on 3D Slicer it shows different values, as you can see.</p>
<p>I tried applying a Linear Transformation, but I still can’t seem to get them aligned correctly. Can someone please help me do this? I would really appreciate any insights.</p>
<p>Thank you!</p>
<p>Greetings,<br>
Beatriz</p>

---

## Post #2 by @cpinter (2025-04-11 12:25 UTC)

<p>Based on the fact that instead of DICOM you use a research file format, I assume that these two images do not come from a PET-CT machine (that ensures that the two images have the same frame of reference), but two different machines. In that case you’ll need to align the two volumes yourself. However, the two modalities are very different, and manual alignment may not be possible without some landmarks.<br>
Using the sliders in the Transforms module is very inconvenient for this. I suggest using the recently added transform interactions. You can turn it on in the Data module after right-clicking the eye in the row of the volume you want to move:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab4d78d40b6022ed81ca3c2f70f7e03f1429ea72.png" data-download-href="/uploads/short-url/orpD5iqu81jhOtHajhYna73nLh0.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab4d78d40b6022ed81ca3c2f70f7e03f1429ea72.png" alt="image" data-base62-sha1="orpD5iqu81jhOtHajhYna73nLh0" width="277" height="134"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">277×134 3.32 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(We should really update this section to contain this information: <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#manual-registration" class="inline-onebox">Registration — 3D Slicer documentation</a>)</p>
<p>By the way the different origin is simply due to the LPS-RAS conversion. Read about this <a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html">here</a>.</p>

---
