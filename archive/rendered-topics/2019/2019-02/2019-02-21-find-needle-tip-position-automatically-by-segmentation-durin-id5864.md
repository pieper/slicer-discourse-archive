---
topic_id: 5864
title: "Find Needle Tip Position Automatically By Segmentation Durin"
date: 2019-02-21
url: https://discourse.slicer.org/t/5864
---

# Find needle tip position automatically by segmentation during needle insertion

**Topic ID**: 5864
**Date**: 2019-02-21
**URL**: https://discourse.slicer.org/t/find-needle-tip-position-automatically-by-segmentation-during-needle-insertion/5864

---

## Post #1 by @s12359e (2019-02-21 07:03 UTC)

<p>Operating system: Win10<br>
Slicer version:4.10.0<br>
Expected behavior:</p>
<p>I make the needle insertion to the phantom as the picture shown.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9678d463814c58dbc000103f8c5bddab9f22117.png" data-download-href="/uploads/short-url/qsabPDVg0wAJHbAILyw4F7PwEbZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9678d463814c58dbc000103f8c5bddab9f22117_2_573x499.png" alt="image" data-base62-sha1="qsabPDVg0wAJHbAILyw4F7PwEbZ" width="573" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9678d463814c58dbc000103f8c5bddab9f22117_2_573x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9678d463814c58dbc000103f8c5bddab9f22117_2_859x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9678d463814c58dbc000103f8c5bddab9f22117.png 2x" data-dominant-color="737494"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1067×930 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>.<br>
I wanna find the needle tip location automatically by segmentation or sort of that.<br>
I try “needle finder” this extensions but I hit “start Giving control point” it didn’t work.<br>
Now i just manually put the fiducial point on the slicer and find the tip position.</p>
<p>Does anyone know how can I figure it out by another methods?</p>
<p>Thanks a lot!</p>

---

## Post #2 by @Yitian_Xian (2022-12-07 06:24 UTC)

<p>Hello, may I know how to configure the needle finder file in my computer? Thanks!</p>

---

## Post #3 by @lassoan (2022-12-08 03:03 UTC)

<p>NeedleFinder project repositories are available here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/needlefinder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/needlefinder" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://avatars.githubusercontent.com/u/20479383?s=280&amp;v=4" class="thumbnail">

<h3><a href="https://github.com/needlefinder" target="_blank" rel="noopener">NeedleFinder</a></h3>

  <p>Needle segmentation from MRI. NeedleFinder has 10 repositories available. Follow their code on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>A simple fully-automatic needle detection algorithm is also discussed here:</p>
<aside class="quote quote-modified" data-post="2" data-topic="26626">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-measure-tip-position-error-and-angle-error-between-two-needles-in-ct-image/26626/2">How to measure tip position error and angle error between two needles in CT image?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Manually specify a line markup that is aligned with needle takes less than one minute (one click near the tip in the 3D view, then click on the dropped point and adjust in slice views; then repeat this for another point along the needle shaft, as far as possible from the tip). 
You could automate the process quite easily, as the needle has very high voxel value, a unique shape, and it is not connected to any other object. For example a fully automatic process could be the following: do threshol…
  </blockquote>
</aside>

<p>If you need to find contrast-filled markers (not needle voids) then you may find the robust tubular marker detection algorithm in ProstateNav useful:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/ProstateBRP/ProstateNav/blob/master/TransRectalProstateRobot/vtkTransRectalFiducialCalibrationAlgo.cxx">
  <header class="source">

      <a href="https://github.com/ProstateBRP/ProstateNav/blob/master/TransRectalProstateRobot/vtkTransRectalFiducialCalibrationAlgo.cxx" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/ProstateBRP/ProstateNav/blob/master/TransRectalProstateRobot/vtkTransRectalFiducialCalibrationAlgo.cxx" target="_blank" rel="noopener">ProstateBRP/ProstateNav/blob/master/TransRectalProstateRobot/vtkTransRectalFiducialCalibrationAlgo.cxx</a></h4>


      <pre><code class="lang-cxx">/*=auto=========================================================================

  Portions (c) Copyright 2007 Brigham and Women's Hospital (BWH) All Rights Reserved.

  See Doc/copyright/copyright.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

  Program:   3D Slicer
  Module:    $RCSfile: $
  Date:      $Date: $
  Version:   $Revision: $

=========================================================================auto=*/

// true=mean detection algo; false=circle detection algo
static const bool USE_MARKER_MEAN_DETECTION=true;
// true: report error if marker is not found; false: if a marker is not found then just use the initial guess
static bool REQUIRE_MARKER_DETECTION=true;
// completely ignore all voxels that are farther from the initial guess line than radius*MAX_RADIUS_TOLERANCE
const double MAX_RADIUS_TOLERANCE=1.8;
</code></pre>



  This file has been truncated. <a href="https://github.com/ProstateBRP/ProstateNav/blob/master/TransRectalProstateRobot/vtkTransRectalFiducialCalibrationAlgo.cxx" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
