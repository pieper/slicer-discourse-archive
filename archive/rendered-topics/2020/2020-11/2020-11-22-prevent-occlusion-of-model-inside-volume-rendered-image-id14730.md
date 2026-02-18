# Prevent occlusion of model inside volume rendered image

**Topic ID**: 14730
**Date**: 2020-11-22
**URL**: https://discourse.slicer.org/t/prevent-occlusion-of-model-inside-volume-rendered-image/14730

---

## Post #1 by @slicer365 (2020-11-22 18:21 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43e2c105b844b9725b4bc6d011abf9e91034b664.jpeg" alt="捕获" data-base62-sha1="9GxO8GohfkjtjdNI6s93ttgD0ag" width="321" height="237"><br>
How to not mediate the transparency of the head, so that the model is fully displayed.<br>
i mean let the model be displayed on the top layer.No matter what angle</p>

---

## Post #2 by @lassoan (2020-11-22 20:46 UTC)

<p>Slicer offers many options to address this need. We can give you more specific advice if you tell us more about your application (is it for planning or guidance? what are the structures of interest? what would you like to assess on the visualization?).</p>
<p>Anyway, a few hints:</p>
<ul>
<li>You can make parts of the volume-rendered image semi-transparent by adjusting Scalar Opacity Mapping in Volume rendering module</li>
<li>You can crop the volume using rectangular ROI (you can rotate it by applying a transform)</li>
<li>You can crop the volume using a conic or spherical ROI using SlicerPRISM extension</li>
</ul>
<div class="youtube-onebox lazy-video-container" data-video-id="-LODgIh5W6k" data-video-title="SlicerPRISM DTI 2018 07 12" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=-LODgIh5W6k" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/-LODgIh5W6k/maxresdefault.jpg" title="SlicerPRISM DTI 2018 07 12" width="" height="">
  </a>
</div>

<ul>
<li>You can segment structures that you want to visualize using Segment editor and display them as solid objects, while displaying other structures as semi-transparent using volume rendering</li>
<li>You can explore a 3D volume along a chosen trajectory in slice views, using modules such as Path Explorer module in SlicerIGT extension.</li>
<li>With a bit of software development skills, you can create custom volume rendering shaders that emphasize structures that you are interested in while suppresses irrelevant ones (SlicerPRISM make it easy to define and adjust parameters of custom shaders).</li>
</ul>

---

## Post #3 by @slicer365 (2020-11-23 00:23 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9b952b1ddfff0bec582f5d9c404e26f3b160ff2.jpeg" data-download-href="/uploads/short-url/odrKcM6gVYD18m4hXsZzfSIZqls.jpeg?dl=1" title="82ea90bee0352649e1a9beadc2d9676" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9b952b1ddfff0bec582f5d9c404e26f3b160ff2_2_666x500.jpeg" alt="82ea90bee0352649e1a9beadc2d9676" data-base62-sha1="odrKcM6gVYD18m4hXsZzfSIZqls" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9b952b1ddfff0bec582f5d9c404e26f3b160ff2_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9b952b1ddfff0bec582f5d9c404e26f3b160ff2_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9b952b1ddfff0bec582f5d9c404e26f3b160ff2_2_1332x1000.jpeg 2x" data-dominant-color="53515D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">82ea90bee0352649e1a9beadc2d9676</span><span class="informations">1440×1080 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Hello, Professor, I want to get the body surface projection of the tumor or hematoma, but without changing the transparency of the head, just like this picture.</p>

---

## Post #4 by @lassoan (2020-12-14 04:38 UTC)

<p>You can get such visualization by segmenting the brain surface (for example, fully automatically, using SwissSkullStripper extension) and make that surface semi-transparent. You can also segment the skin surface easily using thresholding and smoothing, maybe with solidification (SurfaceWrapSolidify extension’s Wrap Solidify effect).</p>
<p>What is the clinical goal? Are you trying to create visualization mode that helps finding optimal burr hole placement?</p>

---
