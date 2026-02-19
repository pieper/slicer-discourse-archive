---
topic_id: 23107
title: "Color And Opacity Rendered Volumes"
date: 2022-04-24
url: https://discourse.slicer.org/t/23107
---

# Color and opacity rendered volumes

**Topic ID**: 23107
**Date**: 2022-04-24
**URL**: https://discourse.slicer.org/t/color-and-opacity-rendered-volumes/23107

---

## Post #1 by @aritche (2022-04-24 14:41 UTC)

<p>Hi,</p>
<p>I am trying to render a 3D MRI scan and 3D segmentation of the Fornix. These are both stored as nifti files, so I am able to open them and use the ‘Volume Rendering’ module to display them in the 3D view.</p>
<p>I want to achieve the following, but I have absolutely no idea how to do it so I would greatly appreciate any advice:</p>
<ol>
<li>Reduce the opacity of the rendered MRI scan volume. The purpose of showing this volume is just to give the audience a subtle clue as to the orientation and position of the brain; i want it to be much less visible than it currently is by default.</li>
<li>Change the colour of the Fornix segmentation volume. All the voxels have the value ‘1’ in the nifti file, so by default this is just rendered as a white volume. I want it to be some other colour like green or red so it stands out more (at the moment it blends in too much with the actual MRI scan).</li>
</ol>
<p>Thank you so much for your help, I have been stuck on this for a little bit now.</p>

---

## Post #2 by @lassoan (2022-04-24 15:35 UTC)

<p>To provide a broad external anatomical context, we often segment the skin and the brain surface and display them as semi-transparent surfaces. They are both easy to segment:</p>
<ul>
<li>skin can be segmented by simple thresholding, followed by smoothing and wrapping as described in this <a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface2/">segmentation recipe</a></li>
<li>segmentation of the brain surface (skull stripping) is provided by many modules, for example I would recommend the simple <a href="https://github.com/lassoan/SlicerSwissSkullStripper#swissskullstripper">SwissSkullStripper extension</a> or the higher-quality, more robust, but more computationally demanding <a href="https://github.com/lassoan/SlicerHDBrainExtraction">HDBrainExtraction extension</a></li>
</ul>
<aside class="quote no-group" data-username="aritche" data-post="1" data-topic="23107">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/aeb1de/48.png" class="avatar"> aritche:</div>
<blockquote>
<p>All the voxels have the value ‘1’ in the nifti file, so by default this is just rendered as a white volume.</p>
</blockquote>
</aside>
<p>When you load the nifti file, make sure you choose <code>Segmentation</code> in the <code>Description</code> column in the <code>Add data</code> window. You can then easily adjust color, opacity, etc. in both slice and 3D views, using Segmentations module.</p>

---

## Post #3 by @aritche (2022-04-25 05:35 UTC)

<p>Thank you, this is very informative.</p>
<p>I tried to load the nifti file as a Segmentation instead of a Volume, and now when I apply a linear transformation to Posterior/Anterior flip it, it renders as black for some reason.</p>
<p>Before flipping:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86cd0d91d49a148bdf1ad9f09e1dff544ae47dec.png" data-download-href="/uploads/short-url/jeviUJbFsT3iOGlIEyRx9cfhKY4.png?dl=1" title="before" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86cd0d91d49a148bdf1ad9f09e1dff544ae47dec_2_300x250.png" alt="before" data-base62-sha1="jeviUJbFsT3iOGlIEyRx9cfhKY4" width="300" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86cd0d91d49a148bdf1ad9f09e1dff544ae47dec_2_300x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86cd0d91d49a148bdf1ad9f09e1dff544ae47dec_2_450x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86cd0d91d49a148bdf1ad9f09e1dff544ae47dec_2_600x500.png 2x" data-dominant-color="9B9CD3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">before</span><span class="informations">960×798 17.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After flipping:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0f627d75377b023c76fdea6cd4f09524f79bce5.png" data-download-href="/uploads/short-url/w66l2ALjS48cMNwJnRiHsHdR5v7.png?dl=1" title="after" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0f627d75377b023c76fdea6cd4f09524f79bce5_2_320x250.png" alt="after" data-base62-sha1="w66l2ALjS48cMNwJnRiHsHdR5v7" width="320" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0f627d75377b023c76fdea6cd4f09524f79bce5_2_320x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0f627d75377b023c76fdea6cd4f09524f79bce5_2_480x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0f627d75377b023c76fdea6cd4f09524f79bce5_2_640x500.png 2x" data-dominant-color="9C9DD3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">after</span><span class="informations">992×775 12.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is the linear transform matrix I am applying:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81570dc1572294cf1af5592de00f8158d2cabb57.png" data-download-href="/uploads/short-url/isc6xl1XJblC3CpN6m2vfgA8mYT.png?dl=1" title="transform" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81570dc1572294cf1af5592de00f8158d2cabb57_2_345x90.png" alt="transform" data-base62-sha1="isc6xl1XJblC3CpN6m2vfgA8mYT" width="345" height="90" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81570dc1572294cf1af5592de00f8158d2cabb57_2_345x90.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81570dc1572294cf1af5592de00f8158d2cabb57_2_517x135.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81570dc1572294cf1af5592de00f8158d2cabb57_2_690x180.png 2x" data-dominant-color="2D2D2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">transform</span><span class="informations">1046×274 7.06 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-04-25 11:45 UTC)

<p>Determinant of this transformation matrix is -1, which means that it turns the object inside out. That’s why it appears black. Do you actually need to apply such transform, or just played around with the values?</p>

---
