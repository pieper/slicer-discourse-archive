# How to get the position of the DICOM from the Mesh generated?

**Topic ID**: 35804
**Date**: 2024-04-29
**URL**: https://discourse.slicer.org/t/how-to-get-the-position-of-the-dicom-from-the-mesh-generated/35804

---

## Post #1 by @guilherme-francisco (2024-04-29 15:23 UTC)

<p>I’d like to know how the 3D Slicer gets the position of the CT images from the position of the 3d model generated. Exactly like the following image:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ea0ee1e4eadb93b4f98cc111e2f3600b2974d76.jpeg" data-download-href="/uploads/short-url/bdA26vvsN433f3wQVXXXSV61jsG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ea0ee1e4eadb93b4f98cc111e2f3600b2974d76_2_686x499.jpeg" alt="image" data-base62-sha1="bdA26vvsN433f3wQVXXXSV61jsG" width="686" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ea0ee1e4eadb93b4f98cc111e2f3600b2974d76_2_686x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ea0ee1e4eadb93b4f98cc111e2f3600b2974d76.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ea0ee1e4eadb93b4f98cc111e2f3600b2974d76.jpeg 2x" data-dominant-color="6A6162"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">807×588 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks in advance!</p>

---

## Post #2 by @muratmaga (2024-04-29 15:37 UTC)

<aside class="quote no-group" data-username="guilherme-francisco" data-post="1" data-topic="35804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/guilherme-francisco/48/70234_2.png" class="avatar"> guilherme-francisco:</div>
<blockquote>
<p>I’d like to know how the 3D Slicer gets the position of the CT images from the position of the 3d model generated. Exactly like the following image:</p>
</blockquote>
</aside>
<p>It is the other way around. It gets the whole geometry information from the CT image, and that geometry is used for generating the model.</p>

---

## Post #3 by @guilherme-francisco (2024-04-29 16:21 UTC)

<p>Hi Murat,<br>
Thanks for your quick reply. I think I wasn’t clear with my question, my ultimate goal with it was to understand how to map between a certain location in 3D to the series of CT images that 3D Slicer has.<br>
I’m developing a virtual reality application and what I want is that when the user is inside the 3d model, they can find themselves through the series of CT images similar to what 3d Slicer does.</p>
<p>What is the algorithm behind this transformation (3D → 2D images)?</p>

---

## Post #4 by @muratmaga (2024-04-29 16:24 UTC)

<aside class="quote no-group" data-username="guilherme-francisco" data-post="3" data-topic="35804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/guilherme-francisco/48/70234_2.png" class="avatar"> guilherme-francisco:</div>
<blockquote>
<p>I’m developing a virtual reality application and what I want is that when the user is inside the 3d model, they can find themselves through the series of CT images similar to what 3d Slicer does.</p>
</blockquote>
</aside>
<p>I am still not following what you want to do, but I have no experience with VR. Regardless, you probably should start by reviewing how different types of coordinate systems are mapped to each other in Slicer.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html">Coordinate systems — 3D Slicer documentation</a></p>

---

## Post #5 by @guilherme-francisco (2024-04-29 16:39 UTC)

<p>Thank you murat!<br>
I will check it out</p>

---

## Post #6 by @lassoan (2024-04-30 02:34 UTC)

<p>You can find code for napping between IJK voxel coordinates and physical RAS coordinates in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates">script repository</a>.</p>
<p>Are you using Slicer’s virtual reality extension? It can render everything that is in Slicer’s 3D view (including volume rendering, 4D animations, slice views, etc.) by a single click. Also, it is just really convenient that you can do everything - DICOM import, segmentation, quantification, surgical planning, real-time navigation, etc. - in a single environment. If you use Slicer for virtual reality then there is no need to export/import data but all data appears live in AR/VR, no need to use different programming languages (you can use Python, no need for C#), no need to redevelop all the medical imaging features in a game engine, etc.</p>

---
