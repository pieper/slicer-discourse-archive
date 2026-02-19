---
topic_id: 1026
title: "I Want To Load A Volume Rendered Image Data From In Matlab"
date: 2017-09-09
url: https://discourse.slicer.org/t/1026
---

# I want to load a volume rendered image data from in matlab

**Topic ID**: 1026
**Date**: 2017-09-09
**URL**: https://discourse.slicer.org/t/i-want-to-load-a-volume-rendered-image-data-from-in-matlab/1026

---

## Post #1 by @airtech2 (2017-09-09 11:59 UTC)

<p>Operating system: window 10<br>
Slicer version: 4.7.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello,</p>
<p>I rendered 3D aorta model in 3D slicer . I want to load this 3D model in matlab.</p>
<p>Is there any way to load this data?</p>
<p>I want to analyze fluid dynamic simulation study using FEATool extension in matlab.</p>
<p>Thanks for reading.</p>

---

## Post #2 by @lassoan (2017-09-09 12:08 UTC)

<p>Volume rendering is a visualization technique. Output of volume rendering is a 2D color image. No data is generated that could be used for FEA. See detailed explanation in this topic:</p>
<aside class="quote quote-modified" data-post="1" data-topic="524">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b19c9b/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524">Save volume rendering as STL file</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, I am a new user on 3D slicer. 
I was using the display preset feature under volume rendering, and I was wondering if there is a way to save what I was viewing as an .stl or 3D printable file. 
For example, I was viewing a sample MRI using the CT-cardiac3 preset display. 
When I tried to save that specific 3D preset displayed sample in a .stl file, the option was unavailable. 
I was only able to see .vp (volume property), .txt formats. 
Is there a way to accomplish what I desire in 3D slic…
  </blockquote>
</aside>

<p>For FEA, you need volumetric mesh or at least a surface mesh - represented as Model node in Slicer. You can create model from a volume by segment the volume using Segment Editor then export the Segmentation node to Model node.</p>

---

## Post #3 by @deepmech (2017-09-11 16:32 UTC)

<p>download cleaver extensions that advertise the capability of generating a volume mesh, but I don’t know whether they are functional and/or maintained.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/CleaverExtension" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/CleaverExtension</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/718084bdf1c3d96b3e99e5bf66235d502f943472.jpeg" data-download-href="/uploads/short-url/gc5iPUuJ3nv3FbuumbbwReEgtXQ.jpg?dl=1" title="imp" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/718084bdf1c3d96b3e99e5bf66235d502f943472_2_690x387.jpg" alt="imp" data-base62-sha1="gc5iPUuJ3nv3FbuumbbwReEgtXQ" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/718084bdf1c3d96b3e99e5bf66235d502f943472_2_690x387.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/718084bdf1c3d96b3e99e5bf66235d502f943472_2_1035x580.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/718084bdf1c3d96b3e99e5bf66235d502f943472.jpeg 2x" data-dominant-color="BCBAC3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imp</span><span class="informations">1366×768 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>there is a option for export in matlab</p>

---

## Post #4 by @lassoan (2017-09-11 17:30 UTC)

<p><a class="mention" href="/u/michael_hardisty">@Michael_Hardisty</a> Could you comment on this? Were you able to use Cleaver extension after all? Have you checked how difficult would it be to upgrade Slicer’s extension to Cleaver2?</p>

---
