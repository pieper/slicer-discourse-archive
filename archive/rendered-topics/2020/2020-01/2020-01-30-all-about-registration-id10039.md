---
topic_id: 10039
title: "All About Registration"
date: 2020-01-30
url: https://discourse.slicer.org/t/10039
---

# All about Registration

**Topic ID**: 10039
**Date**: 2020-01-30
**URL**: https://discourse.slicer.org/t/all-about-registration/10039

---

## Post #1 by @banikr (2020-01-30 20:01 UTC)

<p>Hey, I am embarking a project that involves human brain/head registration. I have 100 patient data and would like to register them without losing the inter-subject variability and shape and size of different subjects(morphometricity).<br>
What would be the best registration algorithm to use? For example: affine, deformable/non-rigid registration.<br>
I guess deformable registration will distort different subject head shapes.</p>
<p>Another thing is how to visualize the registration results? Is there a metric or so to compare and monitor the 100 registration process?<br>
Though it is slicer3D forum but I am also familiar with ITK.</p>

---

## Post #2 by @pieper (2020-01-30 21:09 UTC)

<p>Hi -</p>
<p>You can certainly use Slicer for this, but when working on batch processing of neuroimages you may be better off with one of the neuro-specific packages like freesurfer, FSL or SPM.</p>
<p>For slicer registration you could start by looking at examples here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Registration/RegistrationLibrary" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.10/Registration/RegistrationLibrary</a></p>

---

## Post #3 by @banikr (2020-01-30 21:49 UTC)

<p>I have used FSL before, how about ITK?<br>
And I need intersubject size and shape variability to experiment on different heads. I mean anatomical or structural information is top priority to differentiate between subjects(These registered images will also be segmented to create different tissue labels of head)<br>
Which algorithm should I go for like rigid-nonrigid, affine-bspline or deformable?<br>
Thanks for the link it looks helpful.</p>

---

## Post #4 by @pieper (2020-01-30 22:19 UTC)

<p>If you are looking for head-shape differences then maybe SlicerMorph or SlicerSALT would have interesting tools for you.  Also if you do non-rigid registration then the resulting transformation could be thought of as a way to define the variability of the shapes.</p>

---

## Post #5 by @banikr (2020-01-31 03:00 UTC)

<p>Interesting thought.<br>
I need the head shapes intact so was thinking about rigid registration or affine(considering shear and scaling also change the head shapes).</p>
<p>But if I perform non-rigid with respect to either MNI305 or MNI152 or any reference to get the transformation matrix, what non-rigid method you think would be best?</p>
<p>Also to keep in mind that I will segment these registered images to get the different tissue label maps.<br>
I will prefer running a script for 120 3D images rather than registering one by one.</p>
<p>TIA</p>

---

## Post #6 by @lassoan (2020-01-31 03:45 UTC)

<p>If you segment the images then you don’t need registration. You can compute displacements and shape statistics based on those segmented structures.</p>

---

## Post #7 by @timeanddoctor (2020-01-31 04:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="10039">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>ents and shape statistics based on those segmented structures.</p>
</blockquote>
</aside>
<p>If you just statistic the shape you can use the segment statistic module or if you try to get more information you could perform the radiomic analysis.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5957017ca298d4b398563e831951008f51d96d58.png" data-download-href="/uploads/short-url/cKkU2Nxuy0mykr2XVtrnG33AL3O.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5957017ca298d4b398563e831951008f51d96d58_2_611x500.png" alt="image" data-base62-sha1="cKkU2Nxuy0mykr2XVtrnG33AL3O" width="611" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5957017ca298d4b398563e831951008f51d96d58_2_611x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5957017ca298d4b398563e831951008f51d96d58_2_916x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5957017ca298d4b398563e831951008f51d96d58.png 2x" data-dominant-color="CDC8BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1029×841 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @banikr (2020-01-31 07:05 UTC)

<p>Hey, thanks!<br>
I have never used it before. Could you provide some tutorials or links to learn more about it?<br>
Looks very helpful.</p>

---

## Post #9 by @timeanddoctor (2020-01-31 08:31 UTC)

<p>You can search in the forum and you could get what you want.<br>
For example:<br>
1、segment the ROI<br>
2、select which statistic method in ‘segment statistic’ moduel and then apply.<br>
3、The results and the information should be fould just as:</p><aside class="quote quote-modified" data-post="1" data-topic="7303">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/46a35a/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segment-statistics/7303">Segment statistics</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi! 
I have a question regarding the module Segment Statistics. After applying Segement Statistics in 3DSlicer 4.9, 3DSlicer displays two different volumes, volume (1) and (2). 
Please find the attached table here: 
[image] 
What is the difference between these volumes? 
Thanks!
  </blockquote>
</aside>


---

## Post #10 by @banikr (2020-01-31 15:55 UTC)

<p>I was thinking about MultiAtlas segmentation for subcortical brain regions like putamen, substantia-nigra and all. Do you think I won’t need registration(at least rigid/affine) for that reason?<br>
I have used FSL FAST for segmenting peripheral regions such as WM, GM, CSF.</p>

---

## Post #11 by @banikr (2020-01-31 16:58 UTC)

<p>To assign different electromagnetic properties to different tissues for a simulation I will need segmentation labels.<br>
Previous work pipeline included Affine Registration and then MultiAtlas segmentation(MAS).<br>
For MAS, is it mandatory to have registration?<br>
Moreover the head shape and size also has importance the study  I am doing.</p>

---
