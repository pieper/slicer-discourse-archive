---
topic_id: 24751
title: "How To Generate A Surface Mesh From Segmentation"
date: 2022-08-14
url: https://discourse.slicer.org/t/24751
---

# How to generate a surface mesh from segmentation

**Topic ID**: 24751
**Date**: 2022-08-14
**URL**: https://discourse.slicer.org/t/how-to-generate-a-surface-mesh-from-segmentation/24751

---

## Post #1 by @joanne40226 (2022-08-14 10:35 UTC)

<p>Hi, recently i’m building mesh from segmetation. However i only need the informations of the voxel/vertex  on the surface. So, i’m wondering if there is a way to only generate surface mesh from a segmented 3D model? Thank you for your time.</p>

---

## Post #2 by @cpinter (2022-08-14 16:35 UTC)

<p>You can right-click the segmentation in the Data module and choose Export visible segments to model node.</p>

---

## Post #3 by @joanne40226 (2022-08-15 00:09 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Thank you so much it worked!<br>
However can i change the exact vertex size of the surface mesh manually? thank you for your time!</p>

---

## Post #4 by @muratmaga (2022-08-15 04:04 UTC)

<p>Can you describe what you mean by “change the exact vertex size”? Distribution of vertices are not uniform, they tend to be smaller triangles (hence more dense) in regions of high curvature and larger ones in more smooth regions.</p>
<p>You can decimate (reduce the polygon count) the model using the surface toolbox.</p>

---

## Post #5 by @joanne40226 (2022-08-15 04:48 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="24751">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Distribution of vertices are not uniform, they tend to be smaller triangles (hence more dense) in regions of high curvature and larger ones in more smooth regions.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> thank you for the quick reply!<br>
so, can i set the polygon count manully? since i have plenty of data sets and i need them to have the same amount of polygon count, so i’m wondering if i can decide the polygon amount of a surface mesh. Thank you!</p>

---

## Post #6 by @joanne40226 (2022-08-15 05:44 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a><br>
hi, sorry for the unclearified problem.<br>
my problem is now that i had segment a skin surface as shown below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6704e551a36930497a2adcb5bc73ba4e206a1e5b.jpeg" data-download-href="/uploads/short-url/eHlFs8tXEL7IhVBEcpzNsrQzJur.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/6704e551a36930497a2adcb5bc73ba4e206a1e5b_2_592x500.jpeg" alt="image" data-base62-sha1="eHlFs8tXEL7IhVBEcpzNsrQzJur" width="592" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/6704e551a36930497a2adcb5bc73ba4e206a1e5b_2_592x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6704e551a36930497a2adcb5bc73ba4e206a1e5b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6704e551a36930497a2adcb5bc73ba4e206a1e5b.jpeg 2x" data-dominant-color="ABAD90"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">774×653 50.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
now i want to generate mesh of the surface model.<br>
However, when i use the SegmentMesher, it did not done it well as shown below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddf84fd93e75e14033f1f83d187a40878d74ebc2.png" data-download-href="/uploads/short-url/vFDwEWoKgFwpVxYTi3gDy69f5m2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddf84fd93e75e14033f1f83d187a40878d74ebc2.png" alt="image" data-base62-sha1="vFDwEWoKgFwpVxYTi3gDy69f5m2" width="604" height="500" data-dominant-color="9699C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">631×522 15.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So i’m wondering if there is a way i can generate mesh on the surface with desired polygon count since the vertices meant to me. Thank you for your time!</p>

---

## Post #7 by @muratmaga (2022-08-15 22:06 UTC)

<aside class="quote no-group" data-username="joanne40226" data-post="6" data-topic="24751">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/joanne40226/48/14681_2.png" class="avatar"> joanne40226:</div>
<blockquote>
<p>my problem is now that i had segment a skin surface as shown below</p>
</blockquote>
</aside>
<p>If you have segmentation like the one you show, all you need to do is to go to the export/import section of the Segmentation module and export it as a model. You can also do that from the data module by right clicking on the segmentation object and then click export as a model. That way you don’t need to use the SegmentMesher, which I believe creates volumetric meshes.</p>

---

## Post #8 by @joanne40226 (2022-08-17 05:19 UTC)

<p>Thank you for the reply! I think i misunderstood the concept of mesh, but i get it clear now! Thank you so much.</p>

---
