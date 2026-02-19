---
topic_id: 13412
title: "Crosshair Snap To Voxel Center"
date: 2020-09-09
url: https://discourse.slicer.org/t/13412
---

# Crosshair snap to voxel center

**Topic ID**: 13412
**Date**: 2020-09-09
**URL**: https://discourse.slicer.org/t/crosshair-snap-to-voxel-center/13412

---

## Post #1 by @vanossj (2020-09-09 21:39 UTC)

<p>Is there a way I can configure the crosshair to snap to the grid defined by the voxel centers?</p>
<p>This would solve a problem I’m having where the segmentation looks incorrect because either</p>
<ol>
<li>I segmented centered, but now i’m off centered</li>
<li>My segmentation is inaccurate because I unknowningly segmented a highly interpolated slice.</li>
</ol>
<p>It’s the same problem as <a href="https://discourse.slicer.org/t/duplicated-segmentation-error/5510/2" class="inline-onebox">Duplicated Segmentation Error</a></p>

---

## Post #2 by @lassoan (2020-09-10 02:14 UTC)

<p>How did you end up with a “highly” interpolated slice? A displayed slice is interpolated from exactly two neighbor slices, so interpolation artifact should be negligible.</p>
<p>If your input image spacing is highly anisotropic then it often makes sense to resample it to have isotropic spacing (something between lower intra-slice spacing and larger inter-slice spacing), using Crop volume module, before you start segmenting.</p>

---

## Post #3 by @vanossj (2020-09-10 06:01 UTC)

<p>“Highly” interpolated because my dataset is very ansiotropic, 1x1x5mm.</p>
<p>This segmentation from the center of the slice looks ok<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33a8f7a25e9c0f8218a318c516b0a256697a70ac.png" data-download-href="/uploads/short-url/7n0mqNgSC7a5ea4QYaNZyLpCtnC.png?dl=1" title="center" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33a8f7a25e9c0f8218a318c516b0a256697a70ac_2_574x500.png" alt="center" data-base62-sha1="7n0mqNgSC7a5ea4QYaNZyLpCtnC" width="574" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33a8f7a25e9c0f8218a318c516b0a256697a70ac_2_574x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33a8f7a25e9c0f8218a318c516b0a256697a70ac.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33a8f7a25e9c0f8218a318c516b0a256697a70ac.png 2x" data-dominant-color="3E333A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">center</span><span class="informations">717×624 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But if you move to one end of the voxel, it can look incorrect. If I came across this, I might erronously modify the segmentation to match the interpolated view.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92d232b2eba9bb635be2938185eb05230e452937.png" data-download-href="/uploads/short-url/kWQ3ACJG5rcLUkddS4QxLytKant.png?dl=1" title="high" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92d232b2eba9bb635be2938185eb05230e452937_2_575x500.png" alt="high" data-base62-sha1="kWQ3ACJG5rcLUkddS4QxLytKant" width="575" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92d232b2eba9bb635be2938185eb05230e452937_2_575x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92d232b2eba9bb635be2938185eb05230e452937.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92d232b2eba9bb635be2938185eb05230e452937.png 2x" data-dominant-color="392E35"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">high</span><span class="informations">715×621 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I resample to isotropic spacing, that would reduce this effect. But then there are 5x the slices to look at, 80% of them are artifically generated. I would rather only annotate the slices from the original volume.</p>

---

## Post #4 by @lassoan (2020-09-10 12:31 UTC)

<p>You don’t need to segment more slices if you resampled the volume. To get started, you can just segment every 10th or every 50th slice and interpolate between them using “Fill between slices” effect. If you find that on any of the frames the segmentation is inaccurate then you can segment additional slices and the module will automatically recompute the segmentation. There are also 3D segmentation tools available, such as Grow from seeds, and many more provided by extensions such as Fast marching and Watershed by <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects">SegmentEditorExtraEffects extension</a>, fully automatic AI liver segmentation by <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin">NVidia AIAA extension</a>.</p>
<p>You can learn more about image segmentation <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">here</a> and find step-by-step tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">here</a>.</p>

---
