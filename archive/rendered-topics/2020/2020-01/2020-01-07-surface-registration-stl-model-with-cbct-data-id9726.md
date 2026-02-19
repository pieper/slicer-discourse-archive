---
topic_id: 9726
title: "Surface Registration Stl Model With Cbct Data"
date: 2020-01-07
url: https://discourse.slicer.org/t/9726
---

# Surface Registration (STL model with cbct data)

**Topic ID**: 9726
**Date**: 2020-01-07
**URL**: https://discourse.slicer.org/t/surface-registration-stl-model-with-cbct-data/9726

---

## Post #1 by @OJay (2020-01-07 14:22 UTC)

<p>where i found a Surface Registration?<br>
I will merge a STL model on a cbct data set…</p>
<p>Thank you in advance,<br>
Ole</p>

---

## Post #2 by @lassoan (2020-01-07 14:35 UTC)

<p>There are many options for surface registration.</p>
<p>Landmark registration is simple, always guaranteed to work, but requires manual definition of anatomical landmarks. I would recommend Fiducial Registration Wizard module (provided by SlicerIGT extension). You can use landmark registration as an approximate initial step for automatic registrations.</p>
<p>For rigid registration, you may choose ICP-based surface registration (SlicerIGT extension, Surface registration module). It is very accurate but requires good initial alignment, otherwise it may get stuck in local optimum.</p>
<p>If surfaces may be deformed then you can use Segment Registration extension to align them with a warping transform. You need to import surface models into segmentation node before using this module.</p>
<p>If by CBCT data you mean CBCT image then you need to segment the image (using Segment Editor module) before you can use the methods described above. If you don’t want to segment your data then you may convert your STL model to image data (using Segmentations module, by importing the model into a segment then creating an image volume using Mask Volume effect - provided by SegmentEditorExtraEffects extension) then use intensity-based automatic registration (using BRAINS module or SlicerElastix extension).</p>

---

## Post #3 by @OJay (2020-01-07 15:33 UTC)

<p>Thank you very much!!!</p>

---

## Post #4 by @OJay (2020-01-08 13:47 UTC)

<p>sorry but nothing works <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=9" title=":confused:" class="emoji" alt=":confused:"> why is it so difficult to make a registration of a Volume and  a STL file?<br>
The IGL - Model Registration function looks easy but is not working <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"></p>

---

## Post #5 by @lassoan (2020-01-08 14:05 UTC)

<aside class="quote no-group" data-username="OJay" data-post="4" data-topic="9726">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/c5a1d2/48.png" class="avatar"> OJay:</div>
<blockquote>
<p>looks easy but is not working</p>
</blockquote>
</aside>
<p>The approaches described above should work. If you need help then describe what you did exactly (list of every mouse click and a few screenshots; alternatively, you can post a screen capture video), what did you expect to happen, and what happened instead.</p>

---

## Post #6 by @OJay (2020-01-08 15:22 UTC)

<p>here is a screen capture from the waste what i do <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1_YNgt22sGD6vIlD_CohDqKCw6HeiSHR5/view?usp=drive_open" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1_YNgt22sGD6vIlD_CohDqKCw6HeiSHR5/view?usp=drive_open" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1_YNgt22sGD6vIlD_CohDqKCw6HeiSHR5/view?usp=drive_open" target="_blank" rel="nofollow noopener">ScreenCapture_08.01.2020 15.49.15.wmv (video)</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>thanks!</p>

---

## Post #7 by @lassoan (2020-01-08 15:51 UTC)

<p>Thank you, the video was very helpful. I’ve observed the following problems:</p>
<ul>
<li>CBCT-segmented model is very different from the surface mesh: there are lots of extra surfaces, which may impact registration accuracy if they are close to the bone surface. Anterior part of the image is cropped, which will also slightly reduce accuracy.</li>
<li>Model registration requires good initialization of the registration, especially in presence of so many extra surface patches in the image-based model. You can to the pre-alignment using Fiducial registration wizard module.</li>
<li>Once the transform is computed, you need to apply it to the model using Data module or Transforms module.</li>
</ul>

---
