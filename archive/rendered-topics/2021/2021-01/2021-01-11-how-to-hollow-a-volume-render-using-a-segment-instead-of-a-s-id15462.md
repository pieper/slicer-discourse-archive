---
topic_id: 15462
title: "How To Hollow A Volume Render Using A Segment Instead Of A S"
date: 2021-01-11
url: https://discourse.slicer.org/t/15462
---

# How to hollow a Volume Render using a Segment instead of a Surface Cut?

**Topic ID**: 15462
**Date**: 2021-01-11
**URL**: https://discourse.slicer.org/t/how-to-hollow-a-volume-render-using-a-segment-instead-of-a-surface-cut/15462

---

## Post #1 by @Biomodelos_3D (2021-01-11 20:33 UTC)

<p>Operating system:W10<br>
Slicer version: 4.11.20<br>
Expected behavior: Hollow a Volume Render using a Segment<br>
Actual behavior: ?</p>
<p>Can a Volume Render be Masked by a 3D Segment instead of a Surface Cut?<br>
I assume it can be done, but can’t figure it how. In the attached image, I want to hollow the Volume Render with the blue Segment.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d76c9d6e3da1e4498a404fc9951760ed2e7c271.jpeg" data-download-href="/uploads/short-url/8LJCYTNjhgp1vTeSV2jRs9KWsPT.jpeg?dl=1" title="Restar Segmento de Render Volumetrico" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d76c9d6e3da1e4498a404fc9951760ed2e7c271_2_690x251.jpeg" alt="Restar Segmento de Render Volumetrico" data-base62-sha1="8LJCYTNjhgp1vTeSV2jRs9KWsPT" width="690" height="251" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d76c9d6e3da1e4498a404fc9951760ed2e7c271_2_690x251.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d76c9d6e3da1e4498a404fc9951760ed2e7c271_2_1035x376.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d76c9d6e3da1e4498a404fc9951760ed2e7c271.jpeg 2x" data-dominant-color="817CAF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Restar Segmento de Render Volumetrico</span><span class="informations">1041×380 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2021-01-11 20:37 UTC)

<p>Install the SegmentEditorExtraEffects and use either the MaskVolume (applies only the selected segment) or SplitVolume (creates new volumes for all segments in the segmentation) tools to create new volumes that contain only the region you are interested.</p>
<p>You can use the Volume Rendering on the newly derived volume.</p>

---

## Post #3 by @Biomodelos_3D (2021-01-12 02:27 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a>! that really helped!<br>
This <strong><a href="https://youtu.be/oxR5Tt4f4nE" rel="noopener nofollow ugc">link</a></strong> is a short video of what I’ve got. Pretty much what I was looking for, but cavity interiors are stepped. Any solution to that?</p>

---

## Post #4 by @lassoan (2021-01-12 04:21 UTC)

<aside class="quote no-group" data-username="Biomodelos_3D" data-post="3" data-topic="15462">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/biomodelos_3d/48/9452_2.png" class="avatar"> Biomodelos_3D:</div>
<blockquote>
<p>cavity interiors are stepped</p>
</blockquote>
</aside>
<p>I guess you try to remove the contrast agent from the vessels to make them transparent, so that you get an endovascular view.</p>
<p>The bad news that you cannot easily achieve this with masking, because you will have very high intensity voxels (remnants of the contrast agent or the walls/vessels) right next to very low intensity (blanked out voxels), which will be rendered with staircase artifacts. With some effort you could soften it (create a black-and-white volume, then soften the edges with Gaussian smoothing, then subtract it from the original volume), but you may end up with blurred walls.</p>
<p>The good news that you don’t need to rely on segmentation to render cardiac CT images in endocardial view. You just need to edit the volume rendering transfer functions to make contrast agent transparent.</p>
<p>Default CT Cardiac volume rendering preset:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09a267c089f9d194d6706577febcc4a35a144bfc.jpeg" data-download-href="/uploads/short-url/1nefqWCSNkRszHdSKfcZzkfeMJm.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09a267c089f9d194d6706577febcc4a35a144bfc_2_690x419.jpeg" alt="image" data-base62-sha1="1nefqWCSNkRszHdSKfcZzkfeMJm" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09a267c089f9d194d6706577febcc4a35a144bfc_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09a267c089f9d194d6706577febcc4a35a144bfc_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09a267c089f9d194d6706577febcc4a35a144bfc_2_1380x838.jpeg 2x" data-dominant-color="4A3F3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1371 495 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>With contrast agent (approximately 300-700HU) made transparent:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d55bdc59c27bb0cef2d76691fa96aae55ebc0c2a.jpeg" data-download-href="/uploads/short-url/ursvJUqzH8kPup7R2mOn5e5v9YC.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d55bdc59c27bb0cef2d76691fa96aae55ebc0c2a_2_690x419.jpeg" alt="image" data-base62-sha1="ursvJUqzH8kPup7R2mOn5e5v9YC" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d55bdc59c27bb0cef2d76691fa96aae55ebc0c2a_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d55bdc59c27bb0cef2d76691fa96aae55ebc0c2a_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d55bdc59c27bb0cef2d76691fa96aae55ebc0c2a_2_1380x838.jpeg 2x" data-dominant-color="4A4241"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1370 505 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83c274aad6a2323e3989ba2c06b4fdaebce6214a.gif" alt="SlicerCapture" data-base62-sha1="iNBaqdYvnnubPtIAR31DP9ZNmY2" width="342" height="350" class="animated"></p>

---

## Post #5 by @Biomodelos_3D (2021-01-12 22:34 UTC)

<p>Cool! Much more fast and easy! Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, that’s exactly what I was searching for!</p>

---

## Post #6 by @Biomodelos_3D (2021-01-13 15:51 UTC)

<p>About Volume Render, is there a way to save - load what you do with Volume Render Advanced controllers, so you can use your own presets in other studies?</p>

---

## Post #7 by @lassoan (2021-01-13 18:57 UTC)

<p>You can save the volume rendering preset parameters and use it anywhere. Content of volume rendering preset file is described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/volumerendering.html#format-of-volume-property-vp-file">here</a>.</p>
<p>You can also load the saved .vp file into any Slicer scene and choose that in Volume rendering module / Inputs / Property.</p>

---

## Post #8 by @Biomodelos_3D (2021-01-16 17:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="15462">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can also load the saved .vp file into any Slicer scene and choose that in Volume rendering module / Inputs / Property.</p>
</blockquote>
</aside>
<p>Thanks! very useful info!</p>

---
