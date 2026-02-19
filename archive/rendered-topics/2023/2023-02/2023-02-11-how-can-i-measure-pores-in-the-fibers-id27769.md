---
topic_id: 27769
title: "How Can I Measure Pores In The Fibers"
date: 2023-02-11
url: https://discourse.slicer.org/t/27769
---

# How Can I measure Pores in the fibers?

**Topic ID**: 27769
**Date**: 2023-02-11
**URL**: https://discourse.slicer.org/t/how-can-i-measure-pores-in-the-fibers/27769

---

## Post #1 by @Poorya_Esmaili (2023-02-11 13:56 UTC)

<p>Hello<br>
I want to analyze poros in the fiber. My intention is that in the poros section of the fiber what is the size of sphere that I can fit in the each pore are. is it possible in 3D slicer??<br>
I would be appreciated it if you help me…</p>

---

## Post #2 by @Poorya_Esmaili (2023-02-12 18:34 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/493840d5f3dca79bce970cfbff611995a5dc9818.jpeg" data-download-href="/uploads/short-url/arJnoKwLSnye0zcrTf6NycJkLnq.jpeg?dl=1" title="3D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/493840d5f3dca79bce970cfbff611995a5dc9818_2_690x491.jpeg" alt="3D" data-base62-sha1="arJnoKwLSnye0zcrTf6NycJkLnq" width="690" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/493840d5f3dca79bce970cfbff611995a5dc9818_2_690x491.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/493840d5f3dca79bce970cfbff611995a5dc9818_2_1035x736.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/493840d5f3dca79bce970cfbff611995a5dc9818.jpeg 2x" data-dominant-color="8690AD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D</span><span class="informations">1277×909 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @ahmad_alminnawi (2024-04-12 12:55 UTC)

<p>Hi, were you able to do it? I have a similar situation. I am more interested in the diameter than the volume (if that is easier) please let me know if you have the solution</p>

---

## Post #4 by @mikebind (2024-04-17 01:46 UTC)

<p>You might take a look at VMTK.  One output of pre-processing there is a voronoi skeleton, which is a connected 3D surface of maximal inscribed sphere centers, and I believe that the radius of these spheres is recorded.  You might be able to extract local peaks in radius for each pore.  VMTK is oriented towards analyzing single or branching vessels, so it is not an exact match, but the voronoi skeleton sounds very like what you would need. VMTK computes the skeleton for the interior of the object, so you would need to invert your segmentation first, otherwise you will get the maximal radii of the fibers rather than the gaps between fibers.</p>

---
