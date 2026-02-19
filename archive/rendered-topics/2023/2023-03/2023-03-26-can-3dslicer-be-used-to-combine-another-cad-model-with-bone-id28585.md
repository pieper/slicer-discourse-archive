---
topic_id: 28585
title: "Can 3Dslicer Be Used To Combine Another Cad Model With Bone"
date: 2023-03-26
url: https://discourse.slicer.org/t/28585
---

# Can 3DSlicer be used to combine another CAD model with bone?

**Topic ID**: 28585
**Date**: 2023-03-26
**URL**: https://discourse.slicer.org/t/can-3dslicer-be-used-to-combine-another-cad-model-with-bone/28585

---

## Post #1 by @fea_99 (2023-03-26 13:15 UTC)

<p>I need to perform a finite element analysis of pedicle screw pull out. I plan on using segment mesher to mesh the 3D model from the segmentation in 3DSlicer, and then map the material properties onto the vertebra (from other posts, I understand this is not an issue).</p>
<p>Is it possible to import an external CAD model of the pedicle screw and embed it into the vertebra within 3DSlicer? Or is there a better workflow for this?</p>

---

## Post #2 by @lassoan (2023-03-26 13:25 UTC)

<p>If you just need to combine CAD models with anatomical images or models for rendering then it is trivial. You can simply display both. When the pedicle screw enters into the bone then the bone will occlude it, so it will look as it would look in reality. Pedicle screw insertion is a relatively There have been used by several extensions, both in simple desktop applications and virtual and augmented reality. A few examples:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="XN3Tp8jaYdQ" data-video-title="3D Slicer - Pedicle Screw Surgical Simulator" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=XN3Tp8jaYdQ" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/XN3Tp8jaYdQ/maxresdefault.jpg" title="3D Slicer - Pedicle Screw Surgical Simulator" width="" height="">
  </a>
</div>

<div class="youtube-onebox lazy-video-container" data-video-id="F_UBoE4FaoY" data-video-title="Pedicle screw insertion in virtual reality" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=F_UBoE4FaoY" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/F_UBoE4FaoY/maxresdefault.jpg" title="Pedicle screw insertion in virtual reality" width="" height="">
  </a>
</div>

<p>If you need to combine CAD models and anatomical models to create patient-specific anatomical guides then you need to fuse the two models. An example workflow for this is shown in this video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="2MOAk2oNbKw" data-video-title="Combine patient and CAD models in 3D Slicer using union/intersection/difference operations" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=2MOAk2oNbKw" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/2MOAk2oNbKw/maxresdefault.jpg" title="Combine patient and CAD models in 3D Slicer using union/intersection/difference operations" width="" height="">
  </a>
</div>

<p>A more complex example is the <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner">BoneReconstructionPlanner extension</a>:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="g9Vql5h6uHM" data-video-title="Mandible reconstruction | 3D Slicer Tutorial" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=g9Vql5h6uHM" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/g9Vql5h6uHM/hqdefault.jpg" title="Mandible reconstruction | 3D Slicer Tutorial" width="" height="">
  </a>
</div>


---

## Post #3 by @fea_99 (2023-03-26 16:23 UTC)

<p>Thanks for all the different examples. I think the fusion of the models and then meshing using segementmesher makes the most sense for my use case of pedicle screw pullout strength testing.</p>
<p>However, the output of the fusion/meshing…is it easily importable into FEA software? I am looking into using ANSYS as I have licensing for it, though, if any other FEA software is better in this case I am open to using it.</p>

---

## Post #4 by @lassoan (2023-03-26 22:05 UTC)

<p>Our group mostly uses <a href="https://febio.org/">FEBio</a> (free, open-source biomechanical simulation package), which can directly load VTK files. You can save the CT density value into the volumetric mesh using “Probe volume with model” module.</p>
<p>Other groups are using Abaqus and Ansys, so that should work, too. Maybe they just export surface meshes from Slicer and generate volumetric meshes in Abaqus/Ansys.</p>

---

## Post #5 by @fea_99 (2023-03-27 01:12 UTC)

<p>Great, thanks a lot. I think I have an idea of how that workflow goes now.</p>
<p>However, I seem to be getting an error with the segment mesher:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/7823f13f960404e86d6f4ab1b462d4e03be8a90b.png" data-download-href="/uploads/short-url/h8OiLlFVovMd49awwmrNY4X5o4H.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/7823f13f960404e86d6f4ab1b462d4e03be8a90b.png" alt="image" data-base62-sha1="h8OiLlFVovMd49awwmrNY4X5o4H" width="690" height="92" data-dominant-color="303030"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">892×120 3.85 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Any idea what may be the cause of this error, or if there are any workarounds?</p>

---

## Post #6 by @jamesobutler (2023-03-27 01:38 UTC)

<p>Hi <a class="mention" href="/u/fea_99">@fea_99</a>, that specific code issue was resolved on February 24th, 2023</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/lassoan/SlicerSegmentMesher/commit/3ed2e1ea9c44002ab9724517299765a2723cb960">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerSegmentMesher/commit/3ed2e1ea9c44002ab9724517299765a2723cb960" target="_blank" rel="noopener nofollow ugc">github.com/lassoan/SlicerSegmentMesher</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/lassoan/SlicerSegmentMesher/commit/3ed2e1ea9c44002ab9724517299765a2723cb960" target="_blank" rel="noopener nofollow ugc">Update according to vtkThreshold API changes</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-02-24" data-time="20:35:43" data-timezone="UTC">08:35PM - 24 Feb 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/lassoan/SlicerSegmentMesher/commit/3ed2e1ea9c44002ab9724517299765a2723cb960" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">fixes #14</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please download the latest stable release Slicer 5.2.2 (if you haven’t already) and install the latest version of the extension. <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a></p>
<p>Also see the following thread about staying up-to-date with extensions. As a reminder the latest versions of extensions are only available when using the latest Stable release of Slicer (currently 5.2.2) or the latest Slicer Preview.</p>
<aside class="quote quote-modified" data-post="1" data-topic="24416">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/new-feature-automatic-update-of-extensions/24416">New feature: Automatic update of extensions</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    We have implemented some long-awaited improvements in the Extensions Manager in Slicer-5.0.3. Most importantly extensions can be updated automatically and bookmarks can be used for convenient reinstallation of a list of extensions across different Slicer versions, computers, or users. 
See a half-minute demo video here and details below: 

  <a href="https://www.youtube.com/watch?v=0l2oTonCXFs" target="_blank" rel="noopener nofollow ugc">
    [3D Slicer Extensions Manager redesigned]
  </a>



<a name="new-features-1" class="anchor" href="#new-features-1"></a>New features


Extension update check and installation: Makes it easy for users to keep installed exten…
  </blockquote>
</aside>


---

## Post #7 by @fea_99 (2023-03-27 01:48 UTC)

<p>Thank you so much James. I downloaded 3DSlicer awhile back and did not update the extension/3DSlicer. Cheers.</p>

---
