---
topic_id: 16459
title: "Calculating Second Moment Of Area From Segment"
date: 2021-03-09
url: https://discourse.slicer.org/t/16459
---

# Calculating Second Moment of Area from Segment

**Topic ID**: 16459
**Date**: 2021-03-09
**URL**: https://discourse.slicer.org/t/calculating-second-moment-of-area-from-segment/16459

---

## Post #1 by @jmhuie (2021-03-09 21:33 UTC)

<p>In the SlicerMorph workshop yesterday, <a class="mention" href="/u/muratmaga">@muratmaga</a> and I briefly talked about the steps needed to measure second moment of area from a long bone image stack/volume. Currently I do this using ImageJ with BoneJ, but it’d be nice to do that in 3D Slicer. My current workflow involves segmenting the bone in 3D Slicer, but I end up having to transform and re-slice the bone volumes so that they are aligned with major axes. Then I save the resampled volume move on to BoneJ. This is a bit of a lengthy process and not totally ideal because it leads to a slight reduction in quality when re-slicing the image stacks.</p>
<p>I have been told the segment statistic module can measure second moment of area, but I’m not seeing this option. Am I missing something?</p>
<p>Also as a humble feature request, it would be nice to have the ability to measurement second moment area along the length of a segment similar to how the “Segment cross-section area” module calculates cross sectional area for each slice.</p>

---

## Post #2 by @davidboerma (2021-03-10 00:57 UTC)

<p>Just chiming in to second Jonathan’s request, and to suggest going further to implement other BoneJ functionalities in Slicer. In particular the “Moments of Inertia” plugin and the “Slice Geometry” plugin. Slice Geometry uses the major-axis-aligned bone slices, and the user selects a slice (often midshaft for long bones) for cross-sectional measurements such as cross-sectional area, polar section modulus, min/max feret diameter, etc.</p>
<p>I currently use slicer to segment the bones and mask the bone segment, leaving black pixels outside the bone. I then export each bone as its own .nrrd for cross-sectional analysis in BoneJ. Being able to perform these calculations directly in Slicer for multiple bones in a specimen and export the measurements as a CSV would have an enormous positive impact on my and others’ workflows.</p>
<p>I’d be eager to help if I can!</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://imagej.net/BoneJ.html/skins/ij2.ico" class="site-icon" width="16" height="16">
      <a href="https://imagej.net/BoneJ.html#Moments_of_inertia" target="_blank" rel="noopener nofollow ugc">ImageJ</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://imagej.net/BoneJ.html#Moments_of_inertia" target="_blank" rel="noopener nofollow ugc">BoneJ</a></h3>

<p>BoneJ is a collection of skeletal biology plug-ins for ImageJ.
This is the new, modernized version of the software available through the ImageJ updater. Its update site is called BoneJ. For the old ImageJ1 version, see BoneJ1.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://imagej.net/BoneJ.html/skins/ij2.ico" class="site-icon" width="16" height="16">
      <a href="https://imagej.net/BoneJ.html#Slice_geometry" target="_blank" rel="noopener nofollow ugc">ImageJ</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://imagej.net/BoneJ.html#Slice_geometry" target="_blank" rel="noopener nofollow ugc">BoneJ</a></h3>

<p>BoneJ is a collection of skeletal biology plug-ins for ImageJ.
This is the new, modernized version of the software available through the ImageJ updater. Its update site is called BoneJ. For the old ImageJ1 version, see BoneJ1.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2021-03-10 01:45 UTC)

<p>Segment statistics module can compute principal axes and moments (eigenvectors and eigenvalues of the inertia matrix) using eigensystem decomposition. You need to enable it in the labelmap statistics option:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b62f1c74d241949a2578f7dab59664258b99ff7.png" data-download-href="/uploads/short-url/jT4m43jg04jQM8pnKK5JRgTFhUX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b62f1c74d241949a2578f7dab59664258b99ff7_2_666x500.png" alt="image" data-base62-sha1="jT4m43jg04jQM8pnKK5JRgTFhUX" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b62f1c74d241949a2578f7dab59664258b99ff7_2_666x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b62f1c74d241949a2578f7dab59664258b99ff7_2_999x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b62f1c74d241949a2578f7dab59664258b99ff7_2_1332x1000.png 2x" data-dominant-color="E9E9E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1559×1170 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>These metrics are “labelmap statistics”, i.e., it only takes into account the segmentation and does not use voxel values of the selected “Scalar volume”. We could make available central moments, principal moments and principal axes “scalar volume statistics” (that takes density values from the selected scalar volume node), because the implementation is readily available in <a href="https://itk.org/Doxygen/html/classitk_1_1ImageMomentsCalculator.html">ITK</a>.</p>
<aside class="quote no-group" data-username="jmhuie" data-post="1" data-topic="16459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jmhuie/48/7086_2.png" class="avatar"> jmhuie:</div>
<blockquote>
<p>Also as a humble feature request, it would be nice to have the ability to measurement second moment area along the length of a segment similar to how the “Segment cross-section area” module calculates cross sectional area for each slice.</p>
</blockquote>
</aside>
<p>For this, probably the best is to resample the volume along the chosen axis. You could redistribute effect of each voxel to discrete axial positions one by one, but it would probably not be any more accurate but several magnitudes slower than resampling the entire volume first and then process it slice by slice.</p>
<aside class="quote no-group" data-username="jmhuie" data-post="1" data-topic="16459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jmhuie/48/7086_2.png" class="avatar"> jmhuie:</div>
<blockquote>
<p>Also as a humble feature request, it would be nice to have the ability to measurement second moment area along the length of a segment similar to how the “Segment cross-section area” module calculates cross sectional area for each slice.</p>
</blockquote>
</aside>
<p>Segment cross-section area module is a Python scripted module, so you should be able to modify it to add some more computations. You could also add computation of all the other features to this module, so that you would have everything available in a single module, computing all metrics by a single click (you would then of course rename it accordingly).</p>
<aside class="quote no-group" data-username="davidboerma" data-post="2" data-topic="16459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davidboerma/48/10247_2.png" class="avatar"> davidboerma:</div>
<blockquote>
<p>I’d be eager to help if I can!</p>
</blockquote>
</aside>
<p>Everything that you described very doable. Probably no algorithm development is needed, and you could just start by cloning and modifying “Segment cross-section area” module. It already has plotting and slicing, so you would just need to add more slice-based metric computation, call segment statistics, etc.</p>
<p>Slicer core developers could help with making ITK’s ImageMomentsCalculator conveniently available from Python, but this may not be necessary if you find a good-quality Python package that can compute all the metrics that you need.</p>

---

## Post #4 by @jmhuie (2021-03-12 01:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="16459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Segment cross-section area module is a Python scripted module, so you should be able to modify it to add some more computations. You could also add computation of all the other features to this module, so that you would have everything available in a single module, computing all metrics by a single click (you would then of course rename it accordingly).</p>
</blockquote>
</aside>
<p>Thanks for the support <a class="mention" href="/u/lassoan">@lassoan</a>. I decided to take a stab at adding to the segment cross-sectional area module and I’m glad I did. I’ve been able to implement many of calculations that BoneJ does. It’s not pretty and there’s still a lot I want to fix in terms of the output as well as the UI of the module, but so far so good. Will hopefully get to a point where I can share it soon.</p>

---

## Post #5 by @jmhuie (2021-11-01 19:36 UTC)

<p>For posterity and any future inquires, my extension called <a href="https://github.com/jmhuie/Slicer-SegmentGeometry" rel="noopener nofollow ugc">SegmentGeometry</a> is live on the Extensions Manager for both 4.11 and the preview release. It iterates slice-by-slice through a segment to calculate the second moment of area and other cross-sectional properties. Reach out if you have any questions or run into any issues.</p>

---
