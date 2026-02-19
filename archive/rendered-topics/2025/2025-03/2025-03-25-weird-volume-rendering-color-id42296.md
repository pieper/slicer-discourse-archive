---
topic_id: 42296
title: "Weird Volume Rendering Color"
date: 2025-03-25
url: https://discourse.slicer.org/t/42296
---

# Weird volume rendering color

**Topic ID**: 42296
**Date**: 2025-03-25
**URL**: https://discourse.slicer.org/t/weird-volume-rendering-color/42296

---

## Post #1 by @Arber_Demi (2025-03-25 13:04 UTC)

<p>Hello everyone,</p>
<p>I’m working on creating some form of “heatmap” on an existing volume. At the moment, I create 3D gaussian kernels of some value range (that I can target easily with the scalar color mapping) at specific coordinates I have beforehand. I do this by taking that part of the volume through numpy, setting the values to my kernel (where my kernel is not 0) and then do <code>slicer.util.updateVolumeFromArray(nodeVolume, volumeNumpyArray)</code> to update my volume node.</p>
<p>The replacement works just fine, however the visual results are not really what I expect.</p>
<p>Below you can see a heatmap of the 3D kernels that I use, which look as I expect. (I am using the “hot” color mapping from matplotlib here)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0b20ea9697d55e7cfd9956c166c9eaf4bcb8256.jpeg" data-download-href="/uploads/short-url/mVzSDp7AFpqfyrFO5v7huwXZ85U.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0b20ea9697d55e7cfd9956c166c9eaf4bcb8256_2_505x500.jpeg" alt="image" data-base62-sha1="mVzSDp7AFpqfyrFO5v7huwXZ85U" width="505" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0b20ea9697d55e7cfd9956c166c9eaf4bcb8256_2_505x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0b20ea9697d55e7cfd9956c166c9eaf4bcb8256.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0b20ea9697d55e7cfd9956c166c9eaf4bcb8256.jpeg 2x" data-dominant-color="EFE5E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">690×682 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, in Slicer (with different color mapping), I get these results:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/dee04f3eaf739c8de9d81acd9bb133bd6dd4e8ed.jpeg" data-download-href="/uploads/short-url/vNEzVlvFLsJErDxdGUS1hYvktVr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee04f3eaf739c8de9d81acd9bb133bd6dd4e8ed_2_501x500.jpeg" alt="image" data-base62-sha1="vNEzVlvFLsJErDxdGUS1hYvktVr" width="501" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee04f3eaf739c8de9d81acd9bb133bd6dd4e8ed_2_501x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/dee04f3eaf739c8de9d81acd9bb133bd6dd4e8ed.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/dee04f3eaf739c8de9d81acd9bb133bd6dd4e8ed.jpeg 2x" data-dominant-color="87650D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">523×521 94.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
with a color mapping that looks like this (the entire color map has opacity set to 1):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d276cc3585ac29ebb9a09d8434308cfa81a6dde1.png" alt="image" data-base62-sha1="u1QN5ci73gHZUkUzbQmsSKD5FC1" width="263" height="72"><br>
The inside of the spheres themselves is properly colored (when I zoom in I can see the proper distribution on the inside of the spheres), however I expect the outside here to be fully green.</p>
<p><strong>(This matters as in the end I don’t want actual spheres, they are there to just generate a distribution for the color values. My actual goal it to get some form of heatmap overlay over an existing surface, while still trying to keep most of the physical detail from that surface)</strong></p>
<p>(When changing the Interpolation to nearest neighbours I get more or less what I want, however the quality is quite bad).</p>
<p>Is there anyway to make this behave normally?<br>
Is this already normal behaviour and am I missunderstanding what to expect from volume rendering?<br>
Is there anyway to get better interpolation (without implementing it myself)?<br>
Should I take another approach to get my desired heatmap result?<br>
Any insight would be appreciated. Thank you :]</p>

---

## Post #2 by @Arber_Demi (2025-03-25 13:27 UTC)

<p>As an addition, this seems to happen when any very distinctive color is part of the color mapping, as with the full volume, even on the outer surface I get something like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20c543973b01012d1ed335d7f7fa0d2901ba0725.jpeg" data-download-href="/uploads/short-url/4FTUKleXRCya0yYrtqskcvPg90N.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20c543973b01012d1ed335d7f7fa0d2901ba0725.jpeg" alt="image" data-base62-sha1="4FTUKleXRCya0yYrtqskcvPg90N" width="614" height="448"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">614×448 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2025-03-25 14:40 UTC)

<p>This behavior is expected whenever neighbor voxels have vastly different color and opacity is close to 100%. This is because there is no longer an option in VTK volume renderer to choose between “interpolate first” and “classify first” during ray traversal. It is always “interpolate first” (compute interpolated voxel value and then look up the corresponding color and opacity in the transfer functions).</p>
<p>This means that if you have voxel value of 0 = green, next to voxel value of 1000 = red then you will have sample values like 0, 0, 0, 312, 544, 753, 1000, 1000, 1000 etc. along the ray. Since the opacity of 1000 corresponds to 100%, the first few samples will determine the color, so the result will be greenish-red.</p>
<p>If you want to use 100% opacity = isosurface rendering then one solution is to run a contour filter and render as surface. You can enabl “Surface smoothing” in volume rendering options to randomiz the ray sampling point positions to woodgrain pattern and have a more random distribution. There are many other solutions. If you tell a bit more about your use case then we can give more specific advice.</p>

---

## Post #4 by @Arber_Demi (2025-03-25 14:44 UTC)

<p>My end goal is to try and generate a heatmap based on specific coordinates on a brain segmentation. Something that defines a gradient color from the center coordinate and dissipates toward the edges, preferrably in a different color.</p>
<p>I already took a look at previous posts suggesting the use of segmentations, however that doesn’t offer the preservation of detail that I want here (trying to still have the brain ridges be recognisable through the heatmap).</p>
<p>The best case scenario would be some functionality that allows me to change the colors going into the ray equation (to give the existing color just a tint of the calculated values from my heatmap), but I think that’s likely not possible.</p>
<p>To give a more specific example, I am trying to achieve a more advanced version of this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a5211c30242450d833a0bea29249d390acd80ad.jpeg" data-download-href="/uploads/short-url/1tiBFoMLK6ZDpvMPdkUpyNwrF49.jpeg?dl=1" title="3D_heat_map_epilepsy" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a5211c30242450d833a0bea29249d390acd80ad_2_690x460.jpeg" alt="3D_heat_map_epilepsy" data-base62-sha1="1tiBFoMLK6ZDpvMPdkUpyNwrF49" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a5211c30242450d833a0bea29249d390acd80ad_2_690x460.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a5211c30242450d833a0bea29249d390acd80ad_2_1035x690.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a5211c30242450d833a0bea29249d390acd80ad_2_1380x920.jpeg 2x" data-dominant-color="E0E7E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D_heat_map_epilepsy</span><span class="informations">2880×1920 390 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am trying to have some form of transparency and not fully opaque end surface, however if only the surface shows then that’s also acceptable.</p>

---

## Post #5 by @pieper (2025-03-25 14:51 UTC)

<p>Everything in volume rendering comes down to sampling, so you’ll need to provide a continuous smooth signal if you want a nice result.</p>
<p>Why don’t you post a short script of what you are doing that people can try on their own machines and make suggestions.</p>

---

## Post #6 by @lassoan (2025-03-25 14:54 UTC)

<p>You can render as a colored surface: export the segmentation to a model and assign colors to model points from the heatmap volume using “Probe volume with model” module.</p>
<p>If you don’t have a good-quality surface (so you would rather display it using volume rendering) then you can follow the method that is used in “Colorize volume” module: keep using your scalar volume as alpha channel and use your heatmap as color channels. Then display this RGBA volume using volume rendering.</p>

---

## Post #7 by @Arber_Demi (2025-03-25 15:00 UTC)

<p>That is indeed part of my problem here, the surfaces that I am working with could definitely be a lot better. I don’t mind the cubic results I get for my spheres, as I expect them to look like that on their own. However at the end I plan to crop out the excess that is not inside my main volume.</p>
<p>I will clean up my scripts and send them here once ready.</p>

---

## Post #8 by @pieper (2025-03-25 15:01 UTC)

<p>Definitely try the RGBA rendering option too.</p>

---

## Post #9 by @Arber_Demi (2025-03-25 15:01 UTC)

<p>I didn’t know about the SandBox extension yet, and the description of the Colorize volume model sounds great. In my head that’s what I was trying to achieve, set the volume as alpha and then use the heatmap for color channels, but I will check how successful I am with this module and get back to you. Thank you very much for the suggestion.</p>

---

## Post #10 by @Arber_Demi (2025-03-25 15:17 UTC)

<p>This is currently what I am running in slicerrc for quick iteration.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://drive.google.com/drive/folders/1BfOTYf9K9HUQezGOMoxq6ELp_nXllnob?usp=drive_link">
  <header class="source">
      <img src="https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png" class="site-icon" width="32" height="32">

      <a href="https://drive.google.com/drive/folders/1BfOTYf9K9HUQezGOMoxq6ELp_nXllnob?usp=drive_link" target="_blank" rel="noopener nofollow ugc">Google Drive</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://drive.google.com/drive/folders/1BfOTYf9K9HUQezGOMoxq6ELp_nXllnob?usp=drive_link" target="_blank" rel="noopener nofollow ugc">testfile - Google Drive</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It doesn’t have the masking part that I plan to add for the final version of what I am doing, however it is enough to see the rendering issues.</p>
<p>For the main volume mention in the script, it’s fine to use the sample MRHead MRI and use that as main volume. The points in the markup file should be points that are somewhere around the brains surface (around the skin is also fine to see the same issues).</p>
<p>At the moment I also edited the scalar color map once manually, saved it, and then loaded through the script every other time (however will have it come from an outside color map in the future)</p>

---

## Post #11 by @pieper (2025-03-29 17:15 UTC)

<p>To make it easier to test and discuss this code, please make it fully self contained, in the sense that it downloads sample data and hard-codes any markups or other data so it can easily be copy-pasted to reproduce.</p>
<p>Also please put it in a github repo or gist so iterations and comments can be tracked.</p>

---
