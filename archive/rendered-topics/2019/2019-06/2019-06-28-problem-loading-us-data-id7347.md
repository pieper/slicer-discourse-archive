# Problem loading US data

**Topic ID**: 7347
**Date**: 2019-06-28
**URL**: https://discourse.slicer.org/t/problem-loading-us-data/7347

---

## Post #1 by @svasude1 (2019-06-28 02:40 UTC)

<p>Operating system: Windows<br>
Slicer version: 2.0<br>
Expected behavior:<br>
Actual behavior:<br>
I was trying to load some US patient data into the slicer. When I load the data, all slices are interpreted as axial, even though there are sagittal slices. Is there a way to fix this?</p>

---

## Post #2 by @lassoan (2019-06-28 22:57 UTC)

<p>You can orient the volume by using Transforms module: create a new linear transform, apply it to the volume, and adjust rotation sliders.</p>

---

## Post #3 by @svasude1 (2019-07-08 17:44 UTC)

<p>What if I have one 2-D cross section each along x-z and y-z planes:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff8df633282498c83c956152405342702c786ef1.png" data-download-href="/uploads/short-url/AsJUcKwO9uMYP2bK3uzY3CXPYVr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff8df633282498c83c956152405342702c786ef1_2_690x462.png" alt="image" data-base62-sha1="AsJUcKwO9uMYP2bK3uzY3CXPYVr" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff8df633282498c83c956152405342702c786ef1_2_690x462.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff8df633282498c83c956152405342702c786ef1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff8df633282498c83c956152405342702c786ef1.png 2x" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1005×674 35 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there some way to approximate a volume for this?</p>

---

## Post #4 by @lassoan (2019-07-09 03:49 UTC)

<p>If you know the position of each slice then create a sequence file and load that using sequences extension (see details <a href="https://discourse.slicer.org/t/importing-of-position-tracked-ultrasound-sequence/4094/9">here</a>).</p>
<p>Once you have the slices in their correct position, you can reconstruct a shape from two slices using “Surface cut” effect in Segment Editor module (install SegmentEditorExtraEffects extension to get this effect).</p>
<div class="lazyYT" data-youtube-id="xZwyW6SaoM4" data-youtube-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque&amp;start=86"></div>
<p>This works amazingly well for generation of breast tumor 3D model from a few position-tracked 2D ultrasound images - see more information <a href="http://www.slicerigt.org/wp/breast-cancer-surgery/" rel="nofollow noopener">here</a>.</p>

---
